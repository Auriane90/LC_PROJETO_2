from sympy.logic.inference import satisfiable
from sympy import Symbol
from sympy import *

x0 = Symbol('x0')
x1 = Symbol('x1')
x2 = Symbol('x2')
x3 = Symbol('x3')
x4 = Symbol('x4')
x5 = Symbol('x5')
x = Symbol('x')
y = Symbol('y')

sat = satisfiable((~x1 | ~x2 | ~x3) >> True
                  & (~x1 | x2 | ~x3) >> True
                  & (~x1 | ~x2 | x3) >> False)

print(sat)




