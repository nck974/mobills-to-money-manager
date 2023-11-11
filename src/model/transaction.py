"""
Types of transaction
"""
from enum import Enum


class TransactionType(Enum):
    """
    Representation of a transaction type based on the amount
    """

    INCOME = "Income"
    EXPENSE = "Expense"
