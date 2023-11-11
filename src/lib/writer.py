"""
Module to convert the data to an excel
"""
import xlsxwriter

from model.mobills import MobillsTransaction


def _get_money_manager_header() -> list[str]:
    """
    Return the ordered columns of mobills
    """
    return [
        "Date",
        "Account",
        "Main Cat.",
        "Sub Cat.",
        "Contents",
        "Amount",
        "Inc./Exp.",
        "Details",
    ]


def convert_to_money_manager(
    transactions: list[MobillsTransaction], output: str
) -> None:
    """
    Write the converted transactions the transactions
    """
    # Create a workbook and add a worksheet.
    workbook = xlsxwriter.Workbook(output)
    worksheet = workbook.add_worksheet()

    row = 0
    for column, name in enumerate(_get_money_manager_header(), start=0):
        worksheet.write(row, column, name.strip())

    row += 1
    for transaction in transactions:
        values = [
            transaction.date.strftime(r"%m.%d.%Y"),
            transaction.account,
            transaction.category,
            transaction.subcategory,
            transaction.description,
            transaction.value,
            transaction.transaction_type.value,
            transaction.tags,
        ]
        for column, value in enumerate(values, start=0):
            if value is not None:
                if isinstance(value, str):
                    value.strip()
                worksheet.write(row, column, value)

        row += 1

    workbook.close()
