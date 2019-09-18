# Problème : Etant donné un tableau, afficher l'indice du tableau comportant la valeur la plus elevée.
# Résultat attendu : Un affichage comme ceci : "La valeur maximum est :  x  et elle se trouve à l'indice [ n ][ m ]

tab = [[4, 7, 3, 20, 42], [2, 4, 5, 7, 2], [23, 24, 15, 75, 23]]


maxi = tab[0][0]
indiceMax1 = 0
indiceMax2 = 0
for i in range (len(tab)):
    for j in range(len(tab)):
        if tab[i][j] >= maxi:
            maxi = tab[i][j]
            indiceMax1 = i
            indiceMax2 = j
print("la valeur maximum est : ", maxi, " et elle se trouve à l'indice ", indiceMax1, " ", indiceMax2)


