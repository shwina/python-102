import numpy as np

def dfdx(f, dx, y):
   y[1:-1] = (f[2:] - f[:-2]) / (2*dx)
   y[0] = (f[1] - f[0]) / dx
   y[1] = (f[-2] - f[-1]) / dx
   return y
