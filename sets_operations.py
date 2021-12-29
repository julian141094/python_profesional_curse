"""
  Los sets es un tipo de dato inmutable que se
  representa de forma desordenada. No contiene datos repetidos
  ya que limpia lo que se le ingrese automaticamente.

  Poseen metodos pre definidos para trabjarlos como:
    set1.union(set2)
    set1.symmetric_difference(set2)
    set1.difference(set2)
    set1.intersection(set2) 

  Pero pueden ser trabajados de forma nativa con los operadores:
    Union => |
    Iterseccion => &
    Diferencia => -
    Diferencia Simetrica => ^
"""

my_set1 = {3,4,5}
my_set2 = {5,6,7}

union = my_set1 | my_set2
# {3,4,5,6,7}

iterseccion = my_set1 & my_set2
# {5}

diferencia1 = my_set1 - my_set2
# {3,4}
diferencia2 = my_set2 - my_set1
# {6,7}

diferencia_simetrica = my_set1 ^ my_set2
# {3,4,6,7}