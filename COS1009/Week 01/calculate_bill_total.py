def main():
    print("Enter the appetizer price:")
    appetizer_price = float(input())

    print("Enter the main price:")
    main_price = float(input())

    print("Enter the dessert price:")
    dessert_price = float(input())

    total_price = appetizer_price + main_price + dessert_price

    print("$" + format(total_price, ".2f"))


if __name__ == "__main__":
    main()