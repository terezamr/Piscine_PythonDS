import numpy as np

def slice_me(family: list, start: int, end: int) -> list:
    
    try:
        if not isinstance(family, list) or not isinstance(start, int) or not isinstance(end, int):
            raise ValueError("Input must be a list")

        if not all (isinstance(y, list) for y in family):
            raise ValueError("Input must be a list of lists")

        sizes = set(len(x) for x in family)
        if len(sizes) != 1:
            raise ValueError("Elements should have the same size")

        arr = np.array(family)
        rows, cols = arr.shape
        print(f"My shape is: ({rows}, {cols})")
        new_arr = arr[start:end]
        rows1, cols1 = new_arr.shape
        print(f"My new shape is: ({rows1}, {cols1})")
        return new_arr.tolist()

    except ValueError as e:
        print("Error", e)
        return ''