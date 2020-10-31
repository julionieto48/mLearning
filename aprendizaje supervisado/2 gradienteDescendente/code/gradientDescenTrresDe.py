import numpy as np
import scipy as sc
import matplotlib.pyplot as plt

funcion = lambda th :   np.sin( 1/2 * th[0]**2  + 1/4 * th[1]**2 + 3) * np.cos(2*th[0] + 1 - np.e**th[1])    # declaracion de funcion anonima  th = vector de parametros, es la variable de entrada
                      # np.sin( 1/2 * x**2  + 1/4 * y**2 + 3) * np.cos(2*x + 1 - np.e**y) es funcion a optimizar
# print funcion([5,3])

resolucion = 100
x = np.linspace(-2,2 ,resolucion) ; y = np.linspace(-2,2 ,resolucion)     # se tiene un amatriz de 100 * de resolucion

z = np.zeros((resolucion,resolucion))

# asignar valores... evlauar funcion
for iX, X in enumerate(x) :
    for iY, Y in enumerate(y):
        z[iY , iX] = funcion([X,Y])        # filas = y, columnas
# enumerate recorre el elemento y retorna indice, valor el indice se guarda en ix y el valor se guarda en X

plt.contourf(x,y,z,100)                    # x y y son los linspaces
plt.colorbar()




# tecnica de optimizacion del gradiente decendente

punto = np.random.rand(2) * 4 - 2      # este es pto inicial  np.random.rand(2)   valores entre 0 y 1;  np.random.rand(2) * 4 - 2 vlaores entre -2 y 2 conocido como theta
plt.plot( punto[0], punto[1],"ro", C ="red" , label='inicio')


T = np.copy(punto)             # copia evlauada con el punto inicial

# derivadas parciales obtiene la derivada en cadae eje del vector de parametros

learningRate = 0.1               # pequeno = muchos pasos poca distancia
delta = 0.0001                    # delta = H
grad = np.zeros(2)

for _ in range(100):              # iteracion

    for iT, th in enumerate(punto):  # calculo por medio d eminimas diferencias

        T = np.copy(punto)     # se actualiza con el nuevo valor del punt
        T[iT] = T[iT] + delta  # el primer componente del punto  se le hace un pequeno incremento

        derivada = (funcion(T) - funcion(
            punto)) / delta  # derivada(es un ratio) es la funcion evlauada en el incremento respecto al punto inicial e analisis

        grad[iT] = derivada

    punto = punto - grad * learningRate  # el valor del punto es actualizado
    #print funcion(punto)

    # visualizar el recorrido del punto cada detemirnada iteraciones
    if _% 4 == 0 :
        plt.plot(punto[0], punto[1], ".", c ="green" )  # marca el camino recorrido

plt.plot(punto[0], punto[1], "o", c ="white", label='final')
plt.legend()
plt.show()

