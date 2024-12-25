Chaine=str(input("Entrer une chaine de caractéres : "))
C=str(input("Entrer un caractére à chercher : "))
s=0
for i in Chaine :
    if(i==C) :
        s= s+1
print(s)
