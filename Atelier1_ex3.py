#Exercice 3: Ecrire une fonction en Python pour trouver la somme des séries 1! / 1 + 2! / 2 + 3! / 3 + 4! / 4 + 5! / 5 en utilisant la fonction.
a = int(input("Entrer un nombre: "))
def factorielle (a):
    j=1
    for i in range (1,a+1):
        j=i*j
    return j           
def somme_serie(a):
    j=0
    for i in range (1,a+1):
        j=(i-1)+factorielle(i)
        print('%d +%d!' %(i-1,i))
    j+=a
    print(a)
    return j
print('la somme de la série est : ',somme_serie(a))    