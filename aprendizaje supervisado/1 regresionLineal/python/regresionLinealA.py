import pandas as pd
import  numpy as np
import matplotlib.pyplot as plt
from regresionLineal import regLin

# anlisis y lectura de datos

datos = pd.read_csv ('dataset.csv', sep= ",", skiprows = 32, usecols = [2,3])
print(datos)

#graficar datos... buscar distribucion lineal
datos.plot.scatter(x='Age', y='Systolic blood pressure')
plt.xlabel('Edad (años)'); plt.ylabel('Presión sistólica (mm de Mercurio)')
plt.show()

#tomar las columnas y almacenarlas en las variables x y y
x = datos['Age'].values
y = datos['Systolic blood pressure'].values



runner = regLin() #constructor


# aprender los coeficientes w y b por medio del gradiente descendiente

# Inicializar "w" y "b" aleatoriamente, definir alpha y número de iteraciones.
# En este caso se debe definir una tasa de aprendizaje muy pequeña (w=0.0004) para
# garantizar la convergencia del algoritmo

np.random.seed(2)           # al replicar requiere mismo num de iteraciones
w = np.random.randn(1)[0]   # valores aleaatorios de w y b
b = np.random.randn(1)[0]

alpha = 0.0004
nits = 40000                # num de iteraciones

# Entrenamiento
error = np.zeros((nits,1))  # en esta se almacena valor del error
for i in range(nits):
    # Actualizar valor de los pesos usando el gradiente descendente
    [w, b] = runner.gradDesc(w,b,alpha,x,y)

    # Calcular el valor de la predicción
    y_ = runner.calculoModelo(w,b,x)

    # Actualizar el valor del error
    error[i] = runner.calculoError(y,y_)

    # Imprimir resultados cada 1000 epochs o iteraciones
    if (i+1)%1000 == 0:
        print("Epoch {}".format(i+1))
        print("    w: {:.1f}".format(w), " b: {:.1f}".format(b))
        print("    error: {}".format(error[i]))
        print("=======================================")

# Gráfica de ECM vs iteraciones y de la regresión lineal resultante
plt.subplot(1,2,1)
plt.plot(range(nits),error)
plt.xlabel('epoch')
plt.ylabel('ECM')

y_regr = runner.calculoModelo(w,b,x)
plt.subplot(1,2,2)
plt.scatter(x,y)
plt.plot(x,y_regr,'r')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# Predicción
edad = 90
presion = runner.calculoModelo(w,b,edad)
print("A los {}".format(edad), " años se tendrá una presión sanguínea de {:.1f}".format(presion))
