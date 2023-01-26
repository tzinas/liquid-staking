from base import *

def hey():
  return replace_known_values(alpha.subs(f, 1))

#print(pretty(hey()))
#print(solve(hey(), w)[0])

al = alpha.subs(f, 1.000006).subs(u, (4985382/10)).subs(b0, 4985382).subs(β, 0.0005).subs(p, 0.5).subs(γ, 1.21)

print(solve(al, w))
print(al.subs(w, 1))

#print(b_expression.subs(f, 1.000006).subs(u, (4985382/10)).subs(b0, 4985382).subs(β, 0).subs(p, 0.5).subs(γ, 1.21).subs(w, 0.0210367676026939).evalf())
#aln = alpha_with_b.subs(b, 20000).subs(f, 1.000006).subs(u, (4985382/10)).subs(b0, 4985382).subs(β, 0.01).subs(p, 0.5).subs(γ, 1.21).subs(w, 0.0210367676026939).evalf()
#print(aln)
#print(al.subs(w, 20).evalf())
