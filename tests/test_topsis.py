import sys, os, numpy as np
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from optimization.topsis import TOPSIS
from fgm.material_properties import fgm_properties, volume_fraction, MATERIALS

def test_scores_range():
    s=TOPSIS(np.array([[5,10],[8,6],[3,9]]),np.array([0.6,0.4]),["benefit","benefit"]).compute()
    assert all(0<=x<=1 for x in s); print("OK scores_range")

def test_dominant_wins():
    s=TOPSIS(np.array([[10,10],[5,5],[1,1]]),np.array([0.5,0.5]),["benefit","benefit"]).compute()
    assert s[0]>s[1]>s[2]; print("OK dominant_wins")

def test_cost():
    s=TOPSIS(np.array([[100],[10]]),np.array([1.0]),["cost"]).compute()
    assert s[1]>s[0]; print("OK cost_criterion")

def test_fgm_bounds():
    h=0.01
    assert np.isclose(volume_fraction(h/2,h,1),1.0)
    assert np.isclose(volume_fraction(-h/2,h,1),0.0); print("OK fgm_bounds")

def test_fgm_n0():
    p=fgm_properties(0.0,0.01,n=0)
    assert np.isclose(p["E"],MATERIALS["Al2O3"]["E"],rtol=1e-6); print("OK fgm_n0_ceramic")

for t in [test_scores_range,test_dominant_wins,test_cost,test_fgm_bounds,test_fgm_n0]:
    try: t()
    except Exception as e: print(f"FAIL {t.__name__}: {e}")
print("Tests termines.")
