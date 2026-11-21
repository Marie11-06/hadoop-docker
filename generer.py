import random

mots = ["bonjour", "hadoop", "kali", "docker", "mapreduce", "hdfs",
        "yarn", "reseau", "securite", "python", "linux", "serveur",
        "donnees", "cluster", "fichier", "calcul", "stockage", "cyber"]

taille_voulue = 36 * 1024 * 1024
taille_actuelle = 0

with open("mots.txt", "w") as fichier:
    while taille_actuelle < taille_voulue:
        ligne = " ".join(random.choice(mots) for i in range(10)) + "\n"
        fichier.write(ligne)
        taille_actuelle += len(ligne)
