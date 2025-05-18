""" Un module pour gerer les fonctions de la bibliotheque"""

from helpers.utils import generer_id_unique


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
    print("Ajout d'un nouveau livre")

    # Demander les informations à l'utilisateur
    titre = input("Titre du livre : ")
    auteur = input("Auteur du livre : ")
    try:
        annee = int(input("Année de publication : "))
    except ValueError:
        print("Année invalide. Livre non ajouté.")
        return

    nouvel_id = generer_id_unique(bibliotheque)

    nouveau_livre = {
        "ID": nouvel_id,
        "Titre": titre,
        "Auteur": auteur,
        "Annee": annee,
        "Lu": False,
        "Note": None
    }
    # Ajouter et sauvegarder
    bibliotheque["livres"].append(nouveau_livre)
    print(f" Livre « {titre} » ajouté avec succès.")


def supprimer_livre(bibliotheque):
    """Supprime un livre par ID avec confirmation de l'utilisateur"""
    try:
        livre_id = int(input("Entrez l'identifiant du livre à supprimer : "))
    except ValueError:
        print(" Identifiant invalide.")
        return

    for livre in bibliotheque["livres"]:
        if livre["ID"] == livre_id:
            print("\n Livre trouvé :")
            print(f"Titre : {livre['Titre']}")
            print(f"Auteur : {livre['Auteur']}")
            confirmation = input(
                "Voulez-vous vraiment supprimer ce livre ? (oui/non) : ").strip().lower()

            if confirmation == "oui":
                bibliotheque["livres"].remove(livre)
                print(" Livre supprimé avec succès.")
            else:
                print(" Suppression annulée.")
            return

    print("Aucun livre trouvé avec cet identifiant.")
