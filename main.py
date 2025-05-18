# Point d'entree du programme ou de l'application

from bibliotheque import (
    afficher_tous_les_livres,
    ajouter_livre,
    supprimer_livre,
    rechercher_livre_par_mot_cle,
    marquer_comme_lu,
    afficher_livres_par_etat
)

from helpers.utils import sauvegarder_bibliotheque, charger_bibliotheque, afficher_menu


def main():
    # Charger les données de la bibliotheque existante une seule fois au début
    bibliotheque = charger_bibliotheque()

    while True:
        afficher_menu()
        choix = input("Votre choix : ")

        if choix == "1":
            afficher_tous_les_livres(bibliotheque)
        elif choix == "2":
            ajouter_livre(bibliotheque)
        elif choix == "3":
            supprimer_livre(bibliotheque)
        elif choix == "4":
            rechercher_livre_par_mot_cle(bibliotheque)
        elif choix == "5":
            marquer_comme_lu(bibliotheque)
        elif choix == "6":
            afficher_livres_par_etat(bibliotheque)
        elif choix == "8":
            sauvegarder_bibliotheque(bibliotheque)
            print(" Au revoir !")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")


if __name__ == "__main__":
    main()
