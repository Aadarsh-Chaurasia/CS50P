def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    #  may contain a maximum of 6 and a minimum of 2 characters.
    if len(s) > 6 or len(s) < 2:
        return False

    # All vanity plates must start with at least two letters
    if not s[0].isalpha() or not s[1].isalpha():
        return False

    # No periods, spaces, or punctuation marks are allowed.
    if not s.isalnum():
        return False

    # Numbers cannot be used in the middle of a plate; they must come at the end.
    for i in range(2, len(s)):
        if not s[i].isalpha():
            # The first number used cannot be a ‘0’.
            if s[i] == '0':
                return False
            for j in range(i, len(s)):
                if s[j].isalpha():
                    return False
            break
    return True


main()
