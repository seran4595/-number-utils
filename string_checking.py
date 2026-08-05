def vowel(a):
    c=0
    for i in a:
        if(i=="a" or i=="i" or i=="e" or i=="o" or i=="u" or i=="A" or i=="I" or i=="E" or i=="O" or i=="u"):
            c+=1
    return c
def const(a):
    c=0
    for i in a:
        if(i!="a" or i!="i" or i!="e" or i!="o" or i!="u"):
            c+1
    return c
def uppercase(a):
    c=0
    for i in a:
        if(i=="A" or i=="B" or i=="C" or i=="D" or i=="E" or i=="F" or i=="G" or i=="H" or i=="J" or i=="K" or i=="L" or i=="M" or i=="N" or i=="O" or i=="P" or i=="Q" or i=="R" or i=="S" or i=="T" or i=="W" or i=="U" or i=="V" or i=="X" or i=="Y" or i=="Z"):
            c+=1
    return c

if __name__ == "__main__":
  x =input("Enter the string : ")
  print("number of vowels  : ", vowel(x))
  print("number of consonats : ",const(x))
  print("number of uperrcase : ",uppercase(x))
