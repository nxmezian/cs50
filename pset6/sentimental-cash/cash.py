from cs50 import get_float


def main():
    dollars = get_dollars()

    quarters = get_quarters(dollars)
    dollars = dollars - quarters * 0.25
    print(quarters)

    dimes = get_dimes(dollars)
    print(dimes)
    dollars = dollars - dimes * 0.10

    nickels = get_nickels(dollars)
    print(nickels)
    dollars = dollars - nickels * 0.05

    pennies = get_pennies(dollars)
    print(pennies)

    total = int(quarters + dimes + nickels + pennies)
    print(total)


def get_dollars():
    while True:
        dollars = get_float("How many dollars? ")
        if dollars > 0:
            break

    return dollars


def get_quarters(dollars):
    quarters = int(dollars / 0.25)
    return quarters


def get_dimes(dollars):
    dimes = int(dollars / 0.10)
    return dimes


def get_nickels(dollars):
    nickels = int(dollars / 0.05)
    return nickels


def get_pennies(dollars):
    pennies = round(dollars / 0.01)
    return pennies


main()