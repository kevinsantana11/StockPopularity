import csv
from pathlib import Path

def get_common_stocks():
    stocks = []

    nyse = get_company_symbols('NYSE')
    nasdaq = get_company_symbols('NASDAQ')

    stocks.extend(nyse)
    stocks.extend(nasdaq)
    stocks.sort()

    return stocks

def get_company_symbols(exchange):
    company_symbols = []

    with open(f'./data/files/{exchange}.txt', encoding = 'utf-8') as csvfile:
        readCSV = csv.reader(csvfile, delimiter='\t')

        for row in readCSV:
            company_symbols.append(row[0])

    return company_symbols

def write_to_file(file_name, collection):
    file_exist = Path(file_name).exists()

    with open(file_name, 'a', newline = '', encoding = 'utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames = collection[0].__dict__.keys())

        if not file_exist:
            writer.writeheader()

        writer.writerows([item.__dict__ for item in collection])

if __name__ == "__main__":
    stocks = get_common_stocks()
    print(stocks)