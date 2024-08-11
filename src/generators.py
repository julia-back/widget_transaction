def filter_by_currency(transactions, code):
    filter_transactions = (t for t in transactions if t["operationAmount"]["currency"]["code"] == code)
    return filter_transactions
