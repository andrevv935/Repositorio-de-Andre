import numpy as np

#Datos:
A = np.array([[1, 2, 1], [2, -1, 1], [3, 1, -1]])
b = np.array([4, 1, -2])
x = np.linalg.solve(A, b)

print(f"La solucion es: \nPara X = {x[0]} \nPara Y = {x[1]} \nPara Z = {x[2]}")