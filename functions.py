def factorial(n):
    if n <= 0:
        return False
    factorial = 1
    for x in range(2, n + 1):
        factorial *= x
    return factorial


def sqrt(x):
    if x <= 0:
        return False
    else:
        return int(x ** 0.5)


def is_square(x):
    y = sqrt(x)
    return y * y == x


def is_prime(x):
    if x <= 1 or x % 2 == 0:
        return False
    elif x <= 3:
        return True
    else:
        for i in range(3, sqrt(x) + 1, 2):
            if x % i == 0:
                return False
        return True
