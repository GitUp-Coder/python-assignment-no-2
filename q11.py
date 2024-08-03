def main():
    values = []
    print("Enter values add to the list. Press Enter without typing anything to finish.")

    while True:
        user_input = input("Enter a value: ")
        if user_input == "":
            break
        values.append(user_input)

    print("The list of values is:")
    print(values)

if __name__ == "__main__":
    main()
