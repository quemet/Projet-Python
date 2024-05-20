# Fonctions de conversion
def meters_to_kilometers(meters):
    return meters / 1000

def kilometers_to_meters(kilometers):
    return kilometers * 1000

def grams_to_kilograms(grams):
    return grams / 1000

def kilograms_to_grams(kilograms):
    return kilograms * 1000

def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

# Affichage des menus
def afficher_menu():
    print("\nConvertisseur d'unités")
    print("1 - Longueur")
    print("2 - Poids")
    print("3 - Température")
    print("4 - Quitter")

def afficher_menu_longueur():
    print("\nConversion de longueur")
    print("1 - Mètres en Kilomètres")
    print("2 - Kilomètres en Mètres")
    print("3 - Retour")

def afficher_menu_poids():
    print("\nConversion de poids")
    print("1 - Grammes en Kilogrammes")
    print("2 - Kilogrammes en Grammes")
    print("3 - Retour")

def afficher_menu_temperature():
    print("\nConversion de température")
    print("1 - Celsius en Fahrenheit")
    print("2 - Fahrenheit en Celsius")
    print("3 - Retour")

# Boucle principale
while True:
    afficher_menu()
    choix = input("Entrer votre choix : ")

    if choix == '1':
        while True:
            afficher_menu_longueur()
            choix_longueur = input("Sélectionner une option : ")

            if choix_longueur in ['1', '2']:
                try:
                    longueur = float(input("Entrer la valeur à convertir : "))
                    if choix_longueur == '1':
                        resultat = meters_to_kilometers(longueur)
                        print(f"{longueur} mètres = {resultat} kilomètres")
                    elif choix_longueur == '2':
                        resultat = kilometers_to_meters(longueur)
                        print(f"{longueur} kilomètres = {resultat} mètres")
                    break
                except ValueError:
                    print("Veuillez entrer une valeur valide.")
            elif choix_longueur == '3':
                break
            else:
                print("Choix invalide.")

    elif choix == '2':
        while True:
            afficher_menu_poids()
            choix_poids = input("Sélectionner une option : ")

            if choix_poids in ['1', '2']:
                try:
                    poids = float(input("Entrer la valeur à convertir : "))
                    if choix_poids == '1':
                        resultat = grams_to_kilograms(poids)
                        print(f"{poids} grammes = {resultat} kilogrammes")
                    elif choix_poids == '2':
                        resultat = kilograms_to_grams(poids)
                        print(f"{poids} kilogrammes = {resultat} grammes")
                    break
                except ValueError:
                    print("Veuillez entrer une valeur valide.")
            elif choix_poids == '3':
                break
            else:
                print("Choix invalide. Veuillez réessayer.")

    elif choix == '3':
        while True:
            afficher_menu_temperature()
            choix_temperature = input("Sélectionner une option : ")

            if choix_temperature in ['1', '2']:
                try:
                    temperature = float(input("Entrer la valeur à convertir : "))
                    if choix_temperature == '1':
                        resultat = celsius_to_fahrenheit(temperature)
                        print(f"{temperature} °C = {resultat} °F")
                    elif choix_temperature == '2':
                        resultat = fahrenheit_to_celsius(temperature)
                        print(f"{temperature} °F = {resultat} °C")
                    break
                except ValueError:
                    print("Veuillez entrer une valeur valide.")
            elif choix_temperature == '3':
                break
            else:
                print("Choix invalide. Veuillez réessayer.")

    elif choix == '4':
        print("Au revoir!")
        break

    else:
        print("Choix invalide. Veuillez réessayer.")
