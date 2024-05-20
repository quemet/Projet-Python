contacts = []

contacts.append({"nom": "sample1", "numero": "0791234567", "email": "sample123@gmail.com"})

def ajouter_contact():
    nom = input("Veuillez entrer un nom : ")
    numero = input("Veuillez entrer un numero : ")
    email = input("Veuillez entrer un email : ")

    global contacts

    contacts.append({"nom": nom, "numero": numero, "email": email})
    
    print(f"\nLe contact {nom} a bien été ajouté.")

def afficher_contacts():
    if contacts:
        for contact in contacts:
            print(f"Le nom du contact est {contact['nom']}.")
            print(f"Le numero du contact est {contact['numero']}.")
            print(f"L'email du contact est {contact['email']}.")
            print("")
    else:
        print("Aucun contact trouvé.")

def rechercher_nom():
    nom = input("Veuillez entrer le nom : ").lower()
    trouve = False

    for contact in contacts:
        if contact["nom"].lower() == nom:
            print(f"Le nom du contact est {contact['nom']}.")
            print(f"Le numero du contact est {contact['numero']}.")
            print(f"L'email du contact est {contact['email']}.")
            print("")
            trouve = True
            break

    if not trouve:
        print("Contact non trouvé.")

def supprimer_contact():
    nom = input("Entrer le nom du contact à supprimer : ").lower()
    global contacts
    contacts = [contact for contact in contacts if contact["nom"].lower() != nom]
    print("Contact supprimé avec succès.")

def afficher_menu():
    print("\nGestion des contacts")
    print("1 : Ajouter de nouveaux contacts.")
    print("2 : Afficher tous les contacts.")
    print("3 : Rechercher un contact par nom.")
    print("4 : Supprimer un contact.")
    print("5 : Quitter l'application.")

while True:
    afficher_menu()

    try:
        choix = input("Veuillez choisir une option : ")

        if choix == '1':
            ajouter_contact()
        elif choix == '2':
            afficher_contacts()
        elif choix == '3':
            rechercher_nom()
        elif choix == '4':
            supprimer_contact()
        elif choix == '5':
            print("Au revoir!")
            break
        else:
            print("Choix invalide")
    except Exception as ex:
        print(ex)
        print("Erreur : veuillez entrer un choix valide.")
