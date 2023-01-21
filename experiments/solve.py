from pprint import pprint
from sympy import Symbol, solve, sqrt
import matplotlib.pyplot as plt
import numpy as np

w = Symbol('w', positive=True, real=True)

u = Symbol('u', positive=True, real=True)
f = Symbol('f', positive=True, real=True)
β = Symbol('β', nonnegative=True, real=True)
p = Symbol('p', positive=True, real=True)
γ = Symbol('γ', positive=True, real=True)
b0 = Symbol('b0', positive=True, real=True)
b_star = u / γ # Symbol('b^*', positive=True, real=True)
g = (u * f * p * b0) / γ # Symbol('g', positive=True, real=True)
b = sqrt(g / (β + w)) - b0 # Symbol('b', positive=True, real=True)
alpha = b_star - (1 - p * (b / (b0 + b))) * f * (u / γ) - w * b - β * b

ws = solve(alpha, w)[0]
print(ws)

def get_profit(u, f):
  β = 0 # Symbol('β', nonnegative=True, real=True)
  p = 0.8 # Symbol('p', positive=True, real=True)
  γ = 1.2 # Symbol('γ', positive=True, real=True)
  b0 = 10000 # Symbol('b0', positive=True, real=True)
  # b = Symbol('b', positive=True, real=True)
  b_star = u / γ # Symbol('b^*', positive=True, real=True)
  g = (u * f * p * b0) / γ # Symbol('g', positive=True, real=True)
  b = sqrt(g / (β + w)) - b0 # Symbol('b', positive=True, real=True)
  return b_star - (1 - p * (b / (b0 + b))) * f * (u / γ) - w * b - β * b

def f_plot():
  f_values = list(np.arange(1.0, 1.2, 0.001))

  fig, (ax1) = plt.subplots(1)

  for u, color in [(2000, 'blue'), (3000, 'red'), (4000, 'green'), (5000, 'purple')]:
    alpha = get_profit(u, f)
    w0 = solve(alpha, w)[0]
    w_values = [1 / w0.subs(f, value) for value in f_values]
    ax1.plot(f_values, w_values, lw=2, color=color)

  ax1.set_xlabel('Cost of borrowing (f)')
  ax1.set_ylabel('φ/q')
  ax1.legend(['20%', '30%', '40%', '50%'])
  ax1.axis([1.0, 1.2, 0, 25])

def b_plot():
  u_values = list(np.arange(1.0, 10000.0, 1.0))
  fig, (ax1) = plt.subplots(1)

  alpha = get_profit(u, 1.03)
  w0 = solve(alpha, w)[0]
  w_values = [1 / w0.subs(u, value) for value in u_values]
  #b_b0_values = [1 / w0.subs(u, value) for value in u_values]

  ax1.plot(list(map(lambda a: a/10000, u_values)), w_values, lw=2, color='blue')
  ax1.set_xlabel('u/b0')
  ax1.set_ylabel('φ/q')
  ax1.axis([0, 1, 0, 100])

#b_plot()
plt.show()