from base import *
from matplotlib.ticker import FuncFormatter

def replace_values(ex):
  return ex.subs(b0, B0_VALUE).subs(β, 0.0009).subs(p, 0.5).subs(f, 1)

def percentage_formatter(x, pos):
    return f'{x * 100 :.0f}\%'

def u_plot():
  fig, (ax1) = plt.subplots(1, figsize=(7, 5))

  plt.xlabel(r'Adversary market domination $\frac{u}{b_0}$', labelpad=15)
  plt.ylabel(r'$\frac{\phi}{q}$', rotation=0, labelpad=15)
  ax1.xaxis.set_major_locator(MaxNLocator(nbins=5))
  ax1.yaxis.set_major_locator(MaxNLocator(nbins=5, prune='lower'))
  ax1.axis([0, 1, 0, 120])
  #ax1.set_xscale("log", base=2)
  #ax1.set_yscale("log", base=2)

  ax1.xaxis.set_major_formatter(FuncFormatter(percentage_formatter))

  w0 = solve(alpha, w)[0]
  labels = []

  for ugamma, color in [(1, 'black'), (1.5, 'red'), (2, 'orange'), (2.5, 'green')]:
    w_values = []
    u_values = []
    wt = replace_values(w0.subs(γ,ugamma))
    print(wt)
    for u_value in np.arange(1.0, 10000.0, 10):
      sw = wt.subs(u, u_value)
      if (sw < 0):
        continue

      w_values.append(1 / sw)
      u_values.append(u_value)

    ax1.plot(list(map(lambda a: a/10000, u_values)), w_values, lw=2, color=color)
    labels.append(r'{}\%'.format(int(ugamma * 100)))

  ax1.legend(fontsize=20, title=r'Collateral ratio $\gamma_{\textsf{st}}$', labels=labels)

u_plot()

plt.savefig("plotu_compare_gamma.pdf", bbox_inches = "tight")
