def access_element(lst, index):
    if 0 <= index < len(lst):
        return lst[index]
    else:
        return "Index out of range"

def modify_element(lst, index, new_value):
    if 0 <= index < len(lst):
        lst[index] = new_value
        return lst
    else:
        return "Index out of range"

def slice_list(lst, start, end):
    if 0 <= start <= end <= len(lst):
        return lst[start:end]
    else:
        return "Invalid slice range"

def main():
    my_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']
    print("Initial list:", my_list)

    while True:
        print("\nChoose an operation:")
        print("1 - Access an element")
        print("2 - Modify an element")
        print("3 - Slice the list")
        print("4 - Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            index = int(input("Enter index to access: "))
            print("Result:", access_element(my_list, index))

        elif choice == "2":
            index = int(input("Enter index to modify: "))
            new_value = input("Enter new value: ")
            result = modify_element(my_list, index, new_value)
            print("Updated list:", result)

        elif choice == "3":
            start = int(input("Start index: "))
            end = int(input("End index: "))
            print("Sliced list:", slice_list(my_list, start, end))

        elif choice == "4":
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
