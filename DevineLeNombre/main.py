import random

com_number = random.randint(1, 100)
user_life = 5

print("Bienvenue dans le jeu, Devine le just nombre.")
print("                                             ")

def ask_user_number():
    while True:
        try:
            user_number = int(input("Entrer un nombre (entier): "))
            return user_number
        except:
            print("Entrer un nombre valide")

def print_status(user_number):
    if user_number == com_number:
        return "Win"
    elif user_number > com_number:
        return "Too High"
    else:
        return "Too Low"
    

while True:
    user_number = ask_user_number()
    status = print_status(user_number)

    if status == "Win":
        print("Fécilitation, vous avez gagné !!!")
        print("Le nombre était " + str(com_number))
        break
    elif status == "Too High":
        print("Votre nombre est trop haut !!!")
    else:
        print("Votre nombre est trop petit !!!")

    user_life -= 1

    if user_life == 0:
        print("                   ")
        print("Vous avez perdu !!!")
        print("Le nombre était " + str(com_number))
        break

    print("Vous avez encore " + str(user_life) + " vies")
    print("----------------------------")
