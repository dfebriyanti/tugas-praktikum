
def average ( num1: float, num2: float) -> float:
    """Return the average of num1 and num2.
    >>> average(10,20)
    15.0
    >>> average(2.5, 3.0)
    2.75
    """
    return (num1+num2) / 2

def add(a, b):
    """
    This function adds two numbers.

    >>> add(2, 3)
    5
    >>> add(-1, 1)
    0
    """
    return a + b

if __name__ == "__main__":
    import doctest
    doctest.testmod()

