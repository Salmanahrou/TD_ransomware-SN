Ce projet a pour objectif de simuler le fonctionnement d'un ransomware et de son serveur de commande et contrôle (CNC). Il permet de comprendre comment un malware peut chiffrer des fichiers, envoyer les clés de chiffrement à un serveur distant, et potentiellement les déchiffrer en échange d'une rançon.

L'objectif pédagogique est d'explorer les techniques utilisées par les ransomwares, les faiblesses des algorithmes de chiffrement et les stratégies de protection contre ces attaques.
Dans ce projet, nous avons mis en place :

Dans ce Tp on mis en place:
Un ransomware qui chiffre les fichiers avec un algorithme XOR.
Un serveur CNC (Command & Control) qui stocke les clés de chiffrement envoyées par le ransomware.
Une infrastructure Dockerisée, permettant d’exécuter le projet dans un environnement isolé.


Fonctionnement du ransomware: Le ransomware effectue plusieurs étapes pour compromettre un système cible :
Il scanne les fichiers du répertoire pour identifier ceux à chiffrer.
Il génère une clé secrète à l’aide d’un algorithme cryptographique.
Il chiffre les fichiers en appliquant un XOR entre le contenu des fichiers et la clé générée.
Il envoie la clé au serveur CNC, afin que la victime ne puisse pas déchiffrer ses fichiers sans payer.
Il affiche un message demandant une rançon en échange de la clé de déchiffrement.

Pour exécuter ce projet, il faut suivre les étapes suivantes :
Cloner le projet
Construire l’image Docker
Lancer le serveur CNC
Exécuter le ransomware
Vérifier les fichiers chiffrés

En cybersécurité, il est essentiel de comprendre comment fonctionnent les menaces pour mieux s’en protéger. Ce projet nous a offert une approche pratique et technique d’un sujet d’actualité et critique dans le domaine de la sécurité informatique.