def even(a):
 if(a%2==0):
   return True
 else:
  return False
def square(a):
  return (a*a)
if __name__ == "__main__":
  x = int(input("Enter the number"))
  print("Is it Even number : ", even(x))
  print("The square of X is : ",square(x))