import itertools as it
import operators as op
from pprint import pprint
import random


class Board():
    """Represtents a collection of cards for the 24 game."""

    def __init__(self, deck=[x for x in range(1, 14)] * 4, size=4, target=24):
        """
        Initializes the board with a random list of cards.

        Parameters:
            deck (list) all the cards which could be used
            size (int) the number of cards to use
            target (int) the target number
        """
        self.cards = random.sample(list(deck), size)
        self.target = target

    def solve(self, operators={op.Add(), op.Subtract(), op.Multiply(), op.Divide()}):
        """
        Generates a list of solutions for the board if solutions exist.

        Parameters:
            operators (set) collection of available operators
        Returns:
            (list) all solutions for the board
        Raises:
            TypeError if any of the passed operators is not an instance
                      of operators.Operator
        """
        for operator in operators:
            if not isinstance(operator, op.Operator):
                raise TypeError
        parses = self.parse(self.cards, operators)
        return list(filter(lambda p: parses[p] == self.target, parses.keys()))

    def parse(self, operands, operators):
        """
        Generates all ways to apply the specified operators on the cards.

        Parameters:
            operands (list) collection of available operands
            operators (set) collection of available operators
        Returns:
            (dict) mapping of all possible applications of operators on the
                   operands to their value
        """
        def helper(operands, operators):
            if len(operands) <= 1:
                return operands
            parses = []
            for p in it.permutations(range(len(operands)), 2):  # Each pair of distinct indices.
                remaining = [x for i, x in enumerate(operands) if i not in p]
                for o in operators:
                    if not o.is_commutative() or p[0] < p[1]:  # Avoid redundancy of commutative operators.
                        parses += helper(remaining + [op.Operator_Tree(o, operands[p[0]], operands[p[1]])], operators)
            return parses

        result = {}
        for parse in helper(operands, operators):
            try:
                result[parse] = parse.eval()
            except ArithmeticError:  # Discard any parse with an invalid operation.
                continue
            except AttributeError:  # Edge case: singleton operand.
                result[parse] = parse
        return result


if __name__ == '__main__':
    result = Board().solve()
    print(len(result), "Solutions:")
    pprint(result)
