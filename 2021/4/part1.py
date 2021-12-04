with open("input.lst") as f:
    input = f.read().splitlines()

bingo_numbers = input[0].split(",")

def get_bingo_boards(input):
    i = 0
    bingo_boards = []
    for line in input:
        if i <= 1:
            bingo_board = []
            i += 1
            continue
        if line == "":
            bingo_boards.append(bingo_board)
            bingo_board = []
            i += 1
            continue
        if (i + 1) == len(input):
            bingo_board.append((' '.join(line.split())).split(" "))
            bingo_boards.append(bingo_board)
            continue
        bingo_board.append((' '.join(line.split())).split(" "))

        i += 1
    return bingo_boards

def bingo_draw(board, bingo_numbers):
    hits = {
        "r_0": 0,
        "r_1": 0,
        "r_2": 0,
        "r_3": 0,
        "r_4": 0,
        "c_0": 0,
        "c_1": 0,
        "c_2": 0,
        "c_3": 0,
        "c_4": 0
    }
    for num in bingo_numbers:
        r_num = 0
        for row in board:
            if num in row:
                hits["r_" + str(r_num)] += 1
                hits["c_" + str(row.index(num))] += 1
            r_num += 1
        
        if 5 in hits.values():
           return bingo_numbers.index(num)
           break

def get_winner_board(boards):
    prev_num = 100
    for board in boards:
        if bingo_draw(board, bingo_numbers) < prev_num:
            winner_board = boards.index(board)
            prev_num = bingo_draw(board, bingo_numbers)
    return winner_board

def calc_score(board, bingo_numbers):
    minus_score = 0
    board_sum = 0
    winning_num = bingo_numbers[bingo_draw(board, bingo_numbers)]
    drawn_nums = bingo_numbers[:bingo_numbers.index(winning_num)+1]
    for row in board:
        for num in row:
            board_sum += int(num)
            if num in drawn_nums:
                minus_score += int(num)

    score = (board_sum - minus_score) * int(winning_num)
    return score


bingo_boards = get_bingo_boards(input)
final_score = calc_score(bingo_boards[int(get_winner_board(bingo_boards))], bingo_numbers)
print(final_score)
