import sys 

def isEven(x):
    if x % 2 == 0:
        return True
    else:
        return False
    
def isOdd(x):
    if x % 2 == 0:
        return False
    else:
        return True

# returns a generator object that yields elements of the list one by one when iterated over.
def return_iterator(my_list):
    for item in my_list:
        yield item

#missing: iterator, case when function is none
def ft_filter(myFunc, lst):
    """
filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    try:
        newlist = [x for x in lst if myFunc(x)]
        return return_iterator(newlist)
    except:
        print("Error")    

def main():
    lst = [11, 21, 32, 84, 5, 92]
    lst1 = ft_filter(isEven, lst)
    print(next(lst1))

    if lst1:
        print(list(lst1))
    lst0 = filter(isEven, lst)
    if lst0:
        print(list(lst0))
    
    print("----")
    print(filter.__doc__)
    print("----")
    print(ft_filter.__doc__)
if __name__ == "__main__":
    main()
