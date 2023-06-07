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
            print(f" {row[0]},  {row[1]},  {row[2]},  {row[3]}, {row[4]}")

        conn.close()
    except sqlite3.Error as e:
        print('Erreur lors de la récupération des utilisateurs:', e)

# Section de TEST des fonctions

print("\n getTaches() : \n")
print(getTaches())

print("\n getUtilisateurs() : \n")
print(getUtilisateurs())


def getMessage(message):
    max_size = len(message)
    message += ' ' * (max_size - len(message))
    print()
    print('+' * (len(message) + 4))
    print('+', message, '+')
    print('+' * (len(message) + 4))

def menuUtilisateur():
    # Début du programme
    print()
    print("Bonjour, qui êtes-vous ? Taper 'EXIT' si vous voulez quitter.")

    # Affiche la liste des utilisateurs
    getUtilisateurs(listeUtilisateur)

    # Affiche une option pour créer un utilisateur
    for i in enumerate(listeUtilisateur, 1):
        addUtil = len(listeUtilisateur) + 1
    print(f"{addUtil} -  Créer un nouvel utilisateur")

    util_str = input('> ').lower()
    while not util_str.isdigit() or util_str != "exit" and not 1 <= int(util_str) <= addUtil:
        print("Choisissez un bon utilisateur.")
        util_str = input('> ')

    if util_str == "exit":
        message = "Aurevoir"
        getMessage(message)
    elif int(util_str) == addUtil:
        addUtilisateur(addUtil)
    util = int(util_str)

    print("Pseudo:")
    pseudo = input('> ').capitalize()
    print()

    print("Mot de passe:")
    mdp = input('> ')

    choixUtil(util, pseudo, mdp, addUtil)

def addUtilisateur(addUtil):

    #Nom nouvel utilisateur

    print("Quel est votre nom ?")
    name = input('> ')
    while name.isdigit():
        print('Votre nom ne peut pas comporter de nombre')
        name = input('> ')

    # Prénom nouvel utilisateur

    print("Quel est votre prénom ?")
    firstName = input('> ').capitalize()
    while firstName.isdigit():
        print('Votre prénom ne peut pas comporter de nombre')
        firstName = input('> ').capitalize()

    # Pseudo nouvel utilisateur

    print("Choisissez un pseudo, il vous permettra de vous connecter")
    pseudo = input('> ').capitalize()
    for i, utilisateur in enumerate(listeUtilisateur, 1):
        while utilisateur.pseudoU == pseudo:
            print("Ce pseudo est déjà prit, veuillez en prendre un nouveau.")
            pseudo = input('> ').capitalize()

    # Mot de passe nouvel utilisateur

    print("Choisissez un mot de passe")
    mdp = input('> ')

    nouvelUtilisateur = Utilisateur(addUtil + 1, firstName, name, pseudo, mdp)
    listeUtilisateur.append(nouvelUtilisateur)

    for i, utilisateur in enumerate(listeUtilisateur, 1):
        if utilisateur.pseudoU == pseudo:
            print()
            message = "Félicitations, vous faîtes maintenant partie de l'équipage !"
            getMessage(message)

    menuUtilisateur()

def choixUtil(util, pseudo, mdp, addUtil):
    for i, utilisateur in enumerate(listeUtilisateur, 1):
        if util == i:
            if pseudo == utilisateur.pseudoU and mdp == utilisateur.mdpU:
                message = f"Bienvenue, {utilisateur.prenomU}"
                getMessage(message)
            else:
                print("Il y a une erreur dans le pseudo ou le mot de passe.")
                menuUtilisateur()


        if util == addUtil + 1:
            addUtilisateur()

menuUtilisateur()





