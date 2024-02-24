from .operations import add, subtract, multiply, divide

class Calculator:
    """A simple calculator class."""

    def __init__(self):
        """Initialize the Calculator object."""
        pass

    def add(self, x: float, y: float) -> float:
        """
        Add two numbers.

        Args:
            x (float): The first number.
            y (float): The second number.

        Returns:
            float: The sum of x and y.
        """
        return add(x, y)

    def subtract(self, x: float, y: float) -> float:
        """
        Subtract one number from another.

        Args:
            x (float): The number to subtract from.
            y (float): The number to subtract.

        Returns:
            float: The result of subtracting y from x.
        """
        return subtract(x, y)

    def multiply(self, x: float, y: float) -> float:
        """
        Multiply two numbers.

        Args:
            x (float): The first number.
            y (float): The second number.

        Returns:
            float: The product of x and y.
        """
        return multiply(x, y)

    def divide(self, x: float, y: float) -> float:
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
        return divide(x, y)
