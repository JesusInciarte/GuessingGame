"""This module defines all the user-defined exceptions"""

class OperationCancelled(Exception):
    """Raised when the user cancels an interaction with the program."""
    pass

class InvalidRange(Exception):
    """Raised when the minimum guess is greater than the maximum guess."""
    pass









