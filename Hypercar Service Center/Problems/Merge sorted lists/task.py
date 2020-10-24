def merge_arrays(a, b):
    # "c" will contain the result of merging arrays "a" and "b"
    c = []
    while a or b:
        if not b or (a and b and a[0] < b[0]):
            # removing the first element from "a" and adding it to "c"
            c.append(a[0])
            a.pop(0)
        else:
            # removing the first element from "b" and adding it to "c"
            c.append(b[0])
            b.pop(0)
    return c