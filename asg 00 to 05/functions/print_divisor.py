def print_divisors(num: int):
    # Inform the user
    print("Here are the divisors of", num)
    
    # Loop from 1 to num (inclusive)
    for i in range(num):
        curr_divisor = i + 1  # Because range starts from 0
        if num % curr_divisor == 0:
            print(curr_divisor)


def main():
    # Ask the user to enter a number
    num = int(input("Enter a number: "))
    # Call the function to print divisors
    print_divisors(num)


# This ensures main() runs only if this file is executed directly
if __name__ == '__main__':
    main()
