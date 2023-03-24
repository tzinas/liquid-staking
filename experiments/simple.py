from sympy import Symbol, solve, sqrt, pretty

w = Symbol('w', positive=True, real=True)

q = Symbol('q', positive=True, real=True)
φ = Symbol('φ', positive=True, real=True)

u = Symbol('u', positive=True, real=True)
p = Symbol('p', positive=True, real=True)
b0 = Symbol('b0', positive=True, real=True)
b = Symbol('b', positive=True, real=True)

#b_star = u

# w = q/φ
g = u * p * b0

alpha_with_b = u * p * (b / (b0 + b)) - w * b

max_b = u / w # 1/w = φ/q >= φ, so max_b = u/w >= uφ

b_expression = sqrt(g / w) - b0
#b_expression = max(b_expression.subs(u, 1000).subs(b0, 10000).subs(p, 1).subs(w, 0.05).evalf(), 0)
alpha = alpha_with_b.subs(b, b_expression)

#print(solve(alpha, w))