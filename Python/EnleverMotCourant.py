listeMotCourant = ['le','la','les','l','du','de','des','d','ce','cet','ces','cette','c','un','une','uns','unes','au','aux','à','il','elle','ils','elles','on','tu','je','j','me','te','se','nous','vous','leur','leurs']
chaine = "Il était une fois une elle princesse qui vivait dans la region du troll"
chaine_list  = chaine.split(" ")
i = 0

for mot in listeMotCourant:
    for mot2 in chaine_list:
        if(mot2 == mot):
            del chaine_list[i]
        i+=1
    i=0

print(chaine_list)

dico = {"var":1, "hoy":3}
#for mot in chaine:
#    if dico.has_key(mot) == True:
#        dico[mot] += 1
#    else:
#        dico[mot] = 1 


a = {"nom" : 1}
list = ["nom", "prenom", "manger"]
i = 0
for (mot, nombre) in a.items():
    for item in list:
        if (item == mot):
            a[mot] = nombre+1
            print("ok" + str(mot))
        else:
            print("fuck")
            a[mot] = 1


b = "mpm"
a[b] = 1
print (a)


