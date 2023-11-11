"""
Script to convert the data exported by mobills premium into Money Manager by Realbyte
"""

from lib.reader import read_mobills_transactions
from lib.writer import convert_to_money_manager


FILE = "../data.csv"
OUTPUT = "../output.xlsx"


def main() -> None:
    """
    Convert the data
    """
    transactions = read_mobills_transactions(FILE)
    convert_to_money_manager(transactions, OUTPUT)


if __name__ == "__main__":
    main()
