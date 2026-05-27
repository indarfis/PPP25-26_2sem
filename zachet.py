def print_board(board):
    
    size = len(board)
    print("\n  " + " ".join(str(i + 1) for i in range(size)))
    for i in range(size):
        print(f"{i + 1} " + " ".join(board[i]))
    print()


def create_board(size):
    
    return [["." for _ in range(size)] for _ in range(size)]


def check_win(board, symbol):
    
    size = len(board)
    
    
    for i in range(size):
        row_win = all(board[i][j] == symbol for j in range(size))
        col_win = all(board[j][i] == symbol for j in range(size))
        if row_win or col_win:
            return True
    
    
    diag1_win = all(board[i][i] == symbol for i in range(size))
    if diag1_win:
        return True
    
    
    diag2_win = all(board[i][size - 1 - i] == symbol for i in range(size))
    if diag2_win:
        return True
    
    return False


def check_draw(board):
    
    return all(cell != "." for row in board for cell in row)


def is_valid_move(board, row, col):
    
    size = len(board)
    if row < 0 or row >= size or col < 0 or col >= size:
        return False
    if board[row][col] != ".":
        return False
    return True


def make_move(board, row, col, symbol):
    
    board[row][col] = symbol


def get_board_size():
    
    while True:
        try:
            size = int(input("Выберите размер поля (3 или 4): "))
            if size in [3, 4]:
                return size
            else:
                print("Ошибка! Выберите 3 или 4.")
        except ValueError:
            print("Ошибка! Введите число 3 или 4.")


def get_move(player_symbol):
    
    while True:
        try:
            move = input(f"Игрок {player_symbol}, введите координаты (строка столбец): ")
            parts = move.split()
            if len(parts) != 2:
                print("Ошибка! Введите два числа через пробел.")
                continue
            
            row = int(parts[0]) - 1
            col = int(parts[1]) - 1
            return row, col
        except ValueError:
            print("Ошибка! Введите целые числа.")


def play_game():
    
    # Выбор размера поля
    print("\n=== Новая игра ===")
    size = get_board_size()
    
    # Создание поля
    board = create_board(size)
    current_player = "X"
    game_over = False
    
    # Игровой цикл
    while not game_over:
        print_board(board)
        
        # Получение хода игрока
        row, col = get_move(current_player)
        
        # Проверка корректности хода
        if not is_valid_move(board, row, col):
            print("Ошибка! Клетка занята или координаты вне поля.")
            continue
        
        # Выполнение хода
        make_move(board, row, col, current_player)
        
        # Проверка победы
        if check_win(board, current_player):
            print_board(board)
            print(f"\n🎉 Игрок {current_player} победил! 🎉")
            game_over = True
            break
        
        # Проверка ничьей
        if check_draw(board):
            print_board(board)
            print("\n🤝 Ничья! 🤝")
            game_over = True
            break
        
        # Смена игрока
        current_player = "O" if current_player == "X" else "X"
    
    return game_over


def main():
    print("=" * 50)
    print("     Добро пожаловать в Крестики-нолики!")
    print("=" * 50)
    print("Команды:")
    print("  start - начать новую игру")
    print("  restart - начать игру заново (во время партии)")
    print("  exit - выйти из игры")
    print("=" * 50)
    
    game_in_progress = False
    
    while True:
        command = input("\nВведите команду: ").strip().lower()
        
        if command == "exit":
            print("Спасибо за игру! До свидания!")
            break
        
        elif command == "start":
            if game_in_progress:
                print("Игра уже идет! Используйте 'restart' для новой игры.")
                continue
            play_game()
            game_in_progress = False
        
        elif command == "restart":
            if not game_in_progress:
                print("Сначала начните игру командой 'start'.")
                continue
            print("\nПерезапуск игры...")
            play_game()
            game_in_progress = False
        
        else:
            print("Неизвестная команда. Доступные команды: start, restart, exit")


if __name__ == "__main__":
    main()