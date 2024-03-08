def all_thing_is_obj(object: any) -> int:

    names = {list:"List", tuple:"Tuple", dict:"Dict", set:"Set"}
    tp = type(object)
    name = names.get(tp, "not found")

    if (isinstance(object, str)):
        print(object, "is in the kitchen:", type(object))
    elif (name != "not found"):
        print(name, ":", type(object))
    else:
        print("Type not found")
    return 42
