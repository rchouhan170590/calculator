def add(x: float, y: float) -> float:
    """
    Add two numbers.

    Args:
        x (float): The first number.
        y (float): The second number.

    Returns:
        float: The sum of x and y.
    """
    return x + y

def subtract(x: float, y: float) -> float:
    """
    Subtract one number from another.

    Args:
        x (float): The number to subtract from.
        y (float): The number to subtract.

    Returns:
        float: The result of subtracting y from x.
    """
    return x - y

def multiply(x: float, y: float) -> float:
    """
    Multiply two numbers.

    Args:
        x (float): The first number.
        y (float): The second number.

    Returns:
        float: The product of x and y.
    """
    return x * y

def divide(x: float, y: float) -> float:
    """
    Divide one number by another.

    Args:
        x (float): The dividend.
        y (float): The divisor.

    Returns:
        float: The result of dividing x by y.
    
    Raises:
        ValueError: If y is zero.
    """
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y
