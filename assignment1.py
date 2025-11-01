import numpy as np

def find_period(L_0, L_1):
    g = 9.81  # m/s^2
    T_0 = 2 * np.pi * np.sqrt(L_0 / g)
    T_1 = 2 * np.pi * np.sqrt(L_1 / g)
    
    for L in range(L_0, L_1 + 1):
        T = 2 * np.pi * np.sqrt(L / g)
        print("When L = %4.1f m, T = %.1f s" % (L, T))
    
    return (T_0, T_1)