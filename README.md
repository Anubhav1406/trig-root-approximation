# Trigonometric Approximation via Polynomial Root Finding

This project demonstrates how a trigonometric value can be computed by transforming the problem into a polynomial equation and solving it using numerical methods.

---

## 🧠 Idea

Using the triple-angle identity:

$$
\sin(3x) = 3\sin(x) - 4\sin^3(x)
$$

and the known value:

$$
\sin(30^\circ) = \frac{1}{2}
$$

we derive a cubic equation:

$$
8x^3 - 6x + 1 = 0
$$

The solution to this equation gives:

$$
y = \sin(10^\circ)
$$

---

## ⚙️ Method

The cubic equation is solved using the Newton-Raphson method, an iterative root-finding algorithm:

$$
x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}
$$

Where:

- f(x) = 8x^3 - 6x + 1  
- f'(x) = 24x^2 - 6  

We use the mpmath library to achieve high-precision arithmetic (50 decimal places).

---

## 🚀 Features

- Analytical transformation of a trigonometric problem into a polynomial  
- Implementation of Newton-Raphson method  
- Arbitrary precision computation using mpmath  
- Fast convergence (~6 iterations for 50-digit accuracy)  
- Error tracking against true value  

---

## 📊 Sample Output

Iter 1: approx = 0.166666..., error ≈ 7e-3  
Iter 2: approx = 0.173611..., error ≈ 3e-5  
Iter 3: approx = 0.173648..., error ≈ 1e-9  
Iter 4: approx = 0.173648..., error ≈ 1e-18  
Iter 5: approx = 0.173648..., error ≈ 1e-37  
Iter 6: approx = 0.173648..., error ≈ 0  

---

## 📌 Key Insight

This project highlights how:

- Analytical identities can simplify computation  
- Nonlinear problems can be reduced to polynomial equations  
- Iterative numerical methods can achieve extremely high precision efficiently  

---

## 🛠️ Requirements

pip install mpmath

---

## ▶️ Run

python sin10_iteratively.py

---

## 📁 Files

- sin10_iteratively.py → clean implementation  
- sin10_derivation.ipynb → step-by-step derivation and reasoning  

---

## 🧩 Future Work

- Compare with Taylor series approximation  
- Analyze convergence rates of different methods  
- Extend approach to other trigonometric transformations  