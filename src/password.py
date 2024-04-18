# Systeme de verification de mot de pass

def main():
    password = input("Enter your password: ")
    password_length = len(password)

    # verifier si le password est inferieur a 8
    if password_length <= 8:
        print("Le password est trop court")
    else:
        print("Le password est valide")
    print(password_length)
if __name__ == '__main__':
    main()