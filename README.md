# Projets en Python

## Liste de tout les projets dans le repo

## Projets Débutants

### Calculatrice Basique :

Crée une application de calculatrice en ligne de commande qui peut effectuer des opérations de base comme l'addition, la soustraction, la multiplication et la division.

Voici une explication plus concrète du projet :

#### Objectif du Projet
Créer une application de calculatrice en ligne de commande qui permet à l'utilisateur d'effectuer des opérations arithmétiques de base : 
* Addition
* Soustraction
* Multiplication
* Division.

#### Étapes à Suivre

##### Configurer le Projet :

* Installe Python si ce n'est pas déjà fait.
* Crée un fichier pour ton script, par exemple calculatrice.py.
* Structure de Base du Script :

    * Définis les fonctions pour chaque opération arithmétique.
    * Crée une interface utilisateur en ligne de commande pour choisir les opérations et entrer les nombres.

Voici ma solution :

[Fichier python](./Calculatrice/calculatrice.py)

```python
# Fonction qui retourne l'addition de deux nombres
def addition(x, y):

    # retourne l'addition de x et y
    return x + y

# Fonction qui retourn la soustraction de deux nombres
def soustraction(x, y):

    # retourne la soustraction de x et y
    return x - y

# Fonction qui retourne la multiplication de deux nombres
def multiplication(x, y):

    # retourne la multiplication de x et y
    return x * y

# Fonction qui retourne la division de deux nombres
def division(x, y):

    # retourne la division de x et y si y n'est pas équal à y
    return x / y if y != 0 else "Erreur : Division par zéro."

# Fonction pour afficher les choix qui s'offrent à l'utilisateur
def afficher_menu():
    print("Bienvenue dans ma calculatrice") 
    print("")
    print("Veuillez sélectionner une opération")
    print("")
    print("1 - Addition")
    print("2 - Soustraction")
    print("3 - Multiplication")
    print("4 - Division")
    print("5 - Quitter")

# Boucle infini pour la boucle du jeu
while True:

    # Appelle la fonction pour afficher le menu
    afficher_menu()

    # Demande à l'utilisateur de faire un choix
    choix = input("Entre votre choix (1/2/3/4/5): ")
    
    # Si le choix est 5 alors on quitte l'application
    if choix == '5':
        print('Au revoir')
        break

    # Si le choix est 1 2 3 4 on affiche le résultat de l'opération arithmétique correspondante
    if choix in ['1', '2', '3', '4']:

        # On essaie d'éxecuter le code suivant si il n'emmet pas d'erreur on quitte le jeu
        try:

            # On essaie de transformer le input de l'utilisateur en float
            n1 = float(input("Entrer le chiffre numéro 1 :"))

            # On essaie de transformer le input de l'utilisateur en float
            n2 = float(input("Entrer le chiffre numéro 2 :"))

            # On check le choix si c'est l'un d'eux alors on effectue la opération adéquate
            if choix == '1':
                print(f"Le résultat de l'addition de {n1} et de {n2} == {addition(n1, n2)}")
            elif choix == '2':
                print(f"Le résultat de la soustraction de {n1} et de {n2} == {soustraction(n1, n2)}")
            elif choix == '3':
                print(f"Le résultat de la multiplication de {n1} et de {n2} == {multiplication(n1, n2)}")
            else:
                print(f"Le résultat de la division de {n1} et de {n2} == {division(n1, n2)}")

        # On léve une exception si une erreur est survenue
        except:
            print("Le choix est invalide")
    # Si aucun des choix est valide alors on emmet une erreur
    else:
        print("Choix invalide. Essayez de nouveau.")

```

### Jeu du Devine le Nombre :

Programme un jeu où l'ordinateur choisit un nombre aléatoire et l'utilisateur doit deviner ce nombre en recevant des indices sur la direction (plus haut, plus bas).

Voici une explication plus concrète :

#### Objectifs du Projet
* Générer un nombre aléatoire que le joueur doit deviner.
* Permettre au joueur de saisir ses suppositions.
* Fournir des indices pour guider le joueur.
* Limiter le nombre de tentatives pour ajouter un élément de défi.
* Afficher des messages de victoire ou de défaite.
* Étapes de la Mise en Œuvre
    * Importer les Modules Nécessaires :
        * Utilisez le module random pour générer des nombres aléatoires.

##### Définir les Variables :

* com_number : le nombre aléatoire que l'ordinateur a choisi.
* user_life : le nombre de tentatives que le joueur a pour deviner le nombre.
* Fonction pour Demander un Nombre à l'Utilisateur :
    * Créez une fonction qui demande à l'utilisateur d'entrer un nombre et gère les entrées non valides.

* Fonction pour Vérifier le Nombre Devine :
    * Créez une fonction qui compare le nombre deviné par l'utilisateur avec le nombre choisi par l'ordinateur et retourne un indice (trop haut, trop bas, ou correct).

##### Boucle Principale du Jeu :

* Demandez à l'utilisateur de deviner le nombre.
* Fournissez des indices.
* Réduisez le nombre de tentatives après chaque essai incorrect.
* Affichez un message de victoire ou de défaite en fonction du résultat.

Voici ma réponse :

[Fichier python](./DevineLeNombre/main.py)

```py

# Importer le module random
import random

# Définir le chiffre à deviner
com_number = random.randint(1, 100)

# Le nombre de vie de l'utilisateur
user_life = 5

# Afficher le titre du projet et un espace
print("Bienvenue dans le jeu, Devine le just nombre.")
print("                                             ")

# Défini une fonction pour demander un nombre à l'utilisateur
def ask_user_number():

    # Défini une boucle infinie
    while True:

        # Essaie de convertir l'entrée de l'utilisateur ent entier
        try:

            # Converti l'entrée de l'utilisateur en entier
            user_number = int(input("Entrer un nombre (entier) : "))

            # Retourne l'entrée de l'utilisateur si il n'y a pas d'erreur
            return user_number
        except:

            # Si la conversion renvoie une erreur alors on affiche le message 
            print("Entrer un nombre valide")

# Défini une fonction qui affiche le status pour les eux chiffres
def print_status(user_number):

    # Si les deux nombres sont égal alors l'utilisateur a gagné
    if user_number == com_number:
        return "Win"
    # Si il donne un chiffre plus haut alors on renvoie le message
    elif user_number > com_number:
        return "Too High"
    # Si il donne un chiffre plus bas alors on renvoie le message
    else:
        return "Too Low"
    
# Défini une boucle principale infinie
while True:

    # Demande à l'utilisateur un nombre
    user_number = ask_user_number()

    # Regarde si l'utilisateur a gagné
    status = print_status(user_number)

    # Si status renvoie Win alors l'utilisateur a gagné
    if status == "Win":

        # On affiche un message de fécilitation et le chiffre juste
        print("Fécilitation, vous avez gagné !!!")
        print("Le nombre était " + str(com_number))

        # On quitte la boucle principale
        break
    # Si status renvoie Trop Haut alors on le notifie à l'utilisateur
    elif status == "Too High":
        print("Votre nombre est trop haut !!!")
    # Si status renvoie Trop Bas alors on le notifie à l'utilisateur
    else:
        print("Votre nombre est trop petit !!!")

    # On décrémente la vie de l'utilisateur
    user_life -= 1

    # Si la vie de l'utilisateur est de 0 alors il a perdu
    if user_life == 0:
        print("                   ")
        print("Vous avez perdu !!!")
        print("Le nombre était " + str(com_number))
        break

    # On affiche la vie de l'utilisateur
    print("Vous avez encore " + str(user_life) + " vies")
    print("----------------------------")

```

### Générateur de Mot de Passe :

Développe un script qui génère des mots de passe aléatoires en fonction de critères définis par l'utilisateur (longueur, utilisation de majuscules, chiffres, symboles, etc.).

Voici une explication plus concrète :

#### Objectif du Projet
* Créer un programme qui génère des mots de passe aléatoires en fonction des critères définis par l'utilisateur, comme la longueur du mot de passe et l'inclusion de majuscules, de chiffres et de caractères spéciaux.

* Étapes à Suivre
    * Importer les Bibliothèques Nécessaires
    * Définir les Caractères Disponibles
    * Prendre les Entrées de l'Utilisateur
    * Générer le Mot de Passe
    * Afficher le Mot de Passe Généré

Voici ma réponse :

[Fichier python](./GenerateurMotDePasse/main.py)

```py

# Importe le module random
import random

# Demande à l'utilisateur la longueur du mot de passe
length = int(input("What's the length of the password :"))

# Demande à l'utilisateur s'il veut des lettres majuscules
isUsingUpperCaseLetter = True if "Y" == input("Do you want upper case letter into your password (Y/N): ").upper() else False

# Demande à l'utilisateur s'il veut des lettres minuscules
isUsingNumber = True if "Y" == input("Do you want number into your password (Y/N): ").upper() else False

# Demande à l'utilisateur s'il veut des charactères spéciales
isUsingSpecialCaracter = True if "Y" == input("Do you want special caracter into your password (Y/N): ").upper() else False

# Défini une fonction pour généreer le mot de passe
def generate_password(length, use_uppercase, use_numbers, use_special):
    
    # Défini les listes de minuscule, majuscule, chiffre et etc...
    lower_characters = list('abcdefghijklmnopqrstuvwxyz')
    upper_characters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    number_characters = list('0123456789')
    special_characters = list('[@_!#$%^&*()<>?/|}{~:]')
    
    # Défini un tableaux avec les minuscule
    all_characters = lower_characters
    
    # Si l'utilisateur a accepté de mettre des majuscules on ajoute le tableaux des majuscules
    if use_uppercase:
        all_characters += upper_characters
    
    # Si l'utilisateur a accepté de mettre des chiffres on ajoute le tableaux des chiffres
    if use_numbers:
        all_characters += number_characters

    # Si l'utilisateur a accepté de mettre des caractères spéciales on ajoute le tableaux des caractères spéciales
    if use_special:
        all_characters += special_characters

    # On crée le mot de passe avec les choix de l'utilisateur
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    # On retourne le mot de passe de l'utilisteur
    return password

# On crée le mot de passe avec les choix de l'utilisateur
password = generate_password(length, isUsingUpperCaseLetter, isUsingNumber, isUsingSpecialCaracter)

# On affiche le mot de passe à l'utilisateur
print("Votre mot de passe est : ", password)

```

### Convertisseur d'Unités :

Crée un programme qui convertit différentes unités (par exemple, de kilomètres en miles, de Celsius en Fahrenheit).

Voici une explication plus concrète :

#### Objectif du Projet
* Créer un programme qui permet à l'utilisateur de convertir des valeurs entre différentes unités de mesure. Les unités peuvent inclure des conversions de longueur (mètres, kilomètres, pieds, pouces), de poids (grammes, kilogrammes, livres), de température (Celsius, Fahrenheit), etc.

* Étapes à Suivre
    * Définir les Fonctions de Conversion
    * Afficher le Menu et Prendre les Entrées Utilisateur
    * Effectuer la Conversion et Afficher le Résultat

Voici ma réponse :

[Fichier python](./ConvertisseurUnite/main.py)

### Gestionnaire de Contacts :

Construit une application simple pour ajouter, afficher, rechercher et supprimer des contacts.

Voici ma réponse :

[Fichier python](./GestionContact/main.py)

### To-Do List avec Interface Graphique :

Utilise une bibliothèque comme Tkinter pour créer une application de liste de tâches avec une interface utilisateur graphique. 
Permets à l'utilisateur d'ajouter, marquer comme terminées et supprimer des tâches.

Voici ma réponse :

[Fichier python](./ToDoList/main.py)