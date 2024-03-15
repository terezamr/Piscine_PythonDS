import sys
import string

def check_st(st):
    total = len(st)
    upper = sum(1 for char in st if char.isupper())
    lower = sum(1 for char in st if char.islower())
    punctuation = sum(1 for char in st if char in string.punctuation)
    digits = sum(1 for char in st if char.isdigit())
    spaces = sum(1 for char in st if char.isspace())

    # Print results
    print("The text contains", total, "characters")
    print(upper,"upper letters")
    print(lower, "lower letters")
    print(punctuation, "punctuation marks")
    print(spaces, "spaces")
    print(digits, "digits")


# check ex subject com duas frases como input, so conta a ultima
def main():
    try:
        st = ""
        if len(sys.argv) > 2:
            raise AssertionError("more than one element provided")
        if len(sys.argv) == 1:
            #st = input("Please enter a string: ")
            while not st:
                st = input("Please enter a string: ")
        else:
            st = sys.argv[1]
        check_st(st)
    except AssertionError as e:
        print("AssertionError: ", str(e))

if __name__ == "__main__":
    main()
