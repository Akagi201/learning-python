def my_max(a, b):
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return None


x = my_max(1, 2)

print x
print my_max(3, 2)
