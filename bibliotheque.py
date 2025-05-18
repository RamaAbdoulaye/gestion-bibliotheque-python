""" Un module pour gerer les fonctions de la bibliotheque"""
import json


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


def afficher_tous_les_livres():
    """Fonction pour afficher tous les livres prsents dans la bibliotheques"""
    # Ouvrier et lire le fichier JSON
    with open("bibliotheque.json", "r", encoding="utf-8") as f:
        bibliotheque = json.load(f)
        # Afficher les informations du livre
    for livre in bibliotheque['livres']:
        print(f"ID: {livre['ID']}")
        print(f"Titre: {livre['Titre']}")
        print(f"Auteur: {livre['Auteur']}")
        print(f"Annee: {livre['Annee']}")
        print(f"Lu: {livre['Lu']}")
        print(f"Note: {livre['Note']}")
        print()


# ----- Appel de fonction -----
afficher_menu()
afficher_tous_les_livres()
