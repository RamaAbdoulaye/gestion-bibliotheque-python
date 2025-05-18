""" Un module pour gerer les fonctions de la bibliotheque"""

from helpers.utils import generer_id_unique


def afficher_tous_les_livres(bibliotheque):
    """Fonction pour afficher tous les livres presents dans la bibliotheque"""
    if not bibliotheque["livres"]:
        print("Aucun livre dans la bibliothèque.")
        return

    # Afficher les informations du livre
    for livre in bibliotheque['livres']:
        print(f"ID: {livre['ID']}")
        print(f"Titre: {livre['Titre']}")
        print(f"Auteur: {livre['Auteur']}")
        print(f"Annee: {livre['Annee']}")
        print(f"Lu: {livre['Lu']}")
        print(f"Note: {livre['Note']}")

        commentaire = livre.get("Commentaire")
        if commentaire and commentaire.strip():
            print(f"Commentaire: {commentaire}")
        print("-" * 40)


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


def rechercher_livre_par_mot_cle(bibliotheque):
    """
    Recherche les livres contenant un mot-clé dans le titre 
    ou le nom de l'auteur.
    """
    mot_cle = input("Entrez un mot-clé pour la recherche : ").lower()
    resultats = []

    for livre in bibliotheque['livres']:
        titre = livre['Titre'].lower()
        auteur = livre['Auteur'].lower()
        if mot_cle in titre or mot_cle in auteur:
            resultats.append(livre)

    if resultats:
        print(f"\n {len(resultats)} livre(s) trouvé(s) :\n")
        for livre in resultats:
            print(f"ID: {livre['ID']}")
            print(f"Titre: {livre['Titre']}")
            print(f"Auteur: {livre['Auteur']}")
            print(f"Année: {livre['Annee']}")
            print(f"Lu: {livre['Lu']}")
            print(f"Note: {livre['Note']}")
            print("-" * 40)
    else:
        print("Aucun livre trouvé avec ce mot-clé.")


def marquer_comme_lu(bibliotheque):
    """Marque un livre comme lu, ajoute une note et un commentaire."""
    try:
        identifiant = int(input("Entrez l'ID du livre à marquer comme lu : "))
    except ValueError:
        print("L'ID doit être un nombre.")
        return

    trouve = False

    for livre in bibliotheque['livres']:
        if livre['ID'] == identifiant:
            trouve = True
            if livre['Lu'] == "True":
                print("Ce livre est déjà marqué comme lu.")
            else:
                livre['Lu'] = "True"
                note = input(
                    "Entrez une note sur 10 (laisser vide si aucune) : ").strip()
                if note:
                    while not note.isdigit() or not (0 <= int(note) <= 10):
                        note = input(
                            "Veuillez entrer un nombre entre 0 et 10 : ").strip()
                    livre['Note'] = note
                else:
                    livre['Note'] = "None"

                commentaire = input(
                    "Souhaitez-vous ajouter un commentaire ? (Entrée pour ignorer) : ").strip()
                livre['Commentaire'] = commentaire if commentaire else "Aucun commentaire"
                print("Livre marqué comme lu avec succès.")
            break

    if not trouve:
        print("Aucun livre trouvé avec cet ID.")


def afficher_livres_par_etat(bibliotheque):
    """Affiche les livres lus ou non lus selon le choix de l'utilisateur."""
    choix = input(
        "Voulez-vous afficher les livres (1) lus ou (2) non lus ? Entrez 1 ou 2 : ")

    if choix == "1":
        etat = "True"
        print("\nLivres lus :")
    elif choix == "2":
        etat = False
        print("\nLivres non lus :")
    else:
        print("Choix invalide.")
        return

    # Créer une liste vide pour stocker les livres filtrés
    livres_filtres = []

    # Parcourir tous les livres dans la bibliothèque
    for livre in bibliotheque['livres']:
        # Vérifier si l'état du livre correspond à l'état demandé (lu ou non lu)
        if livre['Lu'] == etat:
            # Si oui, ajouter ce livre à la liste des livres filtrés
            livres_filtres.append(livre)

    if not livres_filtres:
        print("Aucun livre trouvé pour ce filtre.")
        return

    for livre in livres_filtres:
        print(f" ID: {livre['ID']}")
        print(f" Titre: {livre['Titre']}")
        print(f" Auteur: {livre['Auteur']}")
        print(f" Année: {livre['Annee']}")
        print(f" Lu: {livre['Lu']}")
        print(f" Note: {livre.get('Note', 'None')}")
        commentaire = livre.get("Commentaire")
        if commentaire and commentaire.strip():
            print(f" Commentaire: {commentaire}")
        print("-" * 40)
