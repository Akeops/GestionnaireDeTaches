import sqlite3
from datetime import date
import traceback

# Connexion à la base de données
conn = sqlite3.connect('baseDeDonnee')

try:
    conn = sqlite3.connect('BaseDeDonnee')
    print("Connecté à la base de données.")
    conn.close()
except sqlite3.Error as e:
    print("Erreur de connexion à la base de données:", e)

class Utilisateur:
    def __init__ (self, idU, prenomU, nomU, pseudoU, mdpU):
        self.idU = idU
        self.prenomU = prenomU
        self.nomU = nomU
        self.pseudoU = pseudoU
        self.mdpU = mdpU
@staticmethod
def getUtilisateurs():
    try:
        conn = sqlite3.connect('baseDeDonnee')
        cursor = conn.cursor()

        # Exécution de la requête SELECT pour récupérer les données de la table spécifiée
        cursor.execute(f"SELECT * FROM utilisateur")
        result = cursor.fetchall()

        for row in result:
            print(f" {row[0]},  {row[1]},  {row[2]},  {row[3]}, {row[4]}")
        conn.close()
    except sqlite3.Error as e:
        print('Erreur lors de la récupération des utilisateurs:', e)



class Tache:
    def __init__ (self, idT, nomT, date_creation, idU, description):
        self.idT = idT
        self.nomT = nomT
        self.date_creation = date_creation
        self.idU = idU
        self.description = description


@staticmethod
def supprTache(idSupprInt, liste):
    try:
        conn = sqlite3.connect('baseDeDonnee')
        cursor = conn.cursor()

        cursor.execute(f"DELETE FROM tache WHERE idT = {idSupprInt};")
        conn.commit()

        cursor.close()
        conn.close()
        print('Suppression réussi')
        print()

        getTachesByIdU(liste[0], liste)
    except sqlite3.Error as e:
        print('Erreur lors de la suppression de la tâche:', e)

# C'est dans cette fonction qu'il y a tous les choix de l'utilisateur par rapport aux fonctions.
def getTachesByIdU(idU, liste):
    try:
        conn = sqlite3.connect('baseDeDonnee')
        cursor = conn.cursor()


        cursor.execute(f"SELECT * FROM tache WHERE idu = {idU}")
        result = cursor.fetchall()
        i = 1
        for row in result:
            print(f"{row[0]} - {row[1]}, le {row[2]} | '{row[4]}'")
            i += 1


        print(f"{len(result) + 1} - Ajouter une nouvelle tâche")
        print(f"{len(result) + 2} - Supprimer une tâche")
        print(f"{len(result) + 3} - Retour à la liste des utilisateurs")

        choix = input('> ')
        while int(choix) != len(result) + 1 and int(choix) != len(result) + 2 and int(choix) != len(result) + 3:
            print("Il n'est pas possible de faire cette action.")
            choix = input('> ')

        choixInt = int(choix)
        if choixInt == len(result) + 1:
            print("Ajout d'une tâche")

            print('Nom de la tâche :')
            nomT = input('> ')

            print('Description de la tâche :')
            description = input('> ')
            dateDuJour = date.today()
            addTache(nomT, dateDuJour, idU, description, liste)
            print()
            print('La tache a été ajouté.')
            getTachesByIdU(idU, liste)

        elif choixInt == len(result) + 2:
            print('Quelle tâche voulez-vous supprimer ?')
            idSupprInt = int(input('> '))
            supprTache(idSupprInt, liste)

        elif choixInt == len(result) + 3:
            menuUtilisateur()
            liste = []
        else:
            print('Sorry')

        conn.close()
    except sqlite3.Error as e:
        print('Erreur lors de la récupération des utilisateurs:', e)

def addTache(nomT, dateDuJour, idU, description, liste):
    try:
        conn = sqlite3.connect('baseDeDonnee')
        cursor = conn.cursor()

        cursor.execute(f'INSERT INTO tache (nomT, date_creation, idU, description) VALUES ("{nomT}", "{dateDuJour}", {idU}, "{description}")')
        conn.commit()

        cursor.close()
        conn.close()
        getTachesByIdU(idU, liste)
    except Exception as e:
        print("Une erreur s'est produite lors de l'insertion :", e)


def addUtilisateur(prenomU, nomU, pseudoU, mdpU):
    try:
        conn = sqlite3.connect('baseDeDonnee')
        cursor = conn.cursor()

        cursor.execute(f'INSERT INTO utilisateur (prenomU, nomU, pseudoU, mdpU) VALUES ("{prenomU}", "{nomU}", "{pseudoU}", "{mdpU}")')
        conn.commit()

        cursor.close()
        conn.close()
        menuUtilisateur()
    except Exception as e:
        print("Une erreur s'est produite lors de l'insertion :", e)
def accueilUtilisateur(liste):
    print(f"Bienvenue {liste[2]} {liste[1]}")

    print()

    print('Voici vos tâches :')
    getTachesByIdU(liste[0], liste)


def menuUtilisateur():
    print()
    print("Bonjour, qui êtes-vous ?")
    # J'affiche toute la table des utilisateurs
    getUtilisateurs()

    try:
        conn = sqlite3.connect('baseDeDonnee')
        cursor = conn.cursor()

        cursor.execute(f"SELECT * FROM utilisateur")
        result = cursor.fetchall()

        print(f"{len(result) + 1} - Ajouter un nouvel utilisateur")
        #print(f"{len(result) + 2} - Supprimer une tâche")

        choix_str = input('> ')
        if choix_str.isdigit() == False:
            print('Seulement les nombres sont acceptés')
            menuUtilisateur()

        while not 0 < int(choix_str) < len(result) and int(choix_str) != len(result) + 1:
            print("Cette action n'est pas possible")
            choix_str = input('> ')

        choix = int(choix_str)
        for row in result:
            if choix == row[0]:
                print('Quel est votre pseudo ?')
                pseudo = input('> ')

                print('Quel est votre mot de passe ?')
                mdp = input('> ')
                if row[3] == pseudo and row[4] == mdp:
                    # Connection de l'utilisateur
                    liste = [row[0], row[1], row[2], row[3], row[4]]
                    accueilUtilisateur(liste)
                else:
                    print('Le pseudo ou le mot de passe ne correspond pas.')
                    menuUtilisateur()
            elif choix == len(result) + 1:
                print("Ajout d'une tâche")

                print('Votre prénom :')
                prenomU = input('> ')

                print('Votre nom :')
                nomU = input('> ')

                print('Votre pseudo :')
                pseudoU = input('> ')
                for row in result:
                    if pseudoU == row[2]:
                        print('Vous ne pouvez pas choisir ce pseudo, il est déjà utilisé.')
                        pseudoU = input('> ')

                print('Votre mot de passe :')
                mdpU = input('> ')

                addUtilisateur(prenomU, nomU, pseudoU, mdpU)
                print()
                print('Vous avez ajouté un nouvel utilisateur.')
    except Exception as e:
        print("Une erreur s'est produite :", e)
        traceback.print_exc()



# Début du code
menuUtilisateur()




''''#nomT, date_creation, idU, description
# Section de TEST des fonctions
print("\n getTaches() : \n")
print(getTaches())

print("\n getUtilisateurs() : \n")
print(getUtilisateurs())

print("\n getUtilisateurs() : \n")
print(getTachesByIdU(1))'''
