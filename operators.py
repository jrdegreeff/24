from abc import ABC, abstractmethod


class Operator(ABC):
    """Abstract class for a generic binary operator."""

    def __repr__(self):
        """
        Returns a string representation of the operator.
        Should be overriden in subclasses.
        """
        return " "

    @abstractmethod
    def apply(self, a, b):
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
        pass

    def is_commutative(self):
        """
        Flag for commutativity to cut down on redundant permuatations.
        Any commuatative operator should override this method.

        Returns:
            (bool) True if the operator is commutative, False otherwise
        """
        return False


class Add(Operator):
    """Addition operator."""

    def __repr__(self):
        """
        Returns a string representation of the operator.
        """
        return " + "

    def apply(self, a, b):
        """
        Applies the addition operator to two integers.

        Parameters:
            a (int) the first argument
            b (int) the second argument
        Returns:
            (int) the value of a + b
        """
        return a + b

    def is_commutative(self):
        """
        Flag for commutativity to cut down on redundant permuatations.

        Returns:
            (bool) True
        """
        return True


class Subtract(Operator):
    """Subtraction operator."""

    def __repr__(self):
        """
        Returns a string representation of the operator.
        """
        return " - "

    def apply(self, a, b):
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

    def __repr__(self):
        """
        Returns a string representation of the operator.
        """
        return " * "

    def apply(self, a, b):
        """
        Applies the multiplication operator to two integers.

        Parameters:
            a (int) the first argument
            b (int) the second argument
        Returns:
            (int) the value of a * b
        """
        return a * b

    def is_commutative(self):
        """
        Flag for commutativity to cut down on redundant permuatations.

        Returns:
            (bool) True
        """
        return True


class Divide(Operator):
    """Division operator."""

    def __repr__(self):
        """
        Returns a string representation of the operator.
        """
        return " / "

    def apply(self, a, b):
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
        if b == 0:
            raise ZeroDivisionError
        if a % b != 0:
            raise ArithmeticError
        return int(a / b)


class Operator_Tree():
    """Represents a binary tree of operators and operands."""

    def __init__(self, operator, branch1, branch2):
        """
        Inializes the root of the tree with an operator and two branches.

        Parameters:
            operator (Operator) the root operator
            branch1 (Operator_Tree|int) the left branch
            branch2 (Operator_Tree|int) the right branch
        """
        self.operator = operator
        self.branch1 = branch1
        self.branch2 = branch2

    def __repr__(self):
        """Returns a string representation of the operator tree."""
        return f"({repr(self.branch1)}{repr(self.operator)}{repr(self.branch2)})"

    def eval(self):
        """
        Evaluates the operator tree.

        Returns:
            int the value of the tree
        Raises:
            ArithmeticError if any operation in the tree cannot be applied
        """
        return self.operator.apply(self.branch1 if isinstance(self.branch1, int) else self.branch1.eval(), self.branch2 if isinstance(self.branch2, int) else self.branch2.eval())
