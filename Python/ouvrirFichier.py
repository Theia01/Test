texte ="listeMotEnlevermajuscule.py"
#texte="EnleverMotCourant.py"

with open(texte, 'r', encoding='utf-8') as f:
    #print(f.read()) #affiche en entier
    liste_ligne = f.readlines() #renvoie une liste contenant chaque ligne

for user in liste_ligne:
    if liste_ligne.index(user) != len(liste_ligne)-1:#si c'est pas la dernière ligne
        print(user[:-1]) #[:-1] permet d'éviter les saut de lignes 
    else: 
        print(user)


