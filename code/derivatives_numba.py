from numba import jit, prange

@jit(parallel=True, nopython=True)
def dfdx(f, dx, y):
    for i in prange(1, len(y)-1):
        y[i] = (f[i+1] - f[i-1]) / 2*dx
    y[0] = (f[1] - f[0]) / dx
    y[-1] = (f[-1] - f[-2]) / dx
    return y
