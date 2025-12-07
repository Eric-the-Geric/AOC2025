def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

def check_boundry(pos, direction, h, w):
    y, x = pos[0], pos[1]
    i, j = direction[0], direction[1]
    if (y+i > h) or (y+i <0) or (x+j > w) or (x+j < 0):
        return False
    else:
        return True
    

def main():
    content = read_file("eg.txt")
    rows = content.splitlines()
    board = [list(line) for line in rows]
    down = (+1, 0)
    downright = (+1, +1)
    downleft = (+1, -1)
    s = "S"
    count = 0
    for i, row in enumerate(board):
        for j, val in enumerate(row):
            if i == 0:
                if val == "S":
                    board[i+down[0]][j+down[1]] = "|"
            if val == "|":
                if check_boundry((i+1, j), downright, len(board), len(board[0])):
                    if board[i+down[0]][j+down[1]] == "^":
                        count+=1
                        if check_boundry((i+1, j), downright, len(board), len(board[0])):
                            dr = board[i+downright[0]][j + downright[1]]
                            if dr == ".":
                                board[i+ downright[0]][j + downright[1]] = "|"
                        if check_boundry((i, j), downleft, len(board), len(board[0])):
                            dl = board[i+ downleft[0]][j + downleft[1]]
                            if dl == ".":
                                board[i+ downleft[0]][j + downleft[1]] = "|"
                    else:
                        board[i+down[0]][j+down[1]] = "|"


    #count = 0
    #for row in board:
    #    print("".join(row))
    #    for val in row:
    #        if val == "|":
    #            count+=1
    print(count)
                    

if __name__ == "__main__":
    main()

