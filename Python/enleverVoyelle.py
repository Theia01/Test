def supprimer_voyelles(phrase):
    phrase = phrase.lower()
    for lettre in phrase:
        if lettre in 'a':
            phrase = phrase.replace(lettre,'')
        if lettre in 'e':
            phrase = phrase.replace(lettre,'')
        if lettre in 'i':
            phrase = phrase.replace(lettre,'')
        if lettre in 'o':
            phrase = phrase.replace(lettre,'')
        if lettre in 'u':
            phrase = phrase.replace(lettre,'')
        if lettre in 'y':
            phrase = phrase.replace(lettre,'')
    return phrase

print(supprimer_voyelles("HOOOayo gisaimasu"))