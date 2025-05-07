from convert import Convert
from intro import logo, greetings

if __name__ == '__main__':

    print(logo)
    print(greetings + "\n")

    proceed = "y"
    while proceed == "y":
        selection = input("Encrypt or decrypt a string? (e/d): ").lower()
        while selection != "e" and selection != "d":
            selection = input("Enter \"e\" for encrypting or \"d\" for decrypting: ").lower()

        convert_string = Convert()
        invalid_char = True
        while invalid_char:
            string = input(f"Type in a word or sentence to {convert_string.get_method(selection)}: ").lower()
            for char in string:
                if char not in convert_string.get_chart():
                    print(f"You typed in an invalid character: {char}")
                    break
            invalid_char = False

        print(f"{convert_string.get_method(selection)}ed string: ".capitalize(), end = "")
        if selection == "e":
            print(convert_string.encrypt(string))
        else:
            print(convert_string.decrypt(string))
        
        proceed = input("\nWould you like to convert another string? (y/n): ").lower()