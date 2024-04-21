import  statistics
def main():
    notes = [
        16, 12, 8,
        15, 20, 10,
    ]
    result = statistics.mean(notes)
    print("la moyenne est {}".format(result))

if __name__ == '__main__':
    main()