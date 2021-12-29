"""
  Los generadores son funciones que ofrecen el camino para trabajar con sucesiones
  o iteraciones infinitas, dado que provee la formula para
  obtener el numero siguiente. Son similares a los iteradores pero realizados bajo
  funciones y no el paradigma de clases, lo que lo hace mas ligero de entender.
"""

import time

def fibo_gen():
  n1, n2 = 0, 1
  counter = 0
  while True:
    if counter == 0:
      counter += 1
      yield n1
    elif counter == 1:
      counter += 1
      yield n2
    else:
      aux = n1 + n2
      n1, n2 = n2, aux
      counter +=1
      yield aux

if __name__ == '__main__':
  fibonacci = fibo_gen()
  for element in fibonacci:
    print(element)
    time.sleep(0.05)