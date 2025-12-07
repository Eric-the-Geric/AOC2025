from re import findall

def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

def main():
    content = read_file("in.txt")
    rows = content.splitlines()
    calcs = list(rows.pop(-1).replace(" ", ""))
    board = []
    for row in rows:
        new_row = list(row)
        board.append(new_row)
    numbers = []
    for i in range(len(board[0])-1, -1, -1):
        new_number = ""
        for j in range(len(board)):
            #print(board[j][i])
            new_number+=board[j][i]
            
        numbers.append(new_number)
    #print(numbers)
    i = len(calcs)-1
    total = 0
    n = 0
    for num in numbers:
        if any(char.isdigit() for char in num)==False:
            total+=n
            n = 0
            i -= 1
            continue
        if n == 0:
            n = int(num)
            continue
        if calcs[i] == "*":
            print(f"{n} * {num}")
            n*=int(num)
        elif calcs[i] == "+":
            print(f"{n} + {num}")
            n+=int(num)
    
    #forgot that there isn't a last check so need to add this... i guess it's a little hacky though
    total += n
    print(total)







if __name__ == "__main__":
    main()
