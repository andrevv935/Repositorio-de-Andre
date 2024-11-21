import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as spi

def interpolacion_cubica(x_data, y_data, x_vals):
    s = spi.CubicSpline(x_data, y_data)

    fig, ax = plt.subplots(1, 1)
    arr = np.arange(np.amin(x_data), np.amax(x_data), x_vals[1] - x_vals[0]) # Valores para graficar la curva
    ax.plot(arr, s(arr), color="lightgray", label="Interpolación cúbica", linewidth=5)
    ax.plot(x_data, y_data, markerfacecolor="blue", marker='o', linestyle="None", label='Datos')

    npow = np.array([[3], [2], [1], [0]])
    for i in range(x_data.shape[0] - 1):
        w = 3 if i == 0 else 1 # Grosor de la línea
        x = np.arange(x_data[i] - 1.5, x_data[i + 1] + 1.5, x_vals[1] - x_vals[0]) # Valores para graficar el segmento
        xaux = x - x_data[i] 
        if False:
            exp_x = [xaux] ** npow 
            y = s.c[:, 1].dot(exp_x) 
        else:
            y = xaux ** 3 * s.c[0, i] + xaux ** 2 * s.c[1, i] + xaux * s.c[2, i] + s.c[3, i]
        ax.plot(x, y, label="segmento {}".format(i), ls="--", lw=w)

    ax.legend()
    plt.show()
        
#Datos:
x_data = np.array([0, 1, 2, 3, 4, 5])
y_data = np.array([0.5, 0.8, 1.0, 0.9, 1.2, 0.7])
#Valores para graficar la curva:
x_vals = np.linspace(0, 5, 100)