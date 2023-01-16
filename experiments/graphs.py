import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons

fig, (ax1, ax2) = plt.subplots(1,2)
plt.subplots_adjust(left=0.15, bottom=0.6)
u = np.arange(0.0, 10000.0, 1)
s = 0 * u
l, = ax1.plot(u, s, lw=2, color='blue')
r, = ax1.plot(u, s, lw=2, color='red')
w, = ax1.plot(u, s, lw=2, color='orange')
bp, = ax1.plot(u, s, lw=2, color='pink')
pr, = ax2.plot(u, s, lw=2, color='green')
max_b_plot, = ax2.plot(u, s, lw=2, color='red')

ax1.set_xlabel('Initial capital u (ASSET)')
ax1.set_ylabel('ASSET')
ax1.legend(['Shorting profit', 'Cost', 'Profit', 'Maximum profit'])
ax1.axis([0, 10000, 0, 6000])

ax2.set_xlabel('Initial capital u (ASSET)')
ax2.set_ylabel('Ideal b (ASSET)')
ax2.axis([0, 10000, 0, 10000])

axcolor = 'lightgoldenrodyellow'

ax_beta_asset = plt.axes([0.25, 0.05, 0.65, 0.03], facecolor=axcolor)
ax_f = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
ax_b_0 = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)
ax_s_0 = plt.axes([0.25, 0.2, 0.65, 0.03], facecolor=axcolor)
ax_gama_stasset = plt.axes([0.25, 0.25, 0.65, 0.03], facecolor=axcolor)
ax_p = plt.axes([0.25, 0.3, 0.65, 0.03], facecolor=axcolor)
ax_q = plt.axes([0.25, 0.35, 0.65, 0.03], facecolor=axcolor)
ax_fi = plt.axes([0.25, 0.4, 0.65, 0.03], facecolor=axcolor)
ax_b = plt.axes([0.25, 0.45, 0.65, 0.03], facecolor=axcolor)

beta_asset = Slider(ax_beta_asset, 'beta_asset', 0.001, 1, valinit=0.003)
f = Slider(ax_f, 'f', 1, 10.1, valinit=1.03)
b_0 = Slider(ax_b_0, 'b_0', 1, 100000, valinit=10000)
s_0 = Slider(ax_s_0, 's_0', 1, 10000, valinit=10000)
gama_stasset = Slider(ax_gama_stasset, 'gama_stasset', 1, 1.5, valinit=1.2)
p = Slider(ax_p, 'p', 0, 1, valinit=0.3)
q = Slider(ax_q, 'q', 0, 1, valinit=0.3)
fi = Slider(ax_fi, 'fi', 0, 20, valinit=10)
b = Slider(ax_b, 'b', 0, 10000, valinit=10000)

def update(val = None):
    z = (u * s_0.val) / (b_0.val * gama_stasset.val)
    b_star = z * b_0.val / s_0.val
    b_prime = (b_0.val / s_0.val) * (1 - p.val * b.val / (b_0.val + b.val)) * f.val * z

    shorting_profit = b_star - b_prime
    expenses = beta_asset.val * b.val + q.val * b.val / fi.val

    ideal_b = np.maximum(0, np.minimum(u / ((1 / fi.val + beta_asset.val) * gama_stasset.val), np.sqrt((u * f.val * p.val * b_0.val) / (gama_stasset.val * (beta_asset.val + q.val / fi.val))) - b_0.val))

    ideal_b_prime = (b_0.val / s_0.val) * (1 - p.val * ideal_b / (b_0.val + ideal_b)) * f.val * z
    ideal_shorting_profit = b_star - ideal_b_prime
    ideal_expenses = beta_asset.val * ideal_b + q.val * ideal_b / fi.val
    max_b = u / ((1 / fi.val + beta_asset.val) * gama_stasset.val)

    l.set_ydata(shorting_profit)
    r.set_ydata(expenses)
    w.set_ydata(shorting_profit - expenses)
    bp.set_ydata(ideal_shorting_profit - ideal_expenses)
    pr.set_ydata(ideal_b)
    max_b_plot.set_ydata(max_b)
    fig.canvas.draw_idle()

update()

beta_asset.on_changed(update)
f.on_changed(update)
b_0.on_changed(update)
s_0.on_changed(update)
gama_stasset.on_changed(update)
p.on_changed(update)
q.on_changed(update)
fi.on_changed(update)
b.on_changed(update)

plt.show()
