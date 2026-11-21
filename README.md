# Hadoop sous Docker

Hadoop (HDFS + YARN) lancé avec Docker Compose, et un exercice de comptage de mots.

## Démarrer
    docker-compose up -d

## Générer un fichier de 36 Mo
    python3 generer.py

## Envoyer le fichier dans HDFS
    docker cp mots.txt hadoop-docker-namenode-1:/tmp/mots.txt
    docker-compose exec namenode hdfs dfs -mkdir -p /entree
    docker-compose exec namenode hdfs dfs -put -f /tmp/mots.txt /entree

## Compter les mots
    docker-compose exec namenode bash -c 'hadoop jar /opt/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-examples-*.jar wordcount /entree/mots.txt /sortie_mots'
    docker-compose exec namenode bash -c 'hdfs dfs -cat /sortie_mots/part-*'

## Interfaces web
- HDFS : http://localhost:9870
- YARN : http://localhost:8088
