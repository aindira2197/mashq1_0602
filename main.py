son1 = int(input("1-son kirit: "))
son2 = int(input("2-son kirit: "))
amal = input("Amal kirit((+, -)): ")

match amal:
    case "+":
        print(son1+son2)
    case "-":
        print(son1-son2)
    case _:
        print("Amal xato")
