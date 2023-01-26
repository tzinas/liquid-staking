from base import *

def replace_all_values(ex):
  return replace_known_values(ex.subs(f, 1))

def u_plot():
  u_values = list(np.arange(1.0, 10000.0, 10.0))
  fig, (ax1) = plt.subplots(1, figsize=(7, 5))

  plt.xlabel(r'Adversary market domination $\frac{u}{b_0}$', labelpad=15)
  plt.ylabel(r'$\frac{\phi}{q}$', rotation=0, labelpad=15, fontsize=25)
  ax1.xaxis.set_major_locator(MaxNLocator(nbins=5))
  ax1.yaxis.set_major_locator(MaxNLocator(nbins=5, prune='lower'))
  ax1.axis([0, 1, 0, 100])

  b_with_values = replace_all_values(b_expression)

  u_list = list(np.arange(1, 10100, 100)) # 100
  w_list = list(np.arange(0, 101, 0.5))

  beta_list = []
  for wt in w_list:
    beta_list.append([])
    print("------", wt)
    for ut in u_list:
      #old_alpha = replace_all_values(alpha.subs(u, ut).subs(1 / w, wt))
      m = replace_all_values(max_b.subs(w, 1 / wt).subs(u, ut))
      bounded_b = max(min(b_with_values.subs(u, ut).subs(w, 1 / wt).evalf(), m), 0)
      bounded_b = -1 if bounded_b <= 0.1 else bounded_b

      beta_list[len(beta_list) - 1].append(100 * bounded_b / 10000)

  print(beta_list)

  plt.contourf(list(map(lambda a: a/10000, u_list)), w_list, beta_list, levels=np.linspace(0, 650, 11), cmap='RdYlBu')
  cbar = plt.colorbar()
  cbar.ax.tick_params(labelsize=16)
  cbar.ax.set_title(r"$\frac{\alpha}{b_0}$", fontsize=22, pad=16)
  cbar.locator = MaxNLocator(nbins=6)
  cbar.set_ticks(np.linspace(0, 45, 6))
  tick_labels = ['{}\%'.format(int(x)) for x in cbar.get_ticks()]
  cbar.set_ticklabels(tick_labels)

u_plot()

plt.savefig("plotu_contour_beta.pdf", bbox_inches = "tight")