
import json
import os

FICHIER_DATA = os.path.join("data", "bibliotheque.json")


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
