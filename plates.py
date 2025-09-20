def main():
    plate = input("Plate: ")
    if is_valid(plate): # Verifies plate and returns boolean
        print("Valid")
    else:
        print("Invalid")

def is_valid(plate):
    # “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
    if not (2 <= len(plate) <= 6):
        return False

    # “All vanity plates must start with at least two letters.”
    if not plate[:2].isalpha(): # if all characters in the string are alphabetic
        return False

    # “No periods, spaces, or punctuation marks are allowed.”
    if not plate.isalnum(): # if all characters in the string are alphanumeric
        return False

    for index, char in enumerate(plate):
        if char.isdigit(): # if the character is a digit
            # “The first number used cannot be a ‘0’.”
            if char == '0':
                return False

            # “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable.”
            if not plate[index:].isdigit():
                return False

            return True

    return True

main()
