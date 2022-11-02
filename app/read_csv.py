import csv
from pathlib import Path


main_path = Path('.')
file_path = main_path / 'data' / 'data.csv'


def read_csv(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        data = []
        for row in reader:
            iterable = zip(header, row)
            country_dict = {k: v for k, v in iterable}
            data.append(country_dict)
        return data


if __name__ == '__main__':

    data = read_csv(file_path)
    print(data[0])
