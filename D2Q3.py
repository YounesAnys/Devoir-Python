#Auteur : Anys Younes
#Numero d'étudiant : 300145843

print("Auteur : Anys Younes")
print("Numéro d'étudiant : 300145843")

#Question 3 Devoir 2
#triangle isocèle

def triangle(hauteur):
    
    for i in range(hauteur+1):
        print(" " * (hauteur-i), "*" * (i*2 - 1), "\n" , end ="")
    hauteur = hauteur - 1
    return triangle
