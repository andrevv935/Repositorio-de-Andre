import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import sympy as sym

#Funcion para realizar el polinomio de minimos cuadrados
def minimos_cuadrados(x_data, y_data):
    #Calculamos la media de X y Y
    xm = np.mean(x_data)
    ym = np.mean(y_data)
    n = len(x_data)

    #Realizamos la sumatoria de los datos
    sumaX = np.sum(x_data)
    sumaY = np.sum(y_data)
    sumaXY = np.sum(x_data * y_data)
    sumaX2 = np.sum(x_data ** 2)
    sumaY2 = np.sum(y_data ** 2)

    #Calculamos los coeficientes
    b1 = (n*sumaXY - sumaX*sumaY)/(n*sumaX2 - sumaX**2)
    b0 = ym - b1*xm

    #Calculamos la funcion f
    x = sym.Symbol("x")
    f = b0 + b1 * x

    #Calculamos los valores de f
    fx = sym.lambdify(x, f)
    fi = fx(x_data)

    #Calculamos el coeficiente de correlacion
    numerador1 = (n * sumaXY) - (sumaX * sumaY)
    denominador1 = (np.sqrt(n*sumaX2 - (sumaX)**2))*(np.sqrt(n*sumaY2 - (sumaY)**2))
    r = numerador1/denominador1

    #Calculamos los coeficientes de determinacion
    r2 = r**2
    r2_porcentual = np.round(r2*100, 2)

    print(f"Las medias son: Para X = {xm}. Para Y = {ym}")
    print(f"Los coeficientes son: De correlacion = {r}. De determinacion = {r2}")
    print(f"El {r2_porcentual}% de los datos estan descritos en el modelo lineal")

    return fi, f

#Datos:
x_data = np.array([0, 1, 2, 3, 4])
y_data = np.array([1.1, 3.5, 2.8, 4.2, 5.0])
#Valores para graficar la curva ajustada:
x_vals = np.linspace(0, 4, 100)

mostrar_grafica(x_data, y_data, *minimos_cuadrados(x_data, y_data))