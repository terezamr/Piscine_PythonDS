import sys

def is_int():
    nb = int(sys.argv[1])
    if nb % 2 == 0:
        print("I'm Even.\n")
    else:
        print("I'm Odd.\n")

num_arguments = len(sys.argv)
if len(sys.argv) == 1:
    print("")
else:
    try:
        if len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided\n")
        try:
            is_int()
        except ValueError:
            raise AssertionError("argument is not an integer\n")     
    except AssertionError as e:
        print("AssertationError:", str(e))
