# Eliminar repetidos sencillo
# [1, 1, 2, 2, 4] -> [1, 2, 4]

def remove_duplicates(some_list): 
  return list(set(some_list))
  
def run():
  print(remove_duplicates([1, 1, 2, 2, 3, 4]))

if __name__ == '__main__':
  run()