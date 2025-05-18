# Point d'entree du programme
import json

from bibliotheque import (
    afficher_menu,
    afficher_tous_les_livres,
    ajouter_livre,
    sauvegarder_bibliotheque
)

# Charger les données une seule fois au début
with open("bibliotheque.json", "r", encoding="utf-8") as f:
    bibliotheque = json.load(f)


def main():
    while True:
        afficher_menu()
        choix = input("Votre choix : ")

        if choix == "1":
            afficher_tous_les_livres()
        elif choix == "2":
            ajouter_livre()
        elif choix == "8":
            sauvegarder_bibliotheque(bibliotheque)
            print("Données sauvegardées avec succées.")
            print(" Au revoir !")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")


if __name__ == "__main__":
    main()
