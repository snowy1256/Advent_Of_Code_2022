import aoc


def get_value_of_move(move):
    if move == "A" or move == "X":
        return 1
    if move == "B" or move == "Y":
        return 2
    if move == "C" or move == "Z":
        return 3


def sort_moves(rps_input):
    moves = []
    for line in rps_input:
        turn = line.split(" ")
        moves.append([get_value_of_move(turn[0]), get_value_of_move(turn[1])])
    return moves


def compare_move(move):
    win = 6
    draw = 3
    # draw
    if move[0] == move[1]:
        return move[1] + draw
    if move[0] == 1:
        if move[1] == 2:
            return move[1] + win
    if move[0] == 2:
        if move[1] == 3:
            return move[1] + win
    if move[0] == 3:
        if move[1] == 1:
            return move[1] + win
    return move[1]


if __name__ == "__main__":
    rps_input = aoc.load_input("day2/input.txt")
    moves = sort_moves(rps_input)
    total = 0
    for move in moves:
        move_result = compare_move(move)
        total += move_result
    print(total)
