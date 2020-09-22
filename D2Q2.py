#Auteur : Anys Younes
#Numero d'étudiant : 300145843

print("Auteur : Anys Younes")
print("Numéro d'étudiant : 300145843")

#Question 2 Devoir 2
#Suite Fibonacci

number = int(input("Entrez le nombre de termes :"))
def fibonacci(n):
    x = 0
    y = 1
    while n<2 :
        n = int(input("Entrez le nombre de termes :"))
    else:
        for i in range(n):
            z = x + y
            print(x, end = " ")
            x = y
            y = z
            i = i + 1
fibonacci(number)
