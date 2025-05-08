def print_ones_digit(num: int):
    # Use modulo to get the ones digit
    ones_digit = num % 10
    print(f"The ones digit is {ones_digit}")


def main():
    # Prompt user for input
    num = int(input("Enter a number: "))
    # Call the function to print the ones digit
    print_ones_digit(num)


if __name__ == '__main__':
    main()

