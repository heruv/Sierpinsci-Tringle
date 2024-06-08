import numpy as np
import scipy.constants as const

Vs = 10
Ps = 20
Vf = 4
Pf = 34
T = 100
P = 21
k = 1.2

dU = 5 * const.R / 3 * T

# численное выччисление
A = dU + (Ps-Pf) * (Vf-Vs)
A = P * Vs * (Vf**(1-k)-Vs**(1-k))/1-k
# anal
Aa = P*(Vs*np.log(Vf/Vs))

print(f"{A}, \n {Aa}")
