from matplotlib import rc
from matplotlib.ticker import MaxNLocator
import numpy as np
import matplotlib.pyplot as plt
from simple import *
from matplotlib.ticker import FuncFormatter
plt.rcParams['text.latex.preamble'] = r"\usepackage{lmodern}"

rc('text', usetex=True)
rc(
    'font',
    family='serif',
    serif=['Computer Modern Roman'],
    monospace=['Computer Modern Typewriter'],
    size=20
)


B0_VALUE = 10000

def percentage_formatter(x, pos):
    return f'{x * 100 :.0f}\%'

def replace_all_values(ex):
  return ex.subs(b0, B0_VALUE).subs(p, 0.5)

def u_plot():
  u_values = list(np.arange(1.0, 10000.0, 10.0))
  fig, (ax1) = plt.subplots(1, figsize=(7, 5))

  plt.xlabel(r'Adversary market domination $\frac{u}{b_0}$', labelpad=15)
  plt.ylabel(r'$\frac{\phi}{q}$', rotation=0, labelpad=15, fontsize=25)
  ax1.xaxis.set_major_locator(MaxNLocator(nbins=5))
  ax1.yaxis.set_major_locator(MaxNLocator(nbins=5, prune='lower'))
  ax1.axis([0, 1, 0, 100])
  ax1.xaxis.set_major_formatter(FuncFormatter(percentage_formatter))

  b_with_values = replace_all_values(b_expression)

  w0 = solve(alpha, w)[0]
  w_values = []
  w0 = replace_all_values(w0)
  print(w0)
  w_values = [1 / w0.subs(u, value) for value in u_values]
  ax1.plot(list(map(lambda a: a / B0_VALUE, u_values)), w_values, lw=2, color='black')

  u_list = list(np.arange(1, 10100, 50)) # 100
  w_list = list(np.arange(0, 101, 0.5))

  alpha_list = []
  for wt in w_list:
    alpha_list.append([])
    for ut in u_list:
      #old_alpha = replace_all_values(alpha.subs(u, ut).subs(1 / w, wt))
      m = replace_all_values(max_b.subs(1 / w, wt).subs(u, ut))
      bounded_b = max(min(b_with_values.subs(u, ut).subs(1 / w, wt).evalf(), m), 0)
      corrected_alpha = replace_all_values(alpha_with_b.subs(b, bounded_b).subs(u, ut).subs(1 / w, wt).evalf())

      if b_with_values.subs(u, ut).subs(1 / w, wt) > m:
        print('pro')

      corrected_alpha -= 0.1
      alpha_list[len(alpha_list) - 1].append(100 * corrected_alpha / 10000)

  alpha_list = np.array(alpha_list, dtype=float)
  plt.contourf(list(map(lambda a: a/10000, u_list)), w_list, alpha_list, levels=np.linspace(0, 40, 11), cmap='RdYlBu_r')
  cbar = plt.colorbar()
  cbar.ax.tick_params(labelsize=18)
  cbar.ax.set_title(r"\begin{center}profit\\$\frac{\alpha}{b_0}$\end{center}", fontsize=18, pad=32, ha='center', va='center')
  cbar.locator = MaxNLocator(nbins=6)
  cbar.set_ticks(np.linspace(0, 40, 6))
  tick_labels = ['{}\%'.format(int(x)) for x in cbar.get_ticks()]
  cbar.set_ticklabels(tick_labels)

u_plot()

plt.savefig("plotu_contour_alpha.pdf", bbox_inches = "tight")
