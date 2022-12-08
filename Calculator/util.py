def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    if n2 == 0:
        return 'You cannot divide by 0'

    return n1 / n2


operations = {
    '+': add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
