import requests


def get_categories():
    # r = requests.get('https://api.escuelajs.co/api/v1/categories')
    r = requests.get('http://127.0.0.1:8000/')
    print(r.status_code)
    # print(r.text)
    categories = r.json()
    print(categories)
    # print(type(categories))
    # print(categories['name'])

    # for category in categories:
    #     print(category['name'])