from datetime import datetime

#This decorator see the excecution time of any function 
def execution_time(func):
  """
    Para aceptar argumentos posicionales, se utiliza el operador
    de destructuracion de python "*".
    Con *args se le indica a python que la funcion se ejecuta sin
    tener en cuenta la cantidad de argumentos posicionales
    Con *kwargs se le indica a python que la funcion se ejecuta sin
    tener en cuanta la cantidad de argumentos nombrados

    De este modo, se ejecura el decorador sin importar la cantidad de
    parametros
  """
  def wrapper(*args, **kwargs):
    initial_time = datetime.now()
    func(*args, **kwargs)
    final_time = datetime.now()
    time_elapsed = final_time - initial_time
    print(" Han pasado " + str(time_elapsed.total_seconds()) + " segundos")

  return wrapper

@execution_time
def random_func():
  for _ in range(1, 100000000):
    pass

@execution_time
#argumentos posicionales
def suma(a: int, b: int) -> int:
  return a + b

@execution_time
#argumento nombrado
def saludo(nombre = 'Julian'):
  print('Hola ' + nombre)


suma(4, 5)
random_func()
saludo('Pedro')
 
