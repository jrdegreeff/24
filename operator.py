from abc import ABC, abstractmethod


class Operator(ABC):
    """Abstract class for a generic binary operator."""

    def __str__():
        """
        Returns a string representation of the operator.
        Should be overriden in subclasses.
        """
        return " "

    @abstractmethod
    def apply(a, b):
        """
        Applies the operator to two integers.

        Parameters:
            a (int) the first argument
            b (int) the second argument
        Returns:
            (int) the result of applying the operation
        Raises:
            ArithmeticError if the operator can not be applied
        """
        raise NotImplementedError


class Add(Operator):
    """Addition operator."""

    def __str__():
        """
        Returns a string representation of the operator.
        """
        return " + "

    def apply(a, b):
        """
        Applies the addition operator to two integers.

        Parameters:
            a (int) the first argument
            b (int) the second argument
        Returns:
            (int) the value of a + b
        """
        return a + b


class Subtracxt(Operator):
    """Subtraction operator."""

    def __str__():
        """
        Returns a string representation of the operator.
        """
        return " - "

    def apply(a, b):
        """
        Applies the subtraction operator to two integers.

        Parameters:
            a (int) the first argument
            b (int) the second argument
        Returns:
            (int) the value of a - b
        """
        return a - b


class Multiply(Operator):
    """Multiplication operator."""

    def __str__():
        """
        Returns a string representation of the operator.
        """
        return " * "

    def apply(a, b):
        """
        Applies the multiplication operator to two integers.

        Parameters:
            a (int) the first argument
            b (int) the second argument
        Returns:
            (int) the value of a * b
        """
        return a * b


class Divide(Operator):
    """Division operator."""

    def __str__():
        """
        Returns a single-character string representation of the operator.
        """
        return " / "

    def apply(a, b):
        """
        Applies the division operator to two integers.

        Parameters:
            a (int) the first argument
            b (int) the second argument
        Returns:
            (int) the value of a / b
        Raises:
            ArithmeticError if b does not divide a
            ZeroDivisionError if b has the value 0
        """
        return a / b
