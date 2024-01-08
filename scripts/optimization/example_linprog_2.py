#example_linprog_2.py
from scipy.optimize import linprog

c = [-40,-88]
A = [[2,8], [5,2]]
b = [60,60]
bounds = [(0, None), (0, None)]
res = linprog(c, A_ub=A, b_ub=b, bounds=bounds)

x = res.x
fun = res.fun
slack = res.slack
success = res.success

print(x,fun,slack,success)