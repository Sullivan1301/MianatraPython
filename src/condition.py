def main():
    wallet = int(input("combien as tu d'argent en ce moment: "))
    sakafo_price = int(input("combien a coute ton repas: "))
    if sakafo_price > wallet:
        print("Tu n'as pas assez d'argent")
    else:
        wallet -= sakafo_price
        print("Il te reste " +  str(wallet)+ " apres ton repas")


if __name__ == "__main__":
    main()
