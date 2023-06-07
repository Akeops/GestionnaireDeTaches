import sqlite3

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
    def __init__ (self, idT, nomT, date_creation, idU):
        self.idT = idT
        self.nomT = nomT
        self.date_creation = date_creation
        self.idU = idU


@staticmethod
def getTaches():
    try:
        conn = sqlite3.connect('baseDeDonnee')
        cursor = conn.cursor()

        # Exécution de la requête SELECT pour récupérer les données de la table spécifiée
        cursor.execute(f"SELECT * FROM tache")
        result = cursor.fetchall()

        for row in result:
            print(f" {row[0]},  {row[1]},  {row[2]},  {row[3]}")

        conn.close()
    except sqlite3.Error as e:
        print('Erreur lors de la récupération des utilisateurs:', e)

# Section de TEST des fonctions
'''print("\n getTaches() : \n")
print(getTaches())

print("\n getUtilisateurs() : \n")
print(getUtilisateurs())
'''

def getMessage(message):
    max_size = len(message)
    message += ' ' * (max_size - len(message))
    print()
    print('+' * (len(message) + 4))
    print('+', message, '+')
    print('+' * (len(message) + 4))

def accueilUtilisateur(liste):
    print(f"Bienvenue {liste[2]} {liste[1]}")
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

        util_str = input('> ').lower()
        while not util_str.isdigit() and not 1 <= int(util_str) <= 10:
            print("Choisissez un bon utilisateur.")
            util_str = input('> ')
        util = int(util_str)
        for row in result:
            if row[0] == util:
                liste = [row[0], row[1], row[2], row[3], row[4]]
                accueilUtilisateur(liste)
                #print(f"Bienvenue {row[2]} {row[1]}")
    except:
        print('erreur')




menuUtilisateur()





