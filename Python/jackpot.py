import random
nombre_jackpot = random.randint(1,1001)
nombre_choisi = ""

print("__________ZZZZZ______________ZZZZZZ")
print("________ZZZZZ____________________ZZZZ")
print("______ZZZZZ_______________________ZZZZZ")
print("____ZZZZZ___________________________ZZZZ")
print("___ZZZZ______________________________ZZZZ")
print("__ZZZ__________________________________ZZZ")
print("_ZZZ____________________________________ZZZ")
print("ZZZZ____________________________________ZZZ")
print("ZZZ_____________________________________ZZZ")
print("ZZZ_____________________________________ZZZ")
print("ZZZ_____________________________________ZZZ")
print("ZZZ_____________________________ZZ______ZZZ")
print("ZZZ___________________________ZZZZZ_____ZZZ")
print("ZZZ________________________ZZZZZZZZZ__ZZZZZ")
print("ZZZZ____ZZZ______________ZZZZZZZZZZZZ_ZZZZ")
print("ZZZZ___ZZZZZZ___________ZZZZZZZZZZZZZ_ZZZ")
print("ZZZZ__ZZZZZZZZZZ_______ZZZZZZZZZZZZZ__ZZ")
print("ZZZZ__ZZZZZZZZZZZ______ZZZZZZZZZZZZ___ZZ")
print("_ZZZ___ZZZZZZZZZZZ______ZZZZZZZZZZ____ZZ")
print("_ZZZ____ZZZZZZZZZ_ZZZZZ___ZZZZZZ____ZZZZ")
print("__ZZZ____ZZZZZZZ__ZZZZZZ___________ZZZZ")
print("___ZZZZZ__________Z__ZZZ_____ZZZZZZZZZ")
print("____ZZZZZZZZ__________ZZ____ZZZZZZZZ")
print("_____ZZZZZZZZ_____________ZZZZZ")
print("__________ZZZ__Z___Z___Z__ZZZ")
print("__________ZZZ_ZZZ_ZZZ_ZZZ_ZZZ")
print("__________ZZZ_ZZZ_ZZZ_ZZZ_ZZZ")
print("__________ZZZ_ZZZ_ZZZ_ZZZ_ZZZ")
print("___________ZZZZZZZZZZZZZZZZZ")
print("______________ZZZZZZZZZZZ")

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
   





