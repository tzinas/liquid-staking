from base import *

def replace_all_values(ex):
  return replace_known_values(ex.subs(f, 1))

def u_plot():
  fig, (ax1) = plt.subplots(1, figsize=(7, 5))

  plt.xlabel(r'Adversary market domination $\frac{u}{b_0}$', labelpad=15)
  plt.ylabel(r'$\frac{q}{\phi}$', rotation=0, labelpad=15)
  ax1.xaxis.set_major_locator(MaxNLocator(nbins=5))
  ax1.yaxis.set_major_locator(MaxNLocator(nbins=5, prune='lower'))
  ax1.axis([0, 1, 0, 100])

  b_with_values = replace_all_values(b_expression)

  w0 = solve(alpha, w)[0]
  labels = []

  for uβ, color in [(0, 'black'), (0.01, 'red'), (0.02, 'orange'), (0.03, 'green')]:
    w_values = []
    u_values = []
    wt = replace_all_values(w0.subs(β,uβ))
    for u_value in np.arange(1.0, 10000.0, 10):
      sw = wt.subs(u, u_value)
      if (sw < 0):
        continue

      w_values.append(1 / sw)
      u_values.append(u_value)

    ax1.plot(list(map(lambda a: a/10000, u_values)), w_values, lw=2, color=color)
    labels.append(r'{}'.format(uβ))

  ax1.legend(fontsize=22, title=r'Flash loan cost ($\beta_{st}$)', labels=labels)

u_plot()

plt.savefig("plotu_compare_beta.pdf", bbox_inches = "tight")