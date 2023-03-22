from sympy import Symbol, solve, sqrt, pretty

w = Symbol('w', positive=True, real=True)

q = Symbol('q', positive=True, real=True)
φ = Symbol('φ', positive=True, real=True)

u = Symbol('u', positive=True, real=True)
p = Symbol('p', positive=True, real=True)
b0 = Symbol('b0', positive=True, real=True)
b = Symbol('b', positive=True, real=True)

b_star = u

alpha_with_b = u * p * (b / (b0 + b)) - w * b

# w = q/φ
g = u * p * b0

b_expression = sqrt(g / w) - b0
b_expression = max(b_expression.subs(u, 1000).subs(b0, 10000).subs(p, 1).subs(w, 0.05).evalf(), 0)
print(b_expression)
alpha = alpha_with_b.subs(b, b_expression)

print(alpha)

#print(solve(alpha, w))