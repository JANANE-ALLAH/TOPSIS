import numpy as np

MATERIALS = {
    "Al":    {"E": 70e9,  "nu": 0.3,    "rho": 2702.0},
    "Al2O3": {"E": 380e9, "nu": 0.3,    "rho": 3800.0},
    "ZrO2":  {"E": 200e9, "nu": 0.3,    "rho": 5700.0},
    "Si3N4": {"E": 322.3e9,"nu": 0.24,  "rho": 2370.0},
    "SUS304":{"E": 207.8e9,"nu": 0.3177,"rho": 8166.0},
    "Ti-6Al-4V":{"E":105.7e9,"nu":0.2981,"rho":4429.0},
}

def volume_fraction(z, h, n):
    return (z / h + 0.5) ** n

def fgm_properties(z, h, n, ceramic="Al2O3", metal="Al"):
    c, m = MATERIALS[ceramic], MATERIALS[metal]
    Vc = volume_fraction(z, h, n)
    return {"E": c["E"]*Vc + m["E"]*(1-Vc),
            "nu": c["nu"]*Vc + m["nu"]*(1-Vc),
            "rho": c["rho"]*Vc + m["rho"]*(1-Vc)}

def nondim_frequency(a, h, n, ceramic="Al2O3", metal="Al", nz=100):
    z = np.linspace(-h/2, h/2, nz)
    E   = np.array([fgm_properties(zi,h,n,ceramic,metal)["E"]   for zi in z])
    nu  = np.array([fgm_properties(zi,h,n,ceramic,metal)["nu"]  for zi in z])
    rho = np.array([fgm_properties(zi,h,n,ceramic,metal)["rho"] for zi in z])
    D11 = np.trapz(E*z**2/(1-nu**2), z)
    I0  = np.trapz(rho, z)
    lam = np.pi / a
    omega = np.sqrt(D11 * lam**4 / I0)
    mat_m = MATERIALS[metal]
    return omega * (a**2/h) * np.sqrt(mat_m["rho"]/mat_m["E"])

def generate_dataset(n_samples=500, random_state=42):
    rng = np.random.default_rng(random_state)
    n_v  = rng.uniform(0, 10, n_samples)
    ah   = rng.uniform(5, 50, n_samples)
    ab   = rng.uniform(0.5, 2, n_samples)
    h = 0.01
    X = np.column_stack([n_v, ah, ab])
    y = np.array([nondim_frequency(a*h, h, n) / (b**0.5)
                  for n, a, b in zip(n_v, ah, ab)])
    return X, y

if __name__ == "__main__":
    print("=== Frequences FGM Al/Al2O3 (SSSS, a/h=10) ===")
    for n in [0, 0.5, 1, 2, 5]:
        print(f"  n={n} -> Omega = {nondim_frequency(0.1, 0.01, n):.4f}")
