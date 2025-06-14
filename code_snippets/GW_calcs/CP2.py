from math import comb
import numpy as np
import pandas as pd
from fractions import Fraction # GW invariants are rational, so this is more precise

def combb(n,r):
    # A binomial that returns zero whenever arguments are illegal
    if n<0 or r<0:
        return 0
    else:
        return comb(n,r)

def calc_GW(max_degree: int) -> np.array:
    # max_degree: maximum degree
    # Output: N[d] is N_0(d)
    N = np.zeros((max_degree+1),Fraction)
    
    # Initial values
    N[0] = np.nan
    N[1] = Fraction(1,1)
    
    for d in range(2,len(N)):
        # Calculating N_0(d)
        N[d] = 0
        for k in range(1,d):
            l = d-k
            N[d] += k**2*l*N[k]*N[l]*(l*combb(3*d-4,3*k-2)-k*combb(3*d-4,3*k-1))
    return N


def GW_table(max_degree: int) -> pd.DataFrame:
    # Turn GWs into table
    N = calc_GW(max_degree)
    table = pd.DataFrame(N[1:],
                         index = range(1,max_degree+1),
                         columns = ["N_0(d)"])
    table.columns.name = "d"
    return table

if __name__ == "__main__":
    results = GW_table(8).astype(str)
    # Add math mode to all cells
    def str_to_math(x: str) -> str:
        return f"\\\({x}\\\)"
    def str_to_boldmath(x: str) -> str:
        return str_to_math(f"\\boldsymbol{{{x}}}")
    results = results.rename(str_to_boldmath).rename(columns=str_to_boldmath).map(str_to_math)
    results.columns.name = str_to_boldmath("d")

    with open("CP2.md", "w") as f:
        f.write(results.transpose().to_markdown())