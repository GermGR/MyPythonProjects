import random

class Player:
    def __init__(self, name):
        self.name = name
        self.board = [[" " for _ in range(10)] for _ in range(10)]
        self.ships = {
            "Aircraft Carrier": 5,
            "Battleship": 4,
            "Cruiser": 3,
            "Submarine": 3,
            "Destroyer": 2
        }

    def auto_place_ships(self):
        for ship in self.ships:
            while True:
                x = random.randint(0, 9)
                y = random.randint(0, 9)
                direction = random.choice(["horizontal", "vertical"])
                if self.can_place_ship(self.board, x, y, self.ships[ship], direction):
                    self.place_ship(x, y, self.ships[ship], direction)
                    break

    def can_place_ship(self, board, x, y, ship_length, direction):
        if direction == "horizontal":
            for i in range(ship_length):
                if y + i >= 10 or board[x][y + i] != " " or self.has_adjacent_ship(board, x, y + i):
                    return False
        elif direction == "vertical":
            for i in range(ship_length):
                if x + i >= 10 or board[x + i][y] != " " or self.has_adjacent_ship(board, x + i, y):
                    return False
        return True

    def has_adjacent_ship(self, board, x, y):
        adjacent_cells = [
            (x-1, y), (x+1, y), (x, y-1), (x, y+1),
            (x-1, y-1), (x-1, y+1), (x+1, y-1), (x+1, y+1)
        ]
        for cell in adjacent_cells:
            if cell[0] >= 0 and cell[0] < 10 and cell[1] >= 0 and cell[1] < 10:
                if board[cell[0]][cell[1]] == "■":
                    return True
        return False

    def place_ship(self, x, y, ship_length, direction):
        if direction == "horizontal":
            for i in range(ship_length):
                self.board[x][y + i] = "■"
        elif direction == "vertical":
            for i in range(ship_length):
                self.board[x + i][y] = "■"

    def attack(self, target_player, x, y):
        if x < 0 or x > 9 or y < 0 or y > 9:
            print("Недопустимый ход!")
        elif target_player.board[x][y] == " ":
            print("Вы промахнулись!")
            target_player.board[x][y] = "O"
        elif target_player.board[x][y] == "■":
            print("Попадание!")
            target_player.board[x][y] = "*"
        elif target_player.board[x][y] in ["O", "*"]:
            print("Уже стреляли в эту клетку!")

    def is_ships_sunk(self):
        for row in self.board:
            if "■" in row:
                return False
        return True

def print_board(board):
    print("   |0|1|2|3|4|5|6|7|8|9|")
    print("   ---------------------")
    for i, row in enumerate(board):
        print(f"{i} | {' '.join(row)} |")
    print("   --------------------")

def main():
    player1 = Player("Игрок 1")
    player1.auto_place_ships()

    player2 = Player("Игрок 2")
    player2.auto_place_ships()

    while True:
        print(f"Ход игрока {player1.name}")
        print("Доска Игрока 1:")
        print_board(player1.board)
        print("Доска Игрока 2:")
        print_board(player2.board)

        x = int(input("Введите координату X для атаки: "))
        y = int(input("Введите координату Y для атаки: "))

        player1.attack(player2, x, y)

        if player2.is_ships_sunk():
            print("Игрок 1 выиграл!")
            break

        print(f"Ход игрока {player2.name}")
        print("Доска игрока:")
        print_board(player2.board)
        print("Доска противника:")
        print_board(player1.board)

        x = int(input("Введите координату X для атаки: "))
        y = int(input("Введите координату Y для атаки: "))

        player2.attack(player1, x, y)

        if player1.is_ships_sunk():
            print("Игрок 2 выиграл!")
            break

if __name__ == "__main__":
    main()