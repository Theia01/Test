import random
nombre_jackpot = random.randint(1,1001)
nombre_choisi = ""

print("Bonjour et bienvenue pour notre grand jackpot! Ne perdons pas plus de temps!")


print("La roulette tourne! On vous donne 10 essais")

nombre_essai = 9

while nombre_essai>0 :

    nombre_choisi = input("Veuillez choisir un nombre :")

    while nombre_choisi.isnumeric() == 0:
        print("Ceci n'est pas un nombre valide!")
        nombre_choisi = input("Veuillez choisir un nombre :")
    nombre_choisi = int(nombre_choisi)


    if (nombre_choisi == nombre_jackpot):
        print("Nous avons un gagnant toute mes félicitaions!")
        exit()
    elif(nombre_choisi < nombre_jackpot):
        print("C'est plus")
        print("Vous avez encore " + str(nombre_essai) + " essai Allez courage!")
        print(" ")
    else:
        print("C'est moin")
        print("Vous avez encore " + str(nombre_essai) + " essai Allez courage!")
        print(" ")
    nombre_essai -= 1

if(nombre_essai == 0):
    print("Dommage vous restez dans la puvreté absolu le bon nombre était " + str(nombre_jackpot))
   





