def est_ip_valide(ip,masque):
    liste_ip_utilisateur = ip.split(".")
    if len(liste_ip_utilisateur) !=4 :
        return False

    i=0
    while i !=4 :
        if liste_ip_utilisateur[i].isdigit()==True :
            liste_ip_utilisateur[i]=int(liste_ip_utilisateur[i])
        else:

            return False
        if 0<=liste_ip_utilisateur[i]<=255:
            resultat = True
        else:
            return False
        i=i+1

    if liste_ip_utilisateur[0]==0:
        if liste_ip_utilisateur[1]==0 and liste_ip_utilisateur[2]==0 and liste_ip_utilisateur[3]==0:
            return True
        else:
            return False

    masque = int(masque)
    if 0<=masque<=32:
        resultat = True
    else:
        return False

    return (resultat)