# Problème : Calculer le prix TTC d'une nombre d'articles ayant un prix unitaire donné. Avec une T.V.A à 7.7%.
# Données : Nombres d'articles et prix unitaire HT
# Résultat attendu : Un message "Le prix TTC est de XXX.XXX chf." Utilisez la fonction print().

nb_articles = 13
prix_ht = 42.75

somme = nb_articles * prix_ht
tva = somme * 0.077
sommeTva = somme + tva

print("Le prix TTC est de ",sommeTva, " chf.")

