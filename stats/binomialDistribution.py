from matplotlib import pyplot as plt
#from numpy import random
# import random
from random import random
lst = []
slots = 10
ensayos = 5

aciertos = []
perdidas = []


for i  in range(ensayos):
    for x in range(slots):
        lst.append(random())

        #mu = 0.9  # media
        #sigma = 80  # desviacion standard
        #X = random.normalvariate(mu, sigma)  #anadir una distribucion
        #lst.append(X)

        #x = random.binomial( n=1, p=0.5, size=slots)
        #lst.append(x)
        #print 'slot',x

    print lst, range(len(lst)), len(lst)

    acierto = 0 ; perdida = 0
    # print 'range(len(lst))' , range(0, len(lst)) no pueod usar este en el for pq va de 0 a 9 en indices x
    for x , y  in enumerate(lst,1):
        print y
        if y >= 0.5:
            # calificacion positiva
            acierto += 1
        elif y < 0.5:
            # calif negativa
            perdida += 1

        #print x
        if x % (slots + 1) == 0:  # ya que se usa enumerate se debe sumar + 1
            acierto = 0; perdida = 0  # reiniciar los contadores
            del lst[:]

    aciertos.append(acierto)
    perdidas.append(perdida)



print 'contadores ',aciertos,perdidas

#sacar las probabilidades
s = []* len(aciertos)

for j in range(0,len(aciertos)):
    x = round( float((aciertos[j])) / (slots - 1), 20)
    #print aciertos[j],slots - 1, x
    s.append(x)

print 's', s


# bases = []                     # primera solucion manejar bases
# for i in range(1, ensayos + 1):
#     bases.append( 10 * i )
#
# print 'bases' , bases
#
# s = []      pensaba usar bases cuando me daba  contadores  [0, 0, 1, 40, 0] [10, 20, 29, 0, 50] para depsues dividir y tener la probabil


fig, ax = plt.subplots(figsize=(10, 7))
plt.grid(True)
ax.hist(s , bins=[0, 0.1, 0.2, 0.3, 0.4,0.5, 0.6, 0.7, 0.8, 0.9,1])

# Show plot
plt.show()

# https://www.geeksforgeeks.org/plotting-histogram-in-python-using-matplotlib/
# https://numpy.org/doc/stable/reference/generated/numpy.histogram.html
# https://www.geeksforgeeks.org/random-seed-in-python/
# https://www.w3schools.com/python/numpy_random_binomial.asp
# https://www.arduino.cc/en/Tutorial/StateChangeDetection
# https://docs.python.org/3/library/random.html
# https://www.youtube.com/watch?v=iDgkSu5OorU
# https://www.geeksforgeeks.org/different-ways-to-clear-a-list-in-python/
# https://www.tutorialspoint.com/different-ways-to-clear-a-list-in-python


# random.binomial(n=slots, p=0.5, size=10) # n = numero intentos p = prob ocurrencia ej moneda 0.5 size = tamanoaray
