def main():

    note1 = int(input("Entre ta premiere note: "))
    note2 = int(input("Entre ta seconde note: "))
    note3 = int(input("Entre ta troisieme note: "))
    result = (note1 + note2+note3) / 3

    print("Ta moyenne est de " +  str(result))

if __name__ == '__main__':
    main()
