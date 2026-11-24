# Projet POO - Jeu de course 2D

## Description

Ce projet consiste à créer un jeu de course de voitures en 2D avec Python et Pygame.

Le jeu est inspiré de Mario Kart et Trackmania. Deux joueurs pourront jouer sur le même clavier.

Le programme est organisé avec une architecture MVC (Modèle, Vue, Contrôleur).

## Installation

Pour utiliser le projet, il faut avoir Python 3.12 installé.

1. Télécharger le projet depuis GitHub et ouvrir le dossier avec VS Code.

2. Créer un environnement virtuel :

```powershell
py -3.12 -m venv .venv
```

3. Installer les bibliothèques nécessaires :

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

4. Lancer le jeu :

```powershell
.\.venv\Scripts\python.exe main.py
```

## Organisation des fichiers

- `model/` : contient les classes liées aux voitures, aux circuits et au fonctionnement du jeu.
- `view/` : gère l'affichage du jeu.
- `controller/` : gère les commandes du clavier.
- `main.py` : permet de lancer le jeu.
- `constants.py` : contient les constantes du programme.
- `requirements.txt` : contient les bibliothèques nécessaires.
- `.gitignore` : permet d'ignorer certains fichiers sur Git.

## Utilisation de l'IA

XXXXXXXXXX (a compeleter a la fin )