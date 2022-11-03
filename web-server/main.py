import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI()


@app.get('/')
def get_list():
    return [
        {
            'name': 'Jorge',
            'last_name': 'Garcia',
            'age': 23,
            'email': 'jorge@something.com'
        },
        {
            'name': 'Alberto',
            'last_name': 'Estrada',
            'age': 24,
            'email': 'albert-estrada@something.com'
        },
        {
            'name': 'Maria',
            'last_name': 'Iniesta',
            'age': 20,
            'email': 'mary-I@something.com'
        }
    ]


@app.get('/contact/', response_class=HTMLResponse)
def get_contact():
    return """
        <h1>Respuesta HTML desde FastAPI</h1>
        <h2>Elaborado por Jorge Garcia <3</h2>
        <p>Esto es un párrafo</p>
    """


def run():
    store.get_categories()


if __name__ == '__main__':
    run()