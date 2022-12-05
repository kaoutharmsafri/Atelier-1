#Exercice 4:Ecrire une fonction en Python pour convertir le nombre décimal en nombre binaire.
List=[]
x=int(input("Entrer un nombre: "))
a=x
def binaire (x):
        while(x>0):
                i=0
                List.insert(i,x%2)
                x=x//2
                i+=1
        for i in range (len(List)):     
                print(List[i],end="")
        return List
print('le nombre binaire du nombre décimal %d est : '%a,end=" ")
binaire (x)
