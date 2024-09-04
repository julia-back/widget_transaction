import pandas as pd


def reader_csv(file):
    """Считывание финансовых операций из CSV-файла. Возвращает список словарей с транзакциями"""
    transactions = pd.read_csv(file, delimiter=";")
    return transactions.to_dict(orient="records")


def reader_excel(file):
    """Считывание финансовых операций из XLSX-файла. Возвращает список словарей с транзакциями"""
    transactions = pd.read_excel(file)
    return transactions.to_dict(orient="records")
