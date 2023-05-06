import numpy as np

def hartman6D(x):
    A = np.array([[10, 3, 17, 3.5, 1.7, 8],
                  [0.05, 10, 17, 0.1, 8, 14],
                  [3, 3.5, 1.7, 10, 17, 8],
                  [17, 8, 0.05, 10, 0.1, 14]])
    
    P = np.array([[0.1312, 0.1696, 0.5569, 0.0124, 0.8283, 0.5886],
                  [0.2329, 0.4135, 0.8307, 0.3736, 0.1004, 0.9991],
                  [0.2348, 0.1415, 0.3522, 0.2883, 0.3047, 0.6650],
                  [0.4047, 0.8828, 0.8732, 0.5743, 0.1091, 0.0381]])
    
    alpha = np.array([1.0, 1.2, 3.0, 3.2])
    
    exp_sum = 0
    ret_val = 0
    for i in range(4):
      exp_sum = 0
      for j in range(6):
        exp_sum += A[i][j]*(x[j]-P[i][j])**2
      ret_val += np.dot(alpha[i], np.exp(-exp_sum))
    
    return -ret_val

def rastrigin(x):
    n = len(x)
    A = 10
    return A*n + sum(x[i]**2 - A*np.cos(2*np.pi*x[i]) for i in range(n))


def beale(x):
    return (1.5-x[0]+x[0]*x[1])**2+(2.25-x[0]+x[0]*x[1]**2)**2+(2.625-x[0]+x[0]*x[1]**3)**2


def rosenbrock(x):
    a = 1
    b = 100
    s = sum((b*(x[i+1]-x[i]**2))**2 + (x[i]-a)**2 for i in range(len(x)-1))
    return 
