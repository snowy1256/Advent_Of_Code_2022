import aoc


def get_value_of_move(move):
    if move == "A":
        return 1
    if move == "B":
        return 2
    if move == "C":
        return 3
    if move == "X":
        return 0
    if move == "Y":
        return 3
    if move == "Z":
        return 6


def sort_moves(rps_input):
    moves = []
    for line in rps_input:
        turn = line.split(" ")
        moves.append([get_value_of_move(turn[0]), get_value_of_move(turn[1])])
    return moves


def get_correct_move(attack, win):
    
    if attack == 1:
        if win:
            return 2
        else:
            return 3
    if attack == 2:
        if win:
            return 3
        else:
            return 1
    if attack == 3:
        if win:
            return 1
        else:
            return 2


def pick_move(move):
    if move[1] == 0:
        return get_correct_move(move[0], False) + move[1]
    if move[1] == 3:
        return move[1] + move[0]
    if move[1] == 6:
        return get_correct_move(move[0], True) + move[1]


if __name__ == "__main__":
    rps_input = aoc.load_input("day2/input.txt")
    moves = sort_moves(rps_input)
    total = 0
    for move in moves:
        move_result = pick_move(move)
        total += move_result
    print(total)
