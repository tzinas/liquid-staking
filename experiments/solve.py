from pprint import pprint
from sympy import Symbol, solve, sqrt, Eq, pretty
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import rc
from matplotlib.ticker import MaxNLocator
from matplotlib.colors import SymLogNorm
import numpy as np
plt.rcParams['text.latex.preamble'] = r"\usepackage{lmodern}"

rc('text', usetex=True)
rc(
    'font',
    family='serif',
    serif=['Computer Modern Roman'],
    monospace=['Computer Modern Typewriter'],
    size=20
)

w = Symbol('w', positive=True, real=True)
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

def solveqφ():
  return solve(alpha, w)[0]

def double_check(expr1, expr2):
  return expr1 == expr2

def replace_all_values(ex):
  return ex.subs(u, 3000).subs(b0, 10000).subs(β, 0).subs(p, 0.5).subs(γ, 1.2)

def f_plot():
  f_values = list(np.arange(1.0, 1.21, 0.001))
  fig = plt.figure(figsize=(20, 10))
  ax1 = fig.add_subplot(1, 2, 1)
  ax2 = fig.add_subplot(1, 2, 2)
  plt.subplots_adjust(left=0.13, bottom=0.2)
  #ax1.set_title(r'Attack profitability {\LARGE($\frac{u}{b_0} = 20\%$)}', pad=18)
  plt.xlabel(r'Cost of borrowing ($f$)', labelpad=15)
  plt.ylabel(r'$\frac{\phi}{q}$', rotation=0, labelpad=15, fontsize=25)
  ax1.xaxis.set_major_locator(MaxNLocator(nbins=5, integer=True))
  ax1.yaxis.set_major_locator(MaxNLocator(nbins=5, integer=True, prune='lower'))
  #ax1.legend(fontsize=13, title=r'$\frac{u}{b_0}$', labels=[r'20\%', r'30\%', r'40\%', r'50\%'])
  ax1.axis([1.0, 1.2, 0, 120])

  alpha_with_values = replace_all_values(alpha)
  b_with_values = replace_all_values(b_expression)

  w0 = solve(alpha, w)[0]
  print(w0)
  w0 = replace_all_values(w0)

  w_values = [1 / w0.subs(f, value) for value in f_values]
  #ax1.plot(f_values, w_values, lw=2, color='purple')

  f_list = np.arange(1, 1.22, 0.05)
  w_list = np.arange(1, 121, 1)

  alpha_list = []
  for wt in w_list:
    alpha_list.append([])
    for ft in f_list:
      bounded_b = max(min(b_with_values.subs(f, ft).subs(w, 1/wt).evalf(), 10000), 0)
      corrected_alpha = replace_all_values(alpha_with_b.subs(b, bounded_b).subs(f, ft).subs(w, 1/wt))

      alpha_list[len(alpha_list) - 1].append(100 * corrected_alpha / 10000)


  plt.contourf(f_list, w_list, alpha_list, levels=np.linspace(0, 10, 11), cmap='RdYlBu')
  cbar = plt.colorbar()
  cbar.ax.tick_params(labelsize=16)
  cbar.ax.set_title(r"$\frac{\alpha}{b_0}$", fontsize=22, pad=16)
  tick_labels = ['{}\%'.format(x) for x in cbar.get_ticks()]
  cbar.locator = MaxNLocator(nbins=6)
  cbar.set_ticklabels(tick_labels)
  plt.savefig("plotf.pdf", bbox_inches = "tight")

def u_plot():
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

f_plot()
#print(solveqφ())
#print('pretty:', pretty(solveqφ()))
#print(double_check((1/(b0*γ)) * (f*p*u + f*u - b0*β*γ - 2*u*sqrt(f*p*(f-1)) - u), solveqφ()))
#plt.show()