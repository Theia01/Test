import operator

listeMotCourant = ['le','la','les','l','du','de','des','d','ce','cet','ces','cette','c','un','une','uns','unes','au','aux','à','il','elle','ils','elles','on','tu','je','j','me','te','se','nous','vous','leur','leurs']
chaine = "Les deux hommes entourent David et le conduisent à la voiture, un Espace, garé devant sa maison. Il se dit que ce serait bien si sa voisine pouvait le voir comme ça, entouré de deux gardes du corps. Ça fait ‘pro’. Et comme tous les matins, sa voisine Florence le regarde partir, mais cette fois-ci entouré de deux gros gars baraqués, rasés au plus près, menton et crâne. Un peu plus les pieds sur terre défense, il deux n’avait pas su résister. Non pas que c’était passionnant, deux mais au moins, il ne faisait deux"
chaine = chaine.lower()

list_sc = [",",".","-","?","'","[","]","(",")","{","}",";"]
chaine = ''.join([i if i not in list_sc else ' ' for i in chaine ])
chaine_list  = chaine.split()

i = 0

for mot in listeMotCourant:
    for mot2 in chaine_list:
        if(mot2 == mot):
            del chaine_list[i]
        i+=1
    i=0

dico = {}
i = 0
nombre = 1

for item in chaine_list:
    if (item in dico):
        dico[item] += 1
    else:
        dico[item] = nombre
    i+=1

dicoTrier = sorted(dico.items(), reverse=True, key=operator.itemgetter(1))
for element in dicoTrier:
    print (element)


