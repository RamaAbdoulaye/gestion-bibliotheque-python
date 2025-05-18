""" Un module pour gerer les fonctions de la bibliotheque"""


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


def afficher_tous_les_livres(bibliotheque):
    """Fonction pour afficher tous les livres presents dans la bibliotheque"""

    # Afficher les informations du livre
    for livre in bibliotheque['livres']:
        print(f"ID: {livre['ID']}")
        print(f"Titre: {livre['Titre']}")
        print(f"Auteur: {livre['Auteur']}")
        print(f"Annee: {livre['Annee']}")
        print(f"Lu: {livre['Lu']}")
        print(f"Note: {livre['Note']}")
        print()


def ajouter_livre(bibliotheque):
    """Fonction pour ajouter un livre à la bibliothèque"""
    # Demander les informations à l'utilisateur
    titre = input("Titre du livre : ")
    auteur = input("Auteur du livre : ")
    try:
        annee = int(input("Année de publication : "))
    except ValueError:
        print("Année invalide. Livre non ajouté.")
        return

    # Déterminer le prochain ID automatiquement
    if bibliotheque["livres"]:
        dernier_id = bibliotheque["livres"][-1]["ID"]
    else:
        dernier_id = 0

    nouveau_livre = {
        "ID": dernier_id + 1,
        "Titre": titre,
        "Auteur": auteur,
        "Annee": annee,
        "Lu": False,
        "Note": None
    }
    # Ajouter et sauvegarder
    bibliotheque["livres"].append(nouveau_livre)
    """ with open(chemin_fichier, "w", encoding="utf-8") as f:
        json.dump(bibliotheque, f, ensure_ascii=False, indent=4) """

    print(f" Livre « {titre} » ajouté avec succès.")
