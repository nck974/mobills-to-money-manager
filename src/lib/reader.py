"""
Module to read data
"""


import csv
from datetime import datetime
from model.mobills import MobillsTransaction
from model.transaction import TransactionType


def read_mobills_transactions(file: str) -> list[MobillsTransaction]:
    """
    Read the transactions
    """
    transactions: list[MobillsTransaction] = []
    with open(file, mode="r", encoding="utf16") as f:
        reader = csv.DictReader(f, delimiter=";")
        for line in reader:
            date = datetime.strptime(line["Date"], "%d/%m/%Y")
            description = line["Description"]
            value = line["Value"]
            account = line["Account"]
            category = line["Category"]
            subcategory = line["Subcategory"]
            tags = line["Tags"]
            transaction_type = (
                TransactionType.INCOME if float(value) > 0 else TransactionType.EXPENSE
            )

            transactions.append(
                MobillsTransaction(
                    transaction_type=transaction_type,
                    date=date,
                    description=description,
                    value=abs(float(value)),
                    category=category,
                    subcategory=subcategory,
                    tags=tags,
                    account=account,
                )
            )

    return transactions
