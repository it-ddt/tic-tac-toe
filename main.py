from os import system
from random import choice

# глобальные константы
PLAYER_1 = 'x'
PLAYER_2 = 'o'
PLAYERS = (PLAYER_1, PLAYER_2)


def get_board() -> list:
    ''' Возвращает игровое поле с клетками от 1 до 9 вкл '''
    return list(range(1, 10))


def draw_board(board: list) -> None:
    '''
    Очищает экран в терминале
    Выводит на экран игровое поле по 3 клетки в ряд
    '''
    system('cls')
    for i in range(3):
        print(board[i * 3], board[i * 3 + 1], board[i * 3 + 2])


def get_free_cells(board: list) -> list:
    ''' Возвращает индексы незанятых игроками клеток '''
    return [index for index, cell in enumerate(board)]


def make_move(board: list, player: str, is_auto: bool) -> None:
    '''
    Если is_automatic, выбирается случайная клетка из свободных
    Если не is_automatic:
        пользователь вводит номер клетки
        проверяется валидность номера клетки - целое число от 1 до 9 вкл
        проверяется, свободна ли выбранная клетка
        если клетка ОК, тогда элемент изменяется на символ игрока
    '''
    free_cells = get_free_cells(board)

    if is_auto:
        cell_index = choice(free_cells)
        board[cell_index] = player
        return

    while True:
        cell_num = input(f'Введите номер клетки (1-9) для {player}: ')
        try:
            cell_num = int(cell_num)
        except ValueError:
            print('Ошибка! Введите целое число!')
            continue

        if cell_num < 1 or cell_num > 9:
            print('Ошибка! Номер клетки должен быть от 1 до 9.')
        elif board[cell_num - 1] in PLAYERS:
            print('Ошибка! Клетка занята')
        else:
            board[cell_num - 1] = player
            return


def get_winner(board: list, player: str) -> str:
    '''
    Возвращает победителя.
    Побеждает тот, кто заполнит три клетки подряд
    по горизонтали, веритикали или диагонали.
    Если победителя нет, возвращает пустую строку
    '''
    # горизонтали
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] == player:
            return player

    # вертикали
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] == player:
            return player

    # диагонали
    if (
        board[0] == board[4] == board[8] == player or
        board[2] == board[4] == board[6] == player
    ):
        return player

    return ''  # нет победителя


def main() -> None:
    '''
    Главный цикл игры:
    Выводит доску на экран
    Игроки ходят по очереди, начинает PLAYER_1
    Если за 9 ходов победителя нет, то игра закончится ничьей
    '''
    board = get_board()
    turns_counter = 1
    while turns_counter < len(board) + 1:
        draw_board(board)

        if turns_counter % 2:
            player = PLAYER_1
            is_auto = False
        else:
            player = PLAYER_2
            is_auto = True

        make_move(board, player, is_auto)

        winner = get_winner(board, player)
        if winner:
            draw_board(board)
            print(f'Игра окончена! Победил {winner}')
            break

        turns_counter += 1

    else:
        draw_board(board)
        print('Игра окончена! Ничья!')


main()
