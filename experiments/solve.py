from pprint import pprint
from sympy import Symbol, solve, sqrt

for u in range(1000, 10000, 1000):
  β = 0 # Symbol('β', nonnegative=True, real=True)
  f = 1.03 # Symbol('f', positive=True, real=True)
  # u = 10000 # Symbol('u', positive=True, real=True)
  p = 0.8 # Symbol('p', positive=True, real=True)
  γ = 1.2 # Symbol('γ', positive=True, real=True)
  b0 = 3000 # Symbol('b0', positive=True, real=True)
  w = Symbol('w', positive=True, real=True)
  # b = Symbol('b', positive=True, real=True)
  b_star = u / γ # Symbol('b^*', positive=True, real=True)
  g = (u * f * p * b0) / γ # Symbol('g', positive=True, real=True)
  b = sqrt(g / (β + w)) - b0 # Symbol('b', positive=True, real=True)

  alpha = b_star - (1 - p * (b / (b0 + b))) * f * (u / γ) - w * b - β * b

  # print(alpha)
  w0 = solve(alpha, w)[0]
  print('u: ', u, 'w: ', w0)
  alpha = alpha.subs(w, w0)
  print('alpha: ', alpha)
