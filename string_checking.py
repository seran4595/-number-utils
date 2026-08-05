def vowel(a):
    c=0
    for i in a:
        if(i=="a" or i=="i" or i=="e" or i=="o" or i=="u"):
            c+=1
    return c
def const(a):
    c=0
    for i in a:
        if(i!="a" or i!="i" or i!="e" or i!="o" or i!="u"):
            c+1
    return c
if __name__ == "__main__":
  x =input("Enter the string : ")
  print("number of vowels  : ", vowel(x))
  print("number of consonats : ",const(x))
