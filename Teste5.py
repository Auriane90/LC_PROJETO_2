from pysat.formula import CNF
from pysat.solvers import Glucose3
# create a satisfiable CNF formula "(-x1 ∨ x2) ∧ (-x1 ∨ -x2)":
cnf = CNF(from_clauses=[[-1, -2, -3], [-1, 2, -3], [-1, -2, 3]])
cn = Glucose3()

cn.append_formula(cnf.clauses)
cn.solve()

print(cn.get_model())


