def add(*args):
    result = 0
    for arg in args:
        result += arg
    return result

print(add(1, 2, 3))