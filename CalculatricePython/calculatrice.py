def addition(x, y):
    return x + y

def soustraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    return x / y if y != 0 else "Erreur : Division par zéro."

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

while True:
    afficher_menu()
    choix = input("Entre votre choix (1/2/3/4/5): ")
    
    if choix == '5':
        print('Au revoir')
        break

    if choix in ['1', '2', '3', '4']:

        try:
            n1 = float(input("Entrer le chiffre numéro 1 :"))
            n2 = float(input("Entrer le chiffre numéro 2 :"))

            if choix == '1':
                print(f"Le résultat de l'addition de {n1} et de {n2} == {addition(n1, n2)}")
            elif choix == '2':
                print(f"Le résultat de la soustraction de {n1} et de {n2} == {soustraction(n1, n2)}")
            elif choix == '3':
                print(f"Le résultat de la multiplication de {n1} et de {n2} == {multiplication(n1, n2)}")
            else:
                print(f"Le résultat de la division de {n1} et de {n2} == {division(n1, n2)}")
        except:
            print("Le choix est invalide")

    else:
        print("Choix invalide. Essayez de nouveau.")

