# Python virtual environments
Curso de entornos virtuales en Python

## Pasos para ejecutar el juego Piedra Papel o Tijera.
Para poder ejecutar el juego sera necesario ejecutar el siguiente comando desde la raiz del repositorio:

Unix
```sh
cd game
python3 main.py
```

Windows
```sh
cd game
python main.py
```

## Creacion y configuracion del ambiente virtual para el directorio app
Para poder ejecutar el programa debes de ejecutar los siguientes comandos antes:

Unix
```sh
cd app
python3 -m venv evn
source env/bin/activate
pip3 install -r requirements.txt
python3 main.py
```

Windows
```sh
cd app
python -m venv evn
env\Scripts\activate
pip install -r requirements.txt
python main.py
```
