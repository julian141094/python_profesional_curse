def with_custom_message(message):
  """
    Para recibir un argumento en un decorador se tiene que anidar una 
    función más para que esta reciba los parámetros del decorador y 
    la siguiente es la que recibe la función a la que decora.
  """
  def with_message(function):
    print(f'{message}: ')
    def wrapper(*args, **kwargs):
      function(*args, **kwargs)
    return wrapper
  return with_message

@with_custom_message('Hello')
def multiply(a: int, b: int) -> int:
  c = a * b
  print(f'The resul of {a} * {b} is {c}')

multiply(10, 2)