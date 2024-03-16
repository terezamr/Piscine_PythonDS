import numpy as np

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    if (len(height) != len(weight)):
        return ''
    try:
        for x in height:
            i = int(x)
            f = float(x)
        for x in weight:
            i = int(x)
            f = float(x)
    except:
        return ''

    h = np.array(height)
    w = np.array(weight)

    bmi = w / (h ** 2)
    bmi_lst = bmi.tolist()
    return bmi_lst

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    bool_list = [x > limit for x in bmi]
    return bool_list
