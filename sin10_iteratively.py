"""
Compute sin(10°) by transforming a trigonometric identity into a cubic equation:

    sin(3x) = 3sin(x) - 4sin^3(x)

Using sin(30°) = 1/2, we obtain:
    8x^3 - 6x + 1 = 0

The root corresponding to sin(10°) is solved using Newton-Raphson
with arbitrary precision arithmetic (mpmath).
"""

import mpmath as mp
mp.mp.dps = 50 #50-decimal precision

def f(x):
    return 8*x**3 - 6*x + 1

def f_prime(x):
    return 24*x**2 - 6

steps = []

iterations = 10
approx = mp.mpf(0.25)
delta = mp.mpf(0)
true_val = mp.sin(mp.radians(10))

for epoch in range(iterations):
    steps.append(approx)
    
    delta = f(approx)/(-f_prime(approx))
    approx += delta

    if abs(delta) < mp.mpf('1e-50'):
        print(f"Converged at iteration {epoch+1}")
        break
    
    error = abs(approx - true_val)
    print(f"Iter {epoch+1}: approx = {approx}, error = {error}")

print("\nFinal Approximation:", approx)
print("True Value        :", true_val)
print("Absolute Error    :", abs(approx - true_val))