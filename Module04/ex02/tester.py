from callLimit import callLimit

@callLimit(4)
def f(name):
    print("My name is")

@callLimit(2)
def g(age):
    print("My age is")

for i in range(20, 40, 5):
    f("maria")
    g(i)