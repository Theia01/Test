chaine = "Bonjour et bienvenu! Comment allez vous?"
chaine = chaine.lower() 
chaine = chaine.replace("?", "")
chaine = chaine.replace("!", "")
chaine = chaine.split(" ")
print(chaine)