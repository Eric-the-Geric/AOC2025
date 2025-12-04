def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

def new_board(board):
    total = 0
    new_board = []
    for x, row in enumerate(board):
        new_row = []
        for y, c in enumerate(row):
            if c == '@':
                count = 0
                for i in (-1, 0, 1):
                    for j in (-1, 0, 1):
                        if i == 0 and j == 0:
                            continue
                        if (i+x < 0) or (i+x > len(board)-1) or (j+y < 0) or (j+y > len(board[0])-1):
                            continue
                        if board[i+x][y+j] == '@':
                            count += 1
                if count < 4:
                    new_row.append('x')
                    total +=1
                else:
                    new_row.append(c)
            else:
                new_row.append(c)
        new_board.append(new_row)
    board = new_board
    return total, board

def main():

    file_path = 'in.txt'  # Replace with your file path
    content = read_file(file_path)
    rows = content.splitlines()
    board = [list(row) for row in rows]
    total_total = 0
    total, board = new_board(board)
    total_total += total
    while total > 0:
        total, board = new_board(board)
        total_total += total
    print("Final total:", total_total)

if __name__ == "__main__":
    main()
