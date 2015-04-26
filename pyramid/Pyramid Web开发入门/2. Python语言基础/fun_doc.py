def my_max(a, b):
    """return the maximum number

    Parameters a and b should both be integer"""

    if a > b:
        return a
    elif b > a:
        return b
    else:
        return None


print my_max(1, 5)
print my_max.__doc__

