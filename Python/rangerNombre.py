print("Nous allons ranger 5 nombres pour vous")
nombre1 = int(input("Entrez votre premier nombre: "))
nombre2 = int(input("Entrez votre deuxième nombre: "))
nombre3 = int(input("Entrez votre troisième nombre: "))
nombre4 = int(input("Entrez votre quatrième nombre: "))
nombre5 = int(input("Entrez votre cinquième nombre: "))

list = sorted([nombre1, nombre2, nombre3, nombre4, nombre5])

print(list[4])