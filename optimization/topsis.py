import numpy as np, pandas as pd, matplotlib.pyplot as plt

class TOPSIS:
    def __init__(self, matrix, weights, criteria_types, alternatives=None, criteria=None):
        self.X = np.array(matrix, dtype=float)
        self.w = np.array(weights, dtype=float)
        self.ct = criteria_types
        n, k = self.X.shape
        self.alts = alternatives or [f"A{i+1}" for i in range(n)]
        assert np.isclose(self.w.sum(), 1.0), "Somme poids != 1"
        self._s = None

    def compute(self):
        R = self.X / np.sqrt((self.X**2).sum(0))
        V = R * self.w
        Ap = np.where([t=="benefit" for t in self.ct], V.max(0), V.min(0))
        An = np.where([t=="benefit" for t in self.ct], V.min(0), V.max(0))
        dp = np.sqrt(((V-Ap)**2).sum(1))
        dn = np.sqrt(((V-An)**2).sum(1))
        self._s = dn/(dp+dn)
        return self._s

    def summary(self):
        if self._s is None: self.compute()
        ranks = len(self._s) - np.argsort(np.argsort(self._s))
        df = pd.DataFrame({"Alternative":self.alts,
                           "Score":np.round(self._s,4),
                           "Rang":ranks}).sort_values("Rang")
        print(df.to_string(index=False)); return df

    def plot(self, title="TOPSIS"):
        if self._s is None: self.compute()
        idx = np.argsort(self._s)[::-1]
        plt.figure(figsize=(8,5))
        colors=["#2ecc71" if i==0 else "#3498db" for i in range(len(idx))]
        bars=plt.bar([self.alts[i] for i in idx],[self._s[i] for i in idx],color=colors)
        for b,s in zip(bars,[self._s[i] for i in idx]):
            plt.text(b.get_x()+b.get_width()/2,b.get_height()+0.01,f"{s:.3f}",ha="center")
        plt.ylim(0,1.1); plt.title(title); plt.tight_layout()
        plt.savefig("topsis_results.png",dpi=150); plt.show()

if __name__ == "__main__":
    alts = ["Al2O3/Al","ZrO2/Al","Si3N4/SUS304","Al2O3/Ti","ZrO2/Ti"]
    M = np.array([[5.12,38.2,6.25,225.0],[4.87,36.5,8.25,135.0],
                  [6.21,58.1,6.30,265.1],[5.48,42.3,5.57,213.9],[5.09,38.9,5.06,152.9]])
    w = np.array([0.35,0.30,0.20,0.15])
    t = TOPSIS(M, w, ["benefit","benefit","cost","benefit"], alts)
    t.compute(); t.summary()
    t.plot("Selection materiaux FGM - TOPSIS (JANANE ALLAH et al., 2022)")
