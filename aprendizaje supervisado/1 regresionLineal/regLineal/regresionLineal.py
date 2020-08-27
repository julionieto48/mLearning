import pandas as pd
import numpy as np
import matplotlib as plt



# lectura de datos
datos = pd.read_csv('datosRegLinealUno.csv')
print(datos)

x = datos [:,0] ; y = datos [:,1]

class RegLinUno:

    def __init__(self,x,y):
        self.x = x
        self.y  = y
        n = len(x)  # cantidad de datos
        xSum = self.suma(x) ; ySum =self.suma(y)
        xySum = self.columnaXy(x , y, n)
        xCuadrado , sumXCuadrado =  self.columnaCuadrado( x , n)

        xMedia = self.media(xSum,n) ; yMedia = self.media(ySum,n)

        num = xySum * n - ( xSum + ySum ) ; den =  n * sumXCuadrado  - ( xSum ** 2 )
        m = num / den
        b = yMedia - ( m * xMedia)

        #graficar
        x1 = np.linspace(min(x) - 1, max(x) + 1)
        linea = m * x1 + b
        plt.plot(x1, linea); plt.scatter(x, y)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid(True)
        plt.show()


    def suma(self,columna):
        columnSum = 0
        for i in range(0, len(columna - 1) , 1  ):
            columnSum =  columnSum + columna[i]
        return columnSum

    def columnaXy(self,columnaX , columnaY,n):
        xy = [] ; sumXy = 0 ;
        for i in range(0 , n ):
            xy[i] = columnaX[i] * columnaY[i]
            # xy.append( columnaX[i] * columnaY[i] )
            sumXy = sumXy + xy[i]
        return sumXy

    def columnaCuadrado(self, columnaX , n):
        sumXCuadrado = 0 ; xCuadrado = []
        for i in range(0 , n ):
            xCuadrado[i] = columnaX[i] ** (2)
            # xCuadrado[i] = x[i] ** (2)
            sumXCuadrado = sumXCuadrado + xCuadrado[i]
        return xCuadrado , sumXCuadrado

    def media(self, sumatoria , numElementos):
        laMedia = sumatoria / numElementos
        return laMedia
    # def graficar():
    #     # graficar
    #     x1 = np.linspace(min(x) - 1, max(x) + 1)
    #     linea = m * x1 + b
    #     plt.plot(x1, linea);
    #     plt.xlabel('x');
    #     plt.ylabel('y');
    #     plt.grid(True);
    #     plt.scatter(x, y)
    #     plt.show()











runner = RegLinUno(x , y)
# runner.graficar()



# ____________________//______________________________________________________//____________________
# referencia
# https://www.shanelynn.ie/python-pandas-read_csv-load-data-from-csv-files/
# https://www.datacamp.com/community/tutorials/pandas-read-csv

# https://stackoverflow.com/questions/903853/how-do-you-extract-a-column-from-a-multi-dimensional-array
# https://www.geeksforgeeks.org/append-extend-python/
# https://matplotlib.org/tutorials/introductory/pyplot.html