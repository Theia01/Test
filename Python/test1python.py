#afficher le nom de la personne
nom = input("Entrez votre nom : ")
afficher = ("Boujour " + nom)

age =input("Quel est votre age ? ")

while (age.isnumeric() == 0):
    age = input("Quel est votre age ? ")

age = int(age)

print(afficher)
if(0<age<18):
    print("Vous êtes mineur!")
elif(age<0):
    print("Vous n'existez pas!")
elif(age>120):
    print("Vous n'êtes pas humain!")
else:
    print("Vous êtes majeur!")

list=[nom, age, "humain"]
print(list[1:])

pharse2 = "Bonjour, comment allez vous?"
pharse2 = pharse2.replace("?","")
pharse3 = pharse2.split(" ")

pharse3 = pharse3.append("Hola")
pharse3 = pharse3.insert( "KIL", 3 )

print(pharse3)
print(len(pharse3))