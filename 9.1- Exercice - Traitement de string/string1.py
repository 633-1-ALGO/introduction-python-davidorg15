# Consigne : Récupérer le mot "chaine" du string s et l'afficher
s = 'un exemple de chaine'
#sousChaine = s[14:20]
#print (sousChaine)
i = s.find('chaine')
sousChaine = s[i:]
print (sousChaine)
