import tkinter as tk


class ChessGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Tkinter Chess")
        self.root.resizable(False, False)

        self.size = 8
        self.square_size = 70
        self.board = self.create_initial_board()
        self.selected = None
        self.legal_moves = []
        self.turn = "white"

        self.canvas = tk.Canvas(root, width=self.square_size * self.size,
                                height=self.square_size * self.size + 60, bg="#f2e8c9")
        self.canvas.pack()

        self.status_var = tk.StringVar(value="White to move")
        tk.Label(root, textvariable=self.status_var, font=("Segoe UI", 12), pady=6).pack()

        self.canvas.bind("<Button-1>", self.on_click)
        self.draw_board()

    def create_initial_board(self):
        return [
            ["r", "n", "b", "q", "k", "b", "n", "r"],
            ["p", "p", "p", "p", "p", "p", "p", "p"],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            ["R", "N", "B", "Q", "K", "B", "N", "R"],
        ]

    def draw_board(self):
        self.canvas.delete("all")

        for row in range(self.size):
            for col in range(self.size):
                x1 = col * self.square_size
                y1 = row * self.square_size
                x2 = x1 + self.square_size
                y2 = y1 + self.square_size

                color = "#f0d9b5" if (row + col) % 2 == 0 else "#b58863"
                if (row, col) == self.selected:
                    color = "#7cb342"
                elif (row, col) in self.legal_moves:
                    color = "#8bc34a"

                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="#3e3e3e")
                self.canvas.create_text(x1 + self.square_size // 2, y1 + self.square_size // 2,
                                        text=self.piece_symbol(self.board[row][col]),
                                        font=("Segoe UI Symbol", 28), fill=self.piece_color(self.board[row][col]))

        self.canvas.create_text(self.square_size * 4, self.square_size * 8 + 25,
                                text=self.status_var.get(), font=("Segoe UI", 12))

    def on_click(self, event):
        col = event.x // self.square_size
        row = event.y // self.square_size

        if not (0 <= row < self.size and 0 <= col < self.size):
            return

        piece = self.board[row][col]

        if self.selected is None:
            if piece is not None and self.piece_color(piece) == self.turn:
                self.selected = (row, col)
                self.legal_moves = self.get_legal_moves(row, col)
                self.status_var.set(f"{self.turn.title()} selected a piece")
                self.draw_board()
            else:
                self.status_var.set("Select your own piece")
        else:
            if (row, col) == self.selected:
                self.selected = None
                self.legal_moves = []
                self.draw_board()
                return

            if (row, col) in self.legal_moves:
                self.make_move(self.selected, (row, col))
            else:
                if piece is not None and self.piece_color(piece) == self.turn:
                    self.selected = (row, col)
                    self.legal_moves = self.get_legal_moves(row, col)
                    self.status_var.set(f"{self.turn.title()} selected a piece")
                    self.draw_board()
                else:
                    self.selected = None
                    self.legal_moves = []
                    self.status_var.set("Illegal move")
                    self.draw_board()

    def make_move(self, start, end):
        piece = self.board[start[0]][start[1]]
        self.board[end[0]][end[1]] = piece
        self.board[start[0]][start[1]] = None

        if piece == "P" and end[0] == 0:
            self.board[end[0]][end[1]] = "Q"
        elif piece == "p" and end[0] == 7:
            self.board[end[0]][end[1]] = "q"

        self.selected = None
        self.legal_moves = []
        self.turn = "black" if self.turn == "white" else "white"
        self.status_var.set(f"{'White' if self.turn == 'white' else 'Black'} to move")
        self.draw_board()

    def piece_symbol(self, piece):
        symbols = {
            "P": "♙",
            "N": "♘",
            "B": "♗",
            "R": "♖",
            "Q": "♕",
            "K": "♔",
            "p": "♟",
            "n": "♞",
            "b": "♝",
            "r": "♜",
            "q": "♛",
            "k": "♚",
        }
        return symbols.get(piece, "") if piece is not None else ""

    def piece_color(self, piece):
        if piece is None:
            return ""
        return "white" if piece.isupper() else "black"

    def get_legal_moves(self, row, col):
        piece = self.board[row][col]
        if piece is None:
            return []

        moves = []
        piece_type = piece.upper()

        if piece_type == "P":
            direction = -1 if piece.isupper() else 1
            start_row = 6 if piece.isupper() else 1
            forward_row = row + direction
            if self.in_bounds(forward_row, col) and self.board[forward_row][col] is None:
                moves.append((forward_row, col))
                if row == start_row and self.board[row + 2 * direction][col] is None:
                    moves.append((row + 2 * direction, col))
            for dc in (-1, 1):
                new_col = col + dc
                if self.in_bounds(forward_row, new_col):
                    target = self.board[forward_row][new_col]
                    if target is not None and self.piece_color(target) != self.turn:
                        moves.append((forward_row, new_col))

        elif piece_type == "N":
            for dr, dc in [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]:
                new_row, new_col = row + dr, col + dc
                if self.in_bounds(new_row, new_col):
                    target = self.board[new_row][new_col]
                    if target is None or self.piece_color(target) != self.turn:
                        moves.append((new_row, new_col))

        elif piece_type in {"B", "R", "Q"}:
            directions = []
            if piece_type in {"B", "Q"}:
                directions.extend([(-1, -1), (-1, 1), (1, -1), (1, 1)])
            if piece_type in {"R", "Q"}:
                directions.extend([(-1, 0), (1, 0), (0, -1), (0, 1)])
            for dr, dc in directions:
                r, c = row + dr, col + dc
                while self.in_bounds(r, c):
                    target = self.board[r][c]
                    if target is None:
                        moves.append((r, c))
                    else:
                        if self.piece_color(target) != self.turn:
                            moves.append((r, c))
                        break
                    r += dr
                    c += dc

        elif piece_type == "K":
            for dr in range(-1, 2):
                for dc in range(-1, 2):
                    if dr == 0 and dc == 0:
                        continue
                    new_row, new_col = row + dr, col + dc
                    if self.in_bounds(new_row, new_col):
                        target = self.board[new_row][new_col]
                        if target is None or self.piece_color(target) != self.turn:
                            moves.append((new_row, new_col))

        return moves

    def in_bounds(self, row, col):
        return 0 <= row < self.size and 0 <= col < self.size


if __name__ == "__main__":
    root = tk.Tk()
    ChessGame(root)
    root.mainloop()
