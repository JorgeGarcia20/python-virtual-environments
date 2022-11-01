import random
import sys


options = ('piedra', 'papel', 'tijera')


def get_computer_move():
    """Funcion para obtener la eleccion del computador

    Returns:
        str: retorna piedra, papel o tijera
    """
    return random.choice(options)


def get_user_move():
    """Función para obtener la elección del usuario

    Returns:
        str: retorna el input del usuario ya sea piedra, papel o tijera.
    """
    user_move = input('piedra, papel o tijeras => ')
    return user_move.lower()


def is_correct_move(user_move):
    """Función para verificar si el input del usuario es correcto. 

    Args:
        user_move (str): piedra, papel o tijera.

    Returns:
        bool: si el usuario ingreso alguna de las opciones correctas entonces se retornara True.
    """
    return user_move in options


def check_rules(user_move, computer_move, user_wins, computer_wins):
    """Funcion que comprueba los movimientos del usuario y de la computadora y suma 1 al ganador

    Args:
        user_move (srt): movimiento del usuario
        computer_move (srt): movimiento del computador
        user_wins (int): Número de veces que el usuario gana
        computer_wins (int): Número de veces que el computador gana

    Returns:
        int, int: Retorna el numero de veces ganadas del usuario y de la computadora.
    """
    
    PIEDRA_TIJERA = 'Piedra gana a Tijera'
    PAPEL_PIEDRA = 'Papel gana a Piedra'
    TIJERA_PAPEL = 'Tijera gana a Papel'
    
    USER_WIN = 'El usuario gana esta ronda!'
    COMPUTER_WIN = 'El computador gana esta ronda!'

    if user_move == computer_move:
        print('Empate!')

    elif user_move == 'piedra':
        if computer_move == 'tijera':
            print(PIEDRA_TIJERA)
            print(USER_WIN)
            user_wins += 1
        else:
            print(PAPEL_PIEDRA)
            print(COMPUTER_WIN)
            computer_wins += 1
    elif user_move == 'papel':
        if computer_move == 'piedra':
            print(PAPEL_PIEDRA)
            print(USER_WIN)
            user_wins += 1
        else:
            print(PIEDRA_TIJERA)
            print(COMPUTER_WIN)
            computer_wins += 1
    elif user_move == 'tijera':
        if computer_move == 'papel':
            print(TIJERA_PAPEL)
            print(USER_WIN)
            user_wins += 1
        else:
            print(PIEDRA_TIJERA)
            print(COMPUTER_WIN)
            computer_wins += 1
    return user_wins, computer_wins


def check_winer(user_wins, computer_wins):
    """Funcion que recibe el numero de rondas ganadas del usuario y del computador

    Args:
        user_wins (int): Rondas ganadas por el usuario
        computer_wins (int): Rondas ganadas por el computador
    """
    if user_wins == 2:
        sys.exit('El usuario gana el juego!')
    elif computer_wins == 2:
        sys.exit('El computador gana el juego!')


def run_game():
    """Funcion que ejecuta el buble del juego.
    """ 
    user_wins = 0
    computer_wins = 0
    rounds = 1

    while True:

        print('*' * 10)
        print('ROUND', rounds)
        print('*' * 10)

        print('computer_wins', computer_wins)
        print('user_wins', user_wins)

        computer_move = get_computer_move()
        user_move = get_user_move()

        rounds += 1

        if not is_correct_move(user_move):
            print('esa opcion no es valida')
            continue

        print('User option =>', user_move)
        print('Computer option =>', computer_move)

        user_wins, computer_wins = check_rules(user_move, computer_move, user_wins, computer_wins)

        check_winer(user_wins, computer_wins)            

run_game()
