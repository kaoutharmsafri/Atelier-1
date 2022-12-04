#Exercice 2 : Ecrire une fonction python qui calcul la factorielle d’un nombre donné
a=int(input("Entrer un nombre: "))
def factorielle (a):
    j=1
    for i in range (1,a+1):
        j=i*j
    return j           
print('le factoriel du nombre %d est: '%a,factorielle(a))