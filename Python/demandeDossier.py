#liste le ontenu d'un dossier
# os.listdir("C:\\Windows")

#os.path.isfile(chemin)
#______isdir_________
#os.paht.getsize(CHEMINCOMPLET)

#os    sys    shutil    subprocess

#Exercice 1 :
#A partir du CSV vu précédemment (prenom;nom;role), créer un dictionnaire au format suivant : {login1: rôle; login2: rôle}
#   Exemple : roles = {'lbertaux':'Formateur','cbeaudu':'Accueil'...}
#Exercice 2 :
#   Ecrire un programme qui :
#   demande à l'utilisateur de saisir un chemin (complet) vers un dossier
#   vérifie si ce dossier existe et redemande en boucle si ce n'est pas le cas
#   affiche :
#       le nombre de dossiers
#       le nombre de fichiers
#       la taille total du dossier
import os
dico_voisin = {"Margaux": "en face", "Eric": "A gauche", "Nathan": "A droite"}

demande_utilisateur_chemin = input("Entrez le chemin (complet) vers un dossier : ")
while (os.path.isdir(demande_utilisateur_chemin) == False):
        demande_utilisateur_chemin = input("Entrez le chemin (complet) vers un dossier : ")

for fichiers in os.listdir(demande_utilisateur_chemin):
    print(fichiers)

