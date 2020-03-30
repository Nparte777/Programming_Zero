# Input
board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]


def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):              # Checking Valid Number from 1-9
        if valid(bo, i, (row, col)):
            bo[row][col] = i            # Assign Valid Number to Main Board

            if solve(bo):
                return True

        bo[row][col] = 0                # Reset If No Number Found // BackTrack with Recursive call
    return False


def valid(bo, num, pos):
    # Check Row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check Column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False
    # Check Box
    box_x = pos[1]//3       # pos[1] is column
    box_y = pos[0]//3       # pos[0] is rom
    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:           # To avoid Duplicate entries
                return False
    return True

def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - -")    # Horizontal Seperator
        for j in range(len(bo[0])):                 # bo[0] is length of each list inside a main list
           if j % 3 ==0 and j != 0:
               print("  | ", end="")                 # Vertical Seperator
           if j == 8:
               print(bo[i][j])
           else:
               print(str(bo[i][j]) + " ", end="")

def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)        #row , column
    return None


print_board(board)
print("______________________________")
solve(board)
print_board(board)