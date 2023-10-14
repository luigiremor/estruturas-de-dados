import queue

position_to_i = {
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
    "e": 4,
    "f": 5,
    "g": 6,
    "h": 7
}

UPPER_BOUNDARY = 0
LEFT_BOUNDARY = 0
RIGHT_BOUNDARY = 7
LOWER_BOUNDARY = 7


def get_indexes(position):
    i = int(position_to_i[position[0]])
    j = int(position[1]) - 1
    return i, j


class Chess:

    def __init__(self):
        self.board = self._create_board()

    def _create_board(self):
        return [
            ["X", "X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X", "X"],
            ["X", "X", "X", "X", "X", "X", "X", "X"],
        ]

    def mark_board(self, i, j, mark):
        self.board[i][j] = mark

    def print(self):
        for i in range(len(self.board[0])):
            for j in range(len(self.board[1])):
                if i == aimed_position[0] and j == aimed_position[1]:
                    # print x in red
                    print("\033[1;31;40m{}\033[0m".format(
                        self.board[i][j]), end=" ")
                else:
                    print(self.board[i][j], end=" ")
            print()


initial_position = "a1"

final_position = "b2"


i, j = get_indexes(final_position)
aimed_position = (i, j)
i, j = get_indexes(initial_position)
initial_position = (i, j)

chess = Chess()
chess.mark_board(i=initial_position[0], j=initial_position[1], mark=0)

queue = queue.Queue()

queue.put(initial_position)


while not queue.empty():
    chess.print()
    print()

    base_place = queue.get()
    moviment_index = chess.board[base_place[0]][base_place[1]]

    # upper left
    if i - 2 >= UPPER_BOUNDARY and j - 1 >= LEFT_BOUNDARY and chess.board[i - 2][j - 1] == "X":
        if i - 2 == aimed_position[0] and j - 1 == aimed_position[1]:
            chess.mark_board(i=i-2, j=j-1, mark=moviment_index+1)
            break
        chess.mark_board(i=i-2, j=j-1, mark=moviment_index+1)
        queue.put((i-2, j-1))

    # upper right
    if i - 2 >= UPPER_BOUNDARY and j + 1 <= RIGHT_BOUNDARY and chess.board[i - 2][j + 1] == "X":
        if i - 2 == aimed_position[0] and j + 1 == aimed_position[1]:
            chess.mark_board(i=i-2, j=j+1, mark=moviment_index+1)
            break
        chess.mark_board(i=i-2, j=j+1, mark=moviment_index+1)
        queue.put((i-2, j+1))

    # right up
    if i - 1 >= UPPER_BOUNDARY and j + 2 <= RIGHT_BOUNDARY and chess.board[i - 1][j + 2] == "X":
        if i - 1 == aimed_position[0] and j + 2 == aimed_position[1]:
            chess.mark_board(i=i-1, j=j+2, mark=moviment_index+1)
            break
        chess.mark_board(i=i-1, j=j+2, mark=moviment_index+1)
        queue.put((i-1, j+2))

    # right down
    if i + 1 <= LOWER_BOUNDARY and j + 2 <= RIGHT_BOUNDARY and chess.board[i + 1][j + 2] == "X":
        if i + 1 == aimed_position[0] and j + 2 == aimed_position[1]:
            chess.mark_board(i=i+1, j=j+2, mark=moviment_index+1)
            break
        chess.mark_board(i=i+1, j=j+2, mark=moviment_index+1)
        queue.put((i+1, j+2))

    # down right
    if i + 2 <= LOWER_BOUNDARY and j + 1 <= RIGHT_BOUNDARY and chess.board[i + 2][j + 1] == "X":
        if i + 2 == aimed_position[0] and j + 1 == aimed_position[1]:
            chess.mark_board(i=i+2, j=j+1, mark=moviment_index+1)
            break
        chess.mark_board(i=i+2, j=j+1, mark=moviment_index+1)
        queue.put((i+2, j+1))

    # down left
    if i + 2 <= LOWER_BOUNDARY and j - 1 >= LEFT_BOUNDARY and chess.board[i + 2][j - 1] == "X":
        if i + 2 == aimed_position[0] and j - 1 == aimed_position[1]:
            chess.mark_board(i=i+2, j=j-1, mark=moviment_index+1)
            break
        chess.mark_board(i=i+2, j=j-1, mark=moviment_index+1)
        queue.put((i+2, j-1))

    # left down
    if i + 1 <= LOWER_BOUNDARY and j - 2 >= LEFT_BOUNDARY and chess.board[i + 1][j - 2] == "X":
        if i + 1 == aimed_position[0] and j - 2 == aimed_position[1]:
            chess.mark_board(i=i+1, j=j-2, mark=moviment_index+1)
            break
        chess.mark_board(i=i+1, j=j-2, mark=moviment_index+1)
        queue.put((i+1, j-2))

    # left up
    if i - 1 >= UPPER_BOUNDARY and j - 2 >= LEFT_BOUNDARY and chess.board[i - 1][j - 2] == "X":
        if i - 1 == aimed_position[0] and j - 2 == aimed_position[1]:
            chess.mark_board(i=i-1, j=j-2, mark=moviment_index+1)
            break
        chess.mark_board(i=i-1, j=j-2, mark=moviment_index+1)
        queue.put((i-1, j-2))


print(chess.board[aimed_position[0]][aimed_position[1]])
