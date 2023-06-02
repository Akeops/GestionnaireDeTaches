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
    #for i, utilisateur in listeUtilisateur:
    for i, utilisateur in enumerate(listeUtilisateur, 1):
        print(f"{i} -  {utilisateur.prenomU} {utilisateur.nomU} AKA '{utilisateur.pseudoU}'")

    #@staticmethod
    #def

# Création de quelques objets Utilisateur
utilisateur1 = Utilisateur(1 , "Andoni", "Lalanne", "Maven", "123")
utilisateur2 = Utilisateur(2 , "Annabeth", "Chase", " Beth", "456")

# Création de la liste des utilisateurs
listeUtilisateur = [utilisateur1, utilisateur2]


def choixUtil(util):
    for i, utilisateur in listeUtilisateur:
        if util == i:
            print("Bienvenue", utilisateur.prenomU)


#print(listeUtilisateur[0].nomU)

# Début du programme

print("Bonjour, qui êtes-vous ?")
print()
getUtilisateurs(listeUtilisateur)
util_str = input('> ')
while not util_str.isdigit() and not 1 <= int(util_str) < len(listeUtilisateur):
    print("Choisissez un bon utilisateur.")
    util_str = input('> ')
util = int(util_str)

print(listeUtilisateur)
choixUtil(util)