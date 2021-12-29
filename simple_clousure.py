# Define a function that serve a function of higher order
def main():
  a = 1

  # Define a normal function, that remember the variable of higher order function
  def nested():
    print(a) 

  return nested 

# Excecute a main function, and save on my_func nested function
my_func = main()
my_func()

# Test delete a main excecution, to know if my_func save a value of the higher order function
del(main)

my_func()
#return a value

"""
we have 3 rules to know if a script have a clousure, they are :

1 - have a nested function
2 - the nested function must refer to a value of the higher order function
3 - the higher order function must return the nested function 
"""