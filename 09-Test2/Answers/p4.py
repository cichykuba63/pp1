def f(dictionary, x, y):
    sum = 0

    for value in dictionary.values():
        for element in value:
            if element == x or element == y:
                sum += element

    return sum
