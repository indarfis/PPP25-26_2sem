from abc import ABC, abstractmethod


# КООРДИНАТЫ

def to_internal(pos):
    col = ord(pos[0]) - ord('a')
    row = 8 - int(pos[1])
    return row, col



# БАЗОВЫЙ КЛАСС

class Piece(ABC):
    def __init__(self, color, position):
        self.color = color
        self.position = position
        self.has_moved = False

    @abstractmethod
    def get_possible_moves(self, board):
        pass

    def move(self, position):
        self.position = position
        self.has_moved = True


# ФИГУРЫ

class Rook(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.symbol = "♜" if color == "white" else "♖"

    def get_possible_moves(self, board):
        moves = []
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        for dx, dy in directions:
            x, y = self.position
            while True:
                x += dx
                y += dy
                if not board.is_inside(x, y):
                    break
                if board.is_empty(x, y):
                    moves.append((x, y))
                else:
                    if board.get_piece(x, y).color != self.color:
                        moves.append((x, y))
                    break
        return moves


class Knight(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.symbol = "♞" if color == "white" else "♘"

    def get_possible_moves(self, board):
        moves = []
        steps = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)]

        for dx, dy in steps:
            x = self.position[0] + dx
            y = self.position[1] + dy

            if board.is_inside(x, y):
                if board.is_empty(x, y) or board.get_piece(x, y).color != self.color:
                    moves.append((x, y))
        return moves


class Bishop(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.symbol = "♝" if color == "white" else "♗"

    def get_possible_moves(self, board):
        moves = []
        directions = [(1,1),(1,-1),(-1,1),(-1,-1)]

        for dx, dy in directions:
            x, y = self.position
            while True:
                x += dx
                y += dy
                if not board.is_inside(x, y):
                    break
                if board.is_empty(x, y):
                    moves.append((x, y))
                else:
                    if board.get_piece(x, y).color != self.color:
                        moves.append((x, y))
                    break
        return moves


class Queen(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.symbol = "♛" if color == "white" else "♕"

    def get_possible_moves(self, board):
        return Rook.get_possible_moves(self, board) + \
               Bishop.get_possible_moves(self, board)


class King(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.symbol = "♚" if color == "white" else "♔"

    def get_possible_moves(self, board):
        moves = []
        steps = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

        for dx, dy in steps:
            x = self.position[0] + dx
            y = self.position[1] + dy

            if board.is_inside(x, y):
                if board.is_empty(x, y) or board.get_piece(x, y).color != self.color:
                    moves.append((x, y))
        return moves


class Pawn(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.symbol = "♟" if color == "white" else "♙"

    def get_possible_moves(self, board):
        moves = []
        x, y = self.position
        direction = -1 if self.color == "white" else 1

        if board.is_inside(x + direction, y) and board.is_empty(x + direction, y):
            moves.append((x + direction, y))

            if not self.has_moved and board.is_empty(x + 2*direction, y):
                moves.append((x + 2*direction, y))

        for dy in [-1, 1]:
            nx, ny = x + direction, y + dy
            if board.is_inside(nx, ny):
                if not board.is_empty(nx, ny):
                    if board.get_piece(nx, ny).color != self.color:
                        moves.append((nx, ny))

        return moves



# ДОСКА

class Board:
    def __init__(self):
        self.grid = [[None for _ in range(8)] for _ in range(8)]
        self.setup()

    def setup(self):
        for i in range(8):
            self.place_piece(Pawn("white", (6, i)))
            self.place_piece(Pawn("black", (1, i)))

        self.place_piece(Rook("white", (7, 0)))
        self.place_piece(Rook("white", (7, 7)))
        self.place_piece(Rook("black", (0, 0)))
        self.place_piece(Rook("black", (0, 7)))

        self.place_piece(Knight("white", (7, 1)))
        self.place_piece(Knight("white", (7, 6)))
        self.place_piece(Knight("black", (0, 1)))
        self.place_piece(Knight("black", (0, 6)))

        self.place_piece(Bishop("white", (7, 2)))
        self.place_piece(Bishop("white", (7, 5)))
        self.place_piece(Bishop("black", (0, 2)))
        self.place_piece(Bishop("black", (0, 5)))

        self.place_piece(Queen("white", (7, 3)))
        self.place_piece(Queen("black", (0, 3)))

        self.place_piece(King("white", (7, 4)))
        self.place_piece(King("black", (0, 4)))

    def place_piece(self, piece):
        x, y = piece.position
        self.grid[x][y] = piece

    def move_piece(self, piece, new_pos):
        x, y = piece.position
        nx, ny = new_pos

        self.grid[x][y] = None
        piece.move(new_pos)
        self.grid[nx][ny] = piece

    def get_piece(self, x, y):
        return self.grid[x][y]

    def is_empty(self, x, y):
        return self.grid[x][y] is None

    def is_inside(self, x, y):
        return 0 <= x < 8 and 0 <= y < 8

    def print_board(self):
        print("\n   a b c d e f g h")
        for i, row in enumerate(self.grid):
            print(8 - i, end="  ")
            for cell in row:
                print(cell.symbol if cell else "·", end=" ")
            print(" ", 8 - i)
        print("   a b c d e f g h")


# ХОД И ИГРА

class Move:
    def __init__(self, piece, start, end, captured):
        self.piece = piece
        self.start = start
        self.end = end
        self.captured = captured


class Game:
    def __init__(self):
        self.board = Board()
        self.turn = "white"
        self.history = []

    def make_move(self, start, end):
        x1, y1 = to_internal(start)
        x2, y2 = to_internal(end)

        piece = self.board.get_piece(x1, y1)

        if not piece:
            print("Нет фигуры!")
            return

        if piece.color != self.turn:
            print("Не ваш ход!")
            return

        moves = piece.get_possible_moves(self.board)

        if (x2, y2) not in moves:
            print("Недопустимый ход!")
            return

        captured = self.board.get_piece(x2, y2)
        self.history.append(Move(piece, (x1, y1), (x2, y2), captured))

        self.board.move_piece(piece, (x2, y2))
        self.turn = "black" if self.turn == "white" else "white"

    def undo(self):
        if not self.history:
            print("Нет ходов")
            return

        move = self.history.pop()
        self.board.move_piece(move.piece, move.start)

        if move.captured:
            self.board.place_piece(move.captured)

        self.turn = move.piece.color



# ЗАПУСК

def main():
    game = Game()

    while True:
        game.board.print_board()
        print(f"\nХод: {game.turn}")
        cmd = input("Введите ход (например: e2 e4) или отмена: ")

        if cmd == 'отмена':
            game.undo()
            continue

        try:
            start, end = cmd.split()
            game.make_move(start, end)
        except:
            print("Ошибка ввода!")


if __name__ == "__main__":
    main()
