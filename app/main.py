import utils
import read_csv
import charts
import pandas as pd


def run():
    file_path = read_csv.file_path
    '''
    data = read_csv.read_csv(file_path)
    data = list(filter(lambda item: item['Continent'] == 'South America', data))

    countries = list(map(lambda x: x['Country'], data))
    percentages = list(map(lambda x: x['World Population Percentage'], data))
    '''

    df = pd.read_csv(file_path)
    df = df[df['Continent'] == 'South America']

    countries = df['Country'].values
    percentages = df['World Population Percentage'].values
    charts.generate_pie_chart(countries, percentages)
    
    data = read_csv.read_csv(file_path)
    country = input('Type Country => ')
    print(country)

    result = utils.population_by_country(data, country)
    if len(result) > 0:
        country_data = result[0]
        print(country_data)
        labels, values = utils.get_population(country_data)
        charts.generate_bar_chart(country, labels, values)

if __name__ == '__main__':
    run()
