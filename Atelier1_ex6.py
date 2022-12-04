#Exercice 6:Ecrire une fonction en Python pour compter les chiffres d'un nombre donné.
a=input("Entrer un nombre: ")
def chifffre(a):
    j=0
    for i in range (len(a)):
        j+=1
    return j
print('le chiffre du nombre ',a,' est:',chifffre(a))