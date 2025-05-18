
import json
import os

FICHIER_DATA = os.path.join("data", "bibliotheque.json")


def afficher_menu():
    """Fonction pour afficher le menu"""
    print("\t  - Gestion biblliotheque Ramatoulaye Diallo -")
    print("\t | 1. Afficher tous les livres                |")
    print("\t | 2. Ajouter un livre                        |")
    print("\t | 3. Supprimer un livre                      |")
    print("\t | 4. Rechercher un livre comme lu            |")
    print("\t | 5. Marquer un livre comme lu               |")
    print("\t | 6. Afficher livres lus non lus             |")
    print("\t | 7. Trier les livres                        |")
    print("\t | 8. Quitter                                 |")
    print("\t ---------------------------------------------")


def charger_bibliotheque():
    """Charge les données depuis le fichier JSON"""
    if os.path.exists(FICHIER_DATA):
        with open(FICHIER_DATA, "r", encoding="utf-8") as f:
            return json.load(f)
    return {"livres": []}


def sauvegarder_bibliotheque(bibliotheque):
    """Fonction pour sauvegarder les données dans le fichier JSON"""
    with open(FICHIER_DATA, "w", encoding="utf-8") as f:
        json.dump(bibliotheque, f, indent=4, ensure_ascii=False)
    print("Données sauvegardées avec succées.")


def generer_id_unique(bibliotheque):
    """
    Génère un ID unique pour un nouveau livre.
    Si la bibliothèque est vide, retourne 1.
    """
    livres = bibliotheque["livres"]

    if not livres:
        return 1

    max_id = 0
    for livre in livres:
        if livre["ID"] > max_id:
            max_id = livre["ID"]

    return max_id + 1
