#Création d'un gestionnaire de tâches : développez une application qui permet aux utilisateurs de créer, organiser et gérer
# leurs tâches quotidiennes.
#
#
# Gestionnaire de tâches : Vous pouvez créer un programme qui permet aux utilisateurs
# de gérer leurs tâches en affichant des menus, en prenant des entrées de l'utilisateur et en affichant les tâches en cours.

class Utilisateur:
    def __init__ (self, idU, prenomU, nomU, pseudoU, mdpU):
        self.idU = idU
        self.prenomU = prenomU
        self.nomU = nomU
        self.pseudoU = pseudoU
        self.mdpU = mdpU
@staticmethod
def getUtilisateurs(listeUtilisateur):
    for i, utilisateur in enumerate(listeUtilisateur, 1):
        print(f"{i} -  {utilisateur.prenomU} {utilisateur.nomU} AKA '{utilisateur.pseudoU}'")


# Création de quelques objets Utilisateur
utilisateur1 = Utilisateur(1 , "Andoni", "Lalanne", "Maven", "123")
utilisateur2 = Utilisateur(2 , "Annabeth", "Chase", "Beth", "456")

# Création de la liste des utilisateurs
listeUtilisateur = []
listeUtilisateur = utilisateur1, utilisateur2

def getMessage(message):
    max_size = len(message)
    message += ' ' * (max_size - len(message))
    print('+' * (len(message) + 4))
    print('+', message, '+')
    print('+' * (len(message) + 4))

def choixUtil(util, pseudo, mdp):
    for i, utilisateur in enumerate(listeUtilisateur, 1):
        if util == i:
            print(utilisateur.pseudoU)
            if pseudo == utilisateur.pseudoU and mdp == utilisateur.mdpU:
                message = f"Bienvenue, {utilisateur.prenomU}"
                getMessage(message)
            else:
                print("Il y a une erreur dans le pseudo ou le mot de passe.")
                # Je remet ici le début du programme pour que l'utilisateur puisse faire un choix d'utilisateur même si il se trompe et ainsi faire une boucle
                print("Bonjour, qui êtes-vous ? Taper 'EXIT' si vous voulez quitter.")
                print()
                getUtilisateurs(listeUtilisateur)
                util_str = input('> ').lower()
                print()
                # l'utilisateur peut taper exit s'il veut quitter
                if util_str == "exit":
                    message = "Aurevoir"
                    getMessage(message)
                    break

                while not util_str.isdigit() or util_str != "exit" and not 1 <= int(util_str) < len(listeUtilisateur):
                    print("Choisissez un bon utilisateur.")
                    util_str = input('> ')
                util = int(util_str)

                print("Pseudo:")
                pseudo = input('> ').capitalize()
                print()

                print("Mot de passe:")
                mdp = input('> ')

                choixUtil(util, pseudo, mdp)



# Début du programme
print()
print("Bonjour, qui êtes-vous ? Taper 'EXIT' si vous voulez quitter.")
print(listeUtilisateur[0].pseudoU)

# Affiche la liste des utilisateurs
getUtilisateurs(listeUtilisateur)
util_str = input('> ').lower()
while not util_str.isdigit() or util_str != "exit" and not 1 <= int(util_str) < len(listeUtilisateur):
    print("Choisissez un bon utilisateur.")
    util_str = input('> ')

util = int(util_str)
if util_str == "exit":
    message = "Aurevoir"
    getMessage(message)

util = int(util_str)

print("Pseudo:")
pseudo = input('> ').capitalize()
print()

print("Mot de passe:")
mdp = input('> ')

choixUtil(util, pseudo, mdp)


