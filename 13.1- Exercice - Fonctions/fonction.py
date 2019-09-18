# Problème : Créer une fonction affichant la fréquence des lettres d'une chaine de caractère.
# Données : Un texte d'essai et un tableau de caractère et leur fréquences.
texte = "ceci est un texte que vous pouvez modifier mais gare aux caracteres speciaux et aux majuscules"
tab_lettres = [
    ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w',
     'x', 'y', 'z', ' '], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
def afficherFrequenceLettre(texte,tab):
    for j in tab[0]:
        tab[1][tab[0].index(j)] =  texte.count(j)
    return tab


print(afficherFrequenceLettre(texte,tab_lettres))
