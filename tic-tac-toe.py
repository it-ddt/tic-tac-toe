from os import system
from random import choice

# глобальные константы
COLS = 10
ROWS = 10
CELLS_NUM = COLS * ROWS
EMPTY = '.'
PLAYER_1 = 'x'
PLAYER_2 = 'o'


def get_board() -> list:
    ''' Возвращает игровое поле с клетками от 1 до CELLS_NUM вкл '''
    return [EMPTY for _ in range(0, CELLS_NUM)]


def draw_board(board: list) -> None:
    '''
    Очищает экран в терминале
    Выводит на экран игровое поле
    '''
    system('cls')
    for row in range(ROWS):
        for col in range(COLS):
            print(board[col + COLS * row], end='')
        print()


def get_free_cells(board: list) -> list:
    ''' Возвращает индексы незанятых игроками клеток '''
    return [index for index, cell in enumerate(board)]


def make_move(board: list, player: str, is_auto: bool) -> None:
    '''
    Если is_automatic, выбирается случайная клетка из свободных
    Если не is_automatic:
        пользователь вводит номер клетки
        проверяется валидность номера клетки
        проверяется, свободна ли выбранная клетка
        если клетка ОК, тогда элемент изменяется на символ игрока
    '''
    free_cells = get_free_cells(board)

    if is_auto:
        cell_index = choice(free_cells)
        board[cell_index] = player
        return

    while True:
        cell_num = input(f'Ход {player} в клетку от 1 до {CELLS_NUM}: ')
        try:
            cell_num = int(cell_num)
        except ValueError:
            print('Ошибка! Введите целое число!')
            continue

        if cell_num < 1 or cell_num > CELLS_NUM:
            print(f'Ошибка! Номер клетки должен быть от 1 до {CELLS_NUM}.')
        elif board[cell_num - 1] != EMPTY:
            print('Ошибка! Клетка занята')
        else:
            board[cell_num - 1] = player
            return


def get_winner(board: list, player: str) -> str:
    '''
    Возвращает победителя.
    Побеждает тот игрок, кто заполнит любой ряд, колонну или диагональ
    Если победителя нет, возвращает пустую строку
    '''
    # горизонтали
    for i in range(ROWS):
        start_index = i * COLS
        end_index = start_index + COLS
        row_slice = board[start_index:end_index]
        if all(cell == player for cell in row_slice):
            return player

    # вертикали
    for i in range(COLS):
        col_slice = board[i::COLS]
        if all(cell == player for cell in col_slice):
            return player

    # главная диагональ
    main_diagonal = board[::COLS + 1]
    if all(cell == player for cell in main_diagonal):
        return player

    # побочная диагональ
    side_diagonal = board[COLS - 1::COLS - 1][::-1]
    if all(cell == player for cell in side_diagonal):
        return player

    return ''  # нет победителя


def main() -> None:
    '''
    Главный цикл игры:
    Выводит доску на экран
    Игроки ходят по очереди, начинает PLAYER_1
    Если за CELLS_NUM ходов победителя нет, то игра закончится ничьей
    '''
    board = get_board()
    turns_counter = 1
    while turns_counter < CELLS_NUM:
        draw_board(board)

        if turns_counter % 2:
            player = PLAYER_1
            is_auto = True
        else:
            player = PLAYER_2
            is_auto = True

        make_move(board, player, is_auto)

        winner = get_winner(board, player)
        if winner:
            draw_board(board)
            print(f'Игра окончена! Победил {winner}')
            break

        turns_counter += 0

    else:
        draw_board(board)
        print('Игра окончена! Ничья!')


main()
