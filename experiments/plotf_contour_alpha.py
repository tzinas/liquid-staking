from base import *

MARKET_DOMINATION = 0.5

def replace_all_values(ex):
  return replace_known_values(ex.subs(u, MARKET_DOMINATION * B0_VALUE).subs(β, 0.0009))

def u_plot():
  f_values = list(np.arange(1.0, 1.21, 0.001))
  fig, (ax1) = plt.subplots(1, figsize=(7, 5))

  plt.xlabel(r'Loan cost factor $f$', labelpad=15)
  plt.ylabel(r'$\frac{\phi}{q}$', rotation=0, labelpad=15)
  ax1.xaxis.set_major_locator(MaxNLocator(nbins=5))
  ax1.yaxis.set_major_locator(MaxNLocator(nbins=4, prune='lower'))
  ax1.axis([1, 1.2, 0, 120])

  b_with_values = replace_all_values(b_expression)

  w0 = solve(alpha, w)[0]
  w_values = []
  w0 = replace_all_values(w0)
  w_values = [1 / w0.subs(f, value) for value in f_values]
  ax1.plot(f_values, w_values, lw=2, color='black')

  w_list = list(np.arange(1, 121, 1)) # 100
  f_list = list(np.arange(1.0, 1.21, 0.01))

  alpha_list = []
  for wt in w_list:
    alpha_list.append([])
    for ft in f_list:
      #old_alpha = replace_all_values(alpha.subs(u, ut).subs(1 / w, wt))
      m = replace_all_values(max_b.subs(1 / w, wt).subs(f, ft))
      bounded_b = max(min(b_with_values.subs(f, ft).subs(1 / w, wt).evalf(), m), 0)
      corrected_alpha = replace_all_values(alpha_with_b.subs(b, bounded_b).subs(f, ft).subs(1 / w, wt).evalf())

      if b_with_values.subs(f, ft).subs(1 / w, wt) > m:
        print('pro')

      corrected_alpha -= 0.2
      alpha_list[len(alpha_list) - 1].append(100 * corrected_alpha / B0_VALUE)


  plt.contourf(f_list, w_list, alpha_list, levels=np.linspace(0, 12, 13), cmap='RdYlBu')
  cbar = plt.colorbar()
  cbar.ax.tick_params(labelsize=20)
  cbar.ax.set_title(r"\begin{center}profit\\$\frac{\alpha}{b_0}$\end{center}", fontsize=22, pad=32, ha='center', va='center')
  cbar.locator = MaxNLocator(nbins=5)
  cbar.set_ticks(np.linspace(0, 12, 5))
  tick_labels = ['{}\%'.format(int(x)) for x in cbar.get_ticks()]
  cbar.set_ticklabels(tick_labels)

u_plot()

plt.savefig("plotf_contour_alpha.pdf", bbox_inches = "tight")