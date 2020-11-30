from qvalue import qvalue
import numpy as np

"""
	pv : pvalue
    m: number of tests. (default pv.size) 
    verbose: print verbose messages? (default False)
    lowmem: use memory-efficient in-place algorithm
    pi0: if None, it's estimated as suggested in Storey and Tibshirani, 2003.
         For most GWAS this is not necessary, since pi0 is extremely likely to be
         1
"""

print(qvalue.estimate(np.asarray([0.1,0.05,0.025, 0.000001])))