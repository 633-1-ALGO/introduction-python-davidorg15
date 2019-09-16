# Consigne : Rechercher le nombre d'occurences du mot "exemple" et l'afficher. Remplacer le mot "est" par "représente".
# Bonus : Inverser le sens de lecture.

#Compter nombre d'occurences du mot "exemple" et l'afficher.
texte = "Ceci est un exemple exemplaire d'exemple exempté d'exemple."
nbExemple = texte.count("exemple")
print("Le nombre est ",nbExemple)

#Remplacer le mot "est" par "représente".
texteRemplace = texte.replace('est','représente')
print(texteRemplace)

# Inverser le sens de lecture
texteInverse = ""
for lettre in reversed(texte):
    texteInverse +=lettre
print(texteInverse)
