# Module of function related to numbers

def iseven(n):
    """
    Returns true if the given number is even otherwise false
    n : Number to test
    """
    return n % 2 == 0


def ispositive(n):
    return n > 0


if __name__ == '__main__':
    print("Executing number_funs module!")
else:
    print("Importing module!")
