BOARD_SIZE = 8
KNIGHT_MOVES = [
    (2, 1), (1, 2), (-1, 2), (-2, 1),
    (-2, -1), (-1, -2), (1, -2), (2, -1)
]

def is_move_valid(x, y, board):
    return (
        0 <= x < BOARD_SIZE and
        0 <= y < BOARD_SIZE and
        board[y][x] == -1
    )

def count_onward_moves(x, y, board):
    count = 0
    for dx, dy in KNIGHT_MOVES:
        nx, ny = x + dx, y + dy
        if is_move_valid(nx, ny, board):
            count += 1
    return count

def display_board(board):
    for row in board:
        print(' '.join(f'{cell:2}' for cell in row))
    print()

def try_knight_tour(x, y, step, board):
    if step == BOARD_SIZE * BOARD_SIZE:
        return True

    next_moves = []
    for dx, dy in KNIGHT_MOVES:
        nx, ny = x + dx, y + dy
        if is_move_valid(nx, ny, board):
            onward = count_onward_moves(nx, ny, board)
            next_moves.append(((nx, ny), onward))

    # Sort moves by Warnsdorff's heuristic (least onward moves first)
    next_moves.sort(key=lambda move: move[1])

    for (nx, ny), _ in next_moves:
        board[ny][nx] = step
        if try_knight_tour(nx, ny, step + 1, board):
            return True
        board[ny][nx] = -1  # Backtrack

    return False

def start_knight_tour():
    try:
        start_x = int(input("Введите X (0-7): "))
        start_y = int(input("Введите Y (0-7): "))
        if not (0 <= start_x < BOARD_SIZE and 0 <= start_y < BOARD_SIZE):
            raise ValueError
    except ValueError:
        print("Ошибка ввода. Введите координаты от 0 до 7.")
        return

    board = [[-1 for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
    board[start_y][start_x] = 0

    print(f"\nНачинаем тур с клетки ({start_x}, {start_y})...\n")

    if try_knight_tour(start_x, start_y, 1, board):
        print(" Путь найден!\n")
        display_board(board)
    else:
        print(" Путь не найден.")

start_knight_tour()
