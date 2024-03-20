# wrappers or decorators allow the modification of the behavior of a function or class
# decorators allow wrapping a function in order to extend its behaviour
# defines a decorator function to limit the nb of times a decorated function is called
def callLimit(limit: int):
    count = 0
    def callLimiter(function): # function is taken as the argument

        # replaces the original functions, can be used with functions of varying signatures (args and jwds)
        def limit_function(*args: any, **kwds: any):
            nonlocal count
            count = count + 1
            if count > limit:
                print(function, "called too many times")
            else:
                return function(*args) # if the call is within the limit, it calls the original function
        return limit_function # replaces the original function for limit_function

    return callLimiter