
# static typing (variable_name : variable_type) -> (function return ) variable_type
def is_palindrome(string : str) -> bool : 
  string = string.replace(' ', '').lower()
  #  check if string reverse are equal to string
  return string == string[::-1]

def run():
  print(is_palindrome(1000))


#Entry point
if __name__ == '__main__':
  run()