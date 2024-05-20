import random

length = int(input("What's the length of the password :"))
isUsingUpperCaseLetter = True if "Y" == input("Do you want upper case letter into your password (Y/N): ").upper() else False
isUsingNumber = True if "Y" == input("Do you want number into your password (Y/N): ").upper() else False
isUsingSpecialCaracter = True if "Y" == input("Do you want special caracter into your password (Y/N): ").upper() else False

def generate_password(length, use_uppercase, use_numbers, use_special):
    lower_characters = list('abcdefghijklmnopqrstuvwxyz')
    upper_characters = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    number_characters = list('0123456789')
    special_characters = list('[@_!#$%^&*()<>?/|}{~:]')
    
    all_characters = lower_characters
    
    if use_uppercase:
        all_characters += upper_characters
    if use_numbers:
        all_characters += number_characters
    if use_special:
        all_characters += special_characters

    if not all_characters:
        return "Erreur : Aucune catégorie de caractères sélectionnée."

    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password


password = generate_password(length, isUsingUpperCaseLetter, isUsingNumber, isUsingSpecialCaracter)
print("Votre mot de passe est : ", password)
