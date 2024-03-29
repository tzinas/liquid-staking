from base import *
from matplotlib.ticker import FuncFormatter

def percentage_formatter(x, pos):
    return f'{x * 100 :.0f}\%'

def u_plot():
  fig, (ax1) = plt.subplots(1, figsize=(7, 5))

  plt.xlabel(r'Adversary market domination $\frac{u}{b_0}$', labelpad=15)
  plt.ylabel(r'$\frac{\phi}{q}$', rotation=0, labelpad=15)
  ax1.xaxis.set_major_locator(MaxNLocator(nbins=5))
  ax1.yaxis.set_major_locator(MaxNLocator(nbins=5, prune='lower'))
  ax1.axis([0, 1, 0, 120])

  ax1.xaxis.set_major_formatter(FuncFormatter(percentage_formatter))

  w0 = solve(alpha, w)[0]
  labels = []

  for uf, color in [(1, 'black'), (1.01, 'red'), (1.02, 'orange'), (1.03, 'green')]:
    w_values = []
    u_values = []
    wt = replace_known_values(w0.subs(f,uf))
    for u_value in np.arange(1.0, 10000.0, 10):
      sw = wt.subs(u, u_value)
      if (sw < 0):
        continue

      w_values.append(1 / sw)
      u_values.append(u_value)

    ax1.plot(list(map(lambda a: a/10000, u_values)), w_values, lw=2, color=color)
    labels.append(r'{}\%'.format(int(uf * 100)))

  ax1.legend(fontsize=20, title=r'Loan cost $f$', labels=labels)

u_plot()

plt.savefig("plotu_compare_f.pdf", bbox_inches = "tight")
