from sympy import Symbol, solve, sqrt, pretty
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import rc
from matplotlib.ticker import MaxNLocator
import numpy as np
plt.rcParams['text.latex.preamble'] = r"\usepackage{lmodern}"

rc('text', usetex=True)
rc(
    'font',
    family='serif',
    serif=['Computer Modern Roman'],
    monospace=['Computer Modern Typewriter'],
    size=25
)

w = Symbol('w', positive=True, real=True)

q = Symbol('w', positive=True, real=True)
φ = Symbol('w', positive=True, real=True)

u = Symbol('u', positive=True, real=True)
f = Symbol('f', positive=True, real=True)
β = Symbol('β', nonnegative=True, real=True)
p = Symbol('p', positive=True, real=True)
γ = Symbol('γ', positive=True, real=True)
b0 = Symbol('b0', positive=True, real=True)
b = Symbol('b', positive=True, real=True)

b_star = u / γ
g = (u * f * p * b0) / γ
alpha_with_b = b_star - (1 - p * (b / (b0 + b))) * f * (u / γ) - w * b - β * b

b_expression = sqrt(g / (β + w)) - b0
alpha = alpha_with_b.subs(b, b_expression)

max_b = u / ((w + β) * γ)

B0_VALUE = 10000

def replace_known_values(ex):
  return ex.subs(b0, B0_VALUE).subs(β, 0.0009).subs(p, 0.5).subs(γ, 1.46)