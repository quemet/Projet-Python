# Projets en Python

## Liste de tout les projets dans le repo

## Projets Débutants

### Calculatrice Basique :

Crée une application de calculatrice en ligne de commande qui peut effectuer des opérations de base comme l'addition, la soustraction, la multiplication et la division.

@todo Voici une explication plus concrète du projet.  
Voici ma solution.

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

### Générateur de Mot de Passe :

Développe un script qui génère des mots de passe aléatoires en fonction de critères définis par l'utilisateur (longueur, utilisation de majuscules, chiffres, symboles, etc.).

### Convertisseur d'Unités :

Crée un programme qui convertit différentes unités (par exemple, de kilomètres en miles, de Celsius en Fahrenheit).

### Gestionnaire de Contacts :

Construit une application simple pour ajouter, afficher, rechercher et supprimer des contacts.

## Projets Intermédiaires

### To-Do List avec Interface Graphique :

Utilise une bibliothèque comme Tkinter pour créer une application de liste de tâches avec une interface utilisateur graphique. 
Permets à l'utilisateur d'ajouter, marquer comme terminées et supprimer des tâches.

### Analyseur de Fichiers Log :

Écris un script qui analyse les fichiers de log (comme ceux d'un serveur web) pour extraire des informations utiles comme les adresses IP les plus fréquentes, les pages les plus visitées, etc.

### Chat en Temps Réel :

Utilise des bibliothèques comme socket et threading pour créer une application de chat en temps réel. Implémente à la fois le serveur et le client.

### Jeu de la Vie de Conway :

Programme le célèbre "Jeu de la vie" de John Conway en utilisant une bibliothèque comme Pygame pour visualiser les évolutions des cellules.

### Application de Suivi des Habitudes :

Crée une application qui permet à l'utilisateur de suivre ses habitudes quotidiennes. 
Utilise une base de données comme SQLite pour stocker les données et une interface graphique pour l'interaction utilisateur.

### Web Scraper :

Développe un script qui extrait des données d'un site web (par exemple, les prix des produits d'un site de e-commerce) en utilisant des bibliothèques comme BeautifulSoup et Requests. Traite et présente ensuite ces données de manière utile.

### Mini Réseau Social :

Crée une application web de base qui permet aux utilisateurs de s'inscrire, de se connecter, de poster des messages et de voir les messages des autres. Utilise un framework web comme Flask ou Django.

### Analyse de Données avec Pandas :

Utilise la bibliothèque Pandas pour analyser un ensemble de données. Par exemple, analyse des données de ventes pour trouver des tendances ou des anomalies.

Voici les projets dans ce repo.