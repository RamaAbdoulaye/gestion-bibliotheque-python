# Gestion Bibliothèque - Ramatoulaye Diallo

**Collège Boréal**  
**Année scolaire : 2024-2025**

Ce projet est une application Python simple pour gérer une bibliothèque personnelle.  
Vous pouvez afficher les livres, ajouter, supprimer, rechercher, marquer comme lu, filtrer et trier les livres.

---

## Fonctionnalités principales

- Afficher tous les livres
- Ajouter un livre
- Supprimer un livre par ID avec confirmation
- Rechercher un livre par mot-clé dans le titre ou l'auteur
- Marquer un livre comme lu, avec note et commentaire
- Afficher les livres lus ou non lus
- Trier les livres par année, auteur ou note

Autres 
- Afficher le menu principal 
- Charger les données de la bibliotheque depuis le fichier JSON
- Fonction pour sauvegarder les données dans le fichier JSON
- Génèrer un ID unique pour un nouveau livre

---

## Installation 

1. Clonez ce dépôt GitHub :

```bash
git clone https://github.com/RamaAbdoulaye/bibliotheque-rama-diallo.git
```

2. Placez-vous dans le dossier du projet : 
```bash
cd bibliotheque-rama-diallo
```
3. Lancez le programme principal :
```bash
python main.py
```
Le menu interactif vous guidera pour gérer votre bibliothèque.

## Organisation des fichiers
- **main.py** : point d'entrée du programme
- **bibliotheque.py** : fonctions liées à la gestion des livres
- **helpers/utility.py** : fonctions utilitaires (ex : génération d'identifiants uniques)
- **data/bibliotheque.json** : fichier JSON contenant les données des livres

## Lien vers le repository
https://github.com/RamaAbdoulaye/bibliotheque-rama-diallo.git

Auteur
Ramatoulaye Diallo, 
Collège Boréal — Année scolaire 2024-2025