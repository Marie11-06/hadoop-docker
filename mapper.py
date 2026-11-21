import sys

for ligne in sys.stdin:
    champs = ligne.strip().split("\t")
    if len(champs) == 6:
        ville = champs[2]
        montant = champs[4]
        print(ville + "\t" + montant)
