import  numpy as np


class regLin():

    def calculoModelo(self, w, b, x):
        # calculo de valor de una funcion lineal simple
        return w * x + b

    def calculoError(self, y, y_):
        # error cuadratico medio
        N = y.shape[0]  # total de los datos
        error = np.sum((y - y_) ** 2) / N
        return error

    def gradDesc(self, w_, b_, alpha, x, y):
        N = x.shape[0]  # total datos

        # Gradientes: derivadas de la función de error con respecto
        # a los parámetros "w" y "b" ... es la derivada d ela funcion que se desea minimizar osea la funcion de error
        dw = -(2 / N) * np.sum(x * (y - (w_ * x + b_)))
        db = -(2 / N) * np.sum(y - (w_ * x + b_))

        #actualizacion de datos en gradiente descendiente
        w = w_ - alpha * dw
        b = b_ - alpha * db

        return w, b