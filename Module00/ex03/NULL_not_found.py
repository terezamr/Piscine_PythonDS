import types
import math

def NULL_not_found(object: any) -> int:
    type_names = {float:"Cheese", int:"Zero", str:"Empty", bool:"Fake"}

    tp = type(object)
    if tp == types.NoneType:
        name = "Nothing"
    else:
        name = type_names.get(tp, "notfound")
    
    if tp == float and math.isnan(object):
        print(name, ":", object, tp)
        return 0
    elif name != "notfound" and not object:
        print(name, ":", object, tp)
        return 0
    else:
        print("Type not found")
        return 1