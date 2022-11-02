from charts import generate_pie_chart
from charts import generate_bar_chart
from utils import csv_to_dict
from utils import get_country_data
from utils import get_population_by_country
from utils import get_world_percentages


if __name__ == '__main__':
    data = csv_to_dict('data/data.csv')

    colombia_data = get_country_data(data, 'Colombia')
    col_keys, col_values = get_population_by_country(colombia_data)

    w_keys, w_values = get_world_percentages(data)

    generate_bar_chart(col_keys, col_values)
    generate_pie_chart(col_keys, col_values)
