password= input("Enter the password: ")
if len(password)<8:
    print("The password must contain at least  characters. ")
elif not any(char.isdigit() for char in password):
    print("The password must contain at least  one digit.")
elif not any(char.isupper() for char in password):
    print("The password must contain at least  one capitan letter.")
elif not any(char.islower() for char in password):
    print("The password must contain at least  one lowercase letter.")
else:
    print("You have a great password")