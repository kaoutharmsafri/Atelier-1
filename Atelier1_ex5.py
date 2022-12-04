#Exercice 5:Ecrire une fonction en Python pour calculer la somme des nombres de 1 à n
a=int(input("Entrer un nombre: "))
def somme(a):
    j=0
    for i in range (a+1):
        j+=i
    return j
print('la somme des nombres de 1 à %d est: '%a,somme(a))