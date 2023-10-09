#!/usr/bin/python3
"""To write a class MyInt that inherits from int"""


class MyInt(int):
    """
    To define MyInt as a rebel.
    MyInt has == and != operators inverted
    """
    def __eq__(self, other):
        """Override == opeartor with != behavior."""
        return (super().__ne__(other))

    def __ne__(self, other):
        """Override != operator with == behavior."""
        return (super().__eq__(other))
