"""
  Los iteradores son clases que ofrecen el camino para trabajar con sucesiones
  o iteraciones infinitas, dado que provee la formula para
  obtener el numero siguiente.

  La clase del iterador a crear, debe contar con 3 metodos
  basicos:
  * __init__ (el constructor, es opcional)
  * __iter__ (crear los valores necesarios para que el iterador trabaje)
  * __next__ (Realiza la operacion y retorna el numero que le sigue)
"""

import time

class FiboIter():

  #todos los metodos de una clase en python, requiere el objeto self 
  def __iter__(self):
    self.n1 = 0
    self.n2 = 1
    self.counter = 0
    return self

  def __next__(self):
    if self.counter == 0:
      self.counter += 1
      return self.n1
    elif self.counter == 1:
      self.counter += 1
      return self.n2
    else:
      self.aux = self.n1 + self.n2
      # se optimizan con el swaping de python
      #self.n1 = self.n2
      #self.n2 = self.aux
      self.n1, self.n2 = self.n2, self.aux
      self.counter += 1
      return self.aux

# Entry point
if __name__ == '__main__':
  fibonacci = FiboIter()
  for element in fibonacci:
    print(element)
    time.sleep(1)