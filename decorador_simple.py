def decorador(func):
  def envoltura():
    print('Esto se a#ade a mi funcion original')
    func()
  return envoltura

@decorador #Sintaxis de decorador especifica
def saludo():
  print('Hola!!!!')

#saludo = decorador(saludo) #Sintaxis de clousure normal
saludo()
# Escapa: 
# Esto se a#ade a mi funcion original
# Hola!!!

"""
  Basicamente es un decorador especial, hace uso de
  Azucar sintactica para que se vea mas sencilla y se 
  entienda mejor. Con el "@" y el nombre de la funcion
  decoradora.
"""