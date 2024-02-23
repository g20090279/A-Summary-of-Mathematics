import numpy as np
from scipy.stats import unitary_group
from scipy.linalg import qr

A = unitary_group.rvs(5)
q, r = qr(A)

print("a unitary matrix")
print(A)
print("Q")
print(q)
print("R")
print(r)
