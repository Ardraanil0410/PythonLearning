special_chars="@#$%^&*!?"
while True:
    password = input("Please enter the password : ")

    if len(password)<8:
        print("Please have a minimum of 8 characters")
        continue
    if not any(char.isdigit() for char in password):
        print("Password must have atleast one number")
        continue
    if not any(char.isupper() for char in password):
        print("Password atleast should have one upper letter")
        continue
    if not any(char in special_chars for char in password):
        print("Password should atleast have one special character")
        continue
    else:
        print("You got a strong password")
        break