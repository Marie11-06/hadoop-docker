import sys

ville_actuelle = None
total = 0.0

for ligne in sys.stdin:
    ville, montant = ligne.strip().split("\t")
    if ville != ville_actuelle:
        if ville_actuelle is not None:
            print(ville_actuelle + "\t" + str(round(total, 2)))
        ville_actuelle = ville
        total = 0.0
    total += float(montant)

if ville_actuelle is not None:
    print(ville_actuelle + "\t" + str(round(total, 2)))
