def calculer_vitesse(temps_seconde, distance_metre):
    vitesse_kmh = 3600 * distance_metre / temps_seconde
    return vitesse_kmh

print(calculer_vitesse(10, 100))