#liste le ontenu d'un dossier
# os.listdir("C:\\Windows")

#os.path.isfile(chemin)
#______isdir_________
#os.path.getsize(CHEMINCOMPLET)

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

demande_utilisateur_chemin = input("Entrez le chemin (complet) vers un dossier : ")
while (os.path.isdir(demande_utilisateur_chemin) == False):
        demande_utilisateur_chemin = input("Entrez le chemin (complet) vers un dossier : ")

def nbFichier(chemin):
        nombrebFichier = 0
        for fichiers in os.listdir(chemin):
                if os.path.isfile(chemin + "\\" +fichiers) == True:
                        nombrebFichier +=1
                else:
                        nombrebFichier += nbFichier(chemin + "\\" +fichiers)
        return nombrebFichier
        
def nbDossier(chemin):
        nombreDossier = 0
        for fichiers in os.listdir(chemin):
                if os.path.isfile(chemin + "\\" +fichiers) == True:
                        pass
                else:
                        nombreDossier += nbDossier(chemin + "\\" +fichiers)
                        nombreDossier +=1
        return nombreDossier

def tailleFichier(chemin):
        total = 0
        for fichiers in os.listdir(chemin):
                if os.path.isfile(chemin + "\\" +fichiers) == True:
                        print(str(os.path.getsize(chemin + "\\" +fichiers)) + " octets - " + fichiers)
                        total += os.path.getsize(chemin + "\\" + fichiers)
                else:
                        total += tailleFichier(chemin + "\\" +fichiers)
        return total

print(tailleFichier(demande_utilisateur_chemin))
print("Il y a "+ str(nbFichier(demande_utilisateur_chemin)) +" fichiers")
print("Il y a "+ str(nbDossier(demande_utilisateur_chemin)) +" dossiers")






