# Liste de mots initiale
liste_mots = ["chat", "chien", "lapin", "oiseau", "éléphant", "tigre"]

# 1. Filtrer les mots qui contiennent la lettre "a"
resultat_1 = [mot for mot in liste_mots if 'a' in mot]

# 2. Filtrer les mots qui ont une longueur supérieure à 3 et transformer chaque mot en son inverse
resultat_2 = [mot[::-1] for mot in liste_mots if len(mot) > 3]

# 3. Filtrer les chaînes qui contiennent la lettre "e" et aplatir chaque chaîne en une liste de ses caractères
resultat_3 = [list(mot) for mot in liste_mots if 'e' in mot]

# 4. Transformer chaque chaîne en sa version en majuscules
resultat_4 = [mot.upper() for mot in liste_mots]

# 5. Convertir chaque chaîne en sa longueur
resultat_5 = [len(mot) for mot in liste_mots]

# 6. Transformer chaque chaîne en une liste de ses caractères, puis aplatir toutes les listes en une seule liste de caractères
resultat_6 = [caractere for mot in liste_mots for caractere in mot]

# 7. À partir d'une liste de mots, transformer chaque nom en une chaîne de la forme "Nom - Index"
resultat_7 = [f"{mot} - {index}" for index, mot in enumerate(liste_mots)]

# Affichage des résultats
print("1.", resultat_1)
print("2.", resultat_2)
print("3.", resultat_3)
print("4.", resultat_4)
print("5.", resultat_5)
print("6.", resultat_6)
print("7.", resultat_7)
