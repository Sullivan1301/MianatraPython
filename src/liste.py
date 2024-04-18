def main():
    rakotoniaina_name = ["Tahina", "Anja", "Sullivan", "Nayah"]
    print(rakotoniaina_name)
    rakotoniaina_name[0] = "le pere"
    print(rakotoniaina_name)
    rakotoniaina_name.insert(2, "Joro")
    print(rakotoniaina_name)
    rakotoniaina_name[2:4]=["le fils", "la fille"]
    print(rakotoniaina_name)
if __name__ == '__main__':
    main()