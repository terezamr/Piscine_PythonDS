
def square(x: int | float) -> int | float:
    return (x * x)

def pow(x: int | float) -> int | float:
    return (x ** x)

def outer(x: int | float, function) -> object:
    count = 0
    def inner() -> float: # runned everytime the object is called
        nonlocal count # variable does not belong to the inner function
        count = count + 1 # iterates count everytime the object is called
        result = x
        i = 0
        while i < count:
            result = function(result)
            i = i + 1
        return result
    return inner