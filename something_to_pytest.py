from collections import OrderedDict
import csv

# port file
def write_porfolio(filename):
    """
    write data to a CSV file
    """

    field_names = ['symbol', 'units', 'cost']
    field_data = [{'symbol': 'APPL',
                   'units': '100',
                   'cost': '154.23',
                   }, {'symbol': 'AMZN', 'units': '600', 'cost': '1223.43'}]

    with open(filename, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(field_data)

def read_portfolio(filename):
    """
    Returns data from a CSV file
    """
    with open(filename) as csvfile:
        csv_reader = csv.DictReader(csvfile)
        portfoio = []
        for record in csv_reader:
            portfoio.append(OrderedDict(record))

    return portfoio

if __name__ == "__main__":
    filename = "trading.csv"
    write_porfolio(filename)
    portfolio = read_portfolio(filename)
    print(portfolio)
