def polinomio_legendre(n, x):
    if n == 0: 
        return 1 
    elif n == 1:
        return x
    else:
        return ((2 * n - 1) * x * polinomio_legendre(n - 1, x) - (n - 1) * polinomio_legendre(n - 2, x)) / n

for (j, i) in enumerate(n):
    plt.plot(x, legendre[j], label=f'P{i - 1}(x)') #Graficamos los polinomios de Legrenge