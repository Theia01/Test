fichier = "roles.txt"
with open(fichier,'r',encoding='utf-8') as f:
    liste_users = f.readlines()
 
for user in liste_users:
#On supprime le saut de ligne sauf pour la dernière
    if liste_users.index(user) != len(liste_users)-1:
        user = user[:-1]
        user = user.split(";")
        print("Prénom :",user[0],", Nom :",user[1])
        login = user[0][0].lower() + user[1].lower()
        print("Login :",login)
        print("Rôle :",user[2],"\n")