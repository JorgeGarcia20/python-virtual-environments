import csv


def csv_to_dict(path):
    data = []
    with open(path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        header = next(reader)
    
        for row in reader:
            iterable = zip(header, row)
            population_dict = {k: v for k, v in iterable}
            data.append(population_dict)
        return data


def get_country_data(data, country):
    return list(filter(lambda item: item['Country/Territory'] == country, data))


def get_population_by_country(data):
    population_dict = {
        '2022': int(data[0]['2022 Population']),
        '2020': int(data[0]['2020 Population']),
        '2015': int(data[0]['2015 Population']),
        '2010': int(data[0]['2010 Population']),
        '2000': int(data[0]['2000 Population']),
        '1990': int(data[0]['1990 Population']),
        '1980': int(data[0]['1980 Population']),
        '1970': int(data[0]['1970 Population'])
    }
    labels = population_dict.keys()
    values = population_dict.values()
    return labels, values


def get_world_percentages(data):
    percentages_dict = {item["Country/Territory"]: item["World Population Percentage"] for item in data}
    names = percentages_dict.keys()
    percentage = percentages_dict.values()
    return names, percentage

