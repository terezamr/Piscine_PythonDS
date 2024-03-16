import sys
import ft_filter
import re

# lambda function allows using the function with a different nb, according to the input
# returns True if the string size is larger than nb
def check_len(nb):
    return lambda str : len(str) > nb

# eliminates whitespaces, defines the function check_len to compare the size to the specific nb
# creates and prints the new list (using ft_filter)
def filterstring(str, nb):
    if len(str.strip()) == 0:
        raise AssertionError("Empty line")
    lst = re.split(r'\s+', str.strip())
    fc = check_len(int(nb))
    newlist = ft_filter.ft_filter(fc, lst)
    print(list(newlist))

def main():
    try:
        if len(sys.argv) != 3:
            raise AssertionError("Wrong number of arguments")

        # checks if the arguments are a string and an int
        try:
            arg1 = str(sys.argv[1])  # Convert to string
            arg2 = int(sys.argv[2])  # Convert to integer
        except:
            raise AssertionError("Wrong type of arguments: expected a string and a number")

        filterstring(sys.argv[1], sys.argv[2])
    except AssertionError as e:
        print("AssertionError: ", str(e))

if __name__ == "__main__":
    main()
