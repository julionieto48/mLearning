import sympy as sp
import matplotlib.pyplot as plt
from numpy import linspace
import numpy as np
from sympy import lambdify


p , y = sp.symbols('a y')


def gradDesc(xInicial, learningRate , numIter , funcion):
    fun = str(funcion)
    # almacenar valores en cada iteracion y ver le comportamiento
    iteraciones = []
    y = []

    x = xInicial

    for i in range(numIter):
        print('------------------------')
        print('iteracion ', str(i + 1))


        gradiente =  sp.diff( funcion  , p)       # Calculo de gradiente / derivada

        x = x - learningRate * gradiente            # Actualizar "x" usando gradiente descendente

        grad = str(gradiente)
        y.append( eval(grad) )               # almacenar valores correpsondientes de la evaluacion i de iteracion
        iteraciones.append(i + 1)

        # Imprimir resultados
        print('x = ', str(x), ', y = ', eval(fun))

    # grafica valores vs iteraciones
    plt.subplot(1, 2, 1)
    plt.plot(iteraciones, y)
    plt.xlabel('iteraciones')
    plt.ylabel('y')

    # valor de la funcion vs funcion para ver minimo

    #lam_x = lambdify((x,y), funcion, modules=['numpy'])
    X = np.array(linspace(-5, 5, 100 , endpoint=True))
    #Y = round(float (funcion.evalf() )) no funciono pq no es string usando eval f lo mismo en gradiente
    #Y = lam_x( X)
    #Y =   np.array(eval(fun) )  # conversion de lista array
    Y = X**2 + 5*X - 2

    plt.subplot(1, 2, 2)
    plt.plot(X, Y, 0.0, 0.0, 'ro')
    plt.xlabel('x')
    plt.ylabel('y')

    plt.show()


# Parametros iniciales

xInicial = 3                    # pto aleatoro
a  =  0.5                    # learning rate
nIter = 50                     # cantidad ieraciones
f = p**2 + 5*p - 2                  # se cambio p y x por lo que se estna usando elementos symbolicos ya que x significa el gradiente desc

gradDesc(xInicial, a, nIter, f)




# https://www.geeksforgeeks.org/eval-in-python/
# https://docs.sympy.org/latest/modules/evalf.html
# https://www.geeksforgeeks.org/python-sympy-evalf-method/
# https://stackoverflow.com/questions/17090073/sympy-function-evaluation