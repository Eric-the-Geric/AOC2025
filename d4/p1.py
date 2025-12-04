def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

def main():
    file_path = 'in.txt'  # Replace with your file path
    content = read_file(file_path)
    rows = content.splitlines()
    board = [list(row) for row in rows]
    total = 0
    for x, row in enumerate(board):
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
                    total +=1
    print(total)

if __name__ == "__main__":
    main()
