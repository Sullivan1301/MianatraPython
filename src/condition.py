def main():
    wallet = int(input("combien as tu d'argent en ce moment: "))
    sakafo_price = int(input("combien a coute ton repas: "))
    if sakafo_price > wallet:
        print("Tu n'as pas assez d'argent")
    else:
        wallet -= sakafo_price
        print("Il te reste {} apres ton repas".format(wallet))

    ternaire = ("Achat effectué", "Achat impossible")[wallet <= sakafo_price]
    print(ternaire)

if __name__ == "__main__":
    main()
