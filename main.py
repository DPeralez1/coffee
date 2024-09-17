from tabulate import tabulate
import csv
import sys

def main():
    greeting = input("Hello, would you like to see the menu? (y/n): ").lower()
    try:
        if greeting == "y":
            menu("menu.csv")
            print("-------------------------------------")
            order_item()
        else:
            sys.exit("Later!")
    except FileNotFoundError:
        sys.exit("File does not exist!")

def order_item():
    while True:
        order = input("What would you like to order? ").lower()
        print()
        print("-------------------------------------")
        print()
        print("Here is your Iced Americano!")
        print()
        print("-------------------------------------")
        reorder = input("Would you like to order something else? (y/n): ").lower()
        if "q" == reorder:
            break
        elif "y" == reorder:
            menu("menu.csv")
            continue
        else:
            print("***********************************")
            print()
            sys.exit("Later!")

def menu(filename):
    with open(filename) as csvfile:
        reader = csv.reader(csvfile)
        data = list(reader)

    print(tabulate(data, headers="firstrow", tablefmt="grid"))

if __name__ == "__main__":
    main()
