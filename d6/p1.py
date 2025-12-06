from re import findall

def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

def main():
    content = read_file("in.txt")
    rows = content.splitlines()
    calcs = list(rows.pop(-1).replace(" ", ""))
    rows = [findall(r'\d+', r) for r in rows]

    total = 0
    for i in range(len(rows[0])):
        count = 0
        for j in range(len(rows)):
            calc = calcs[i]
            if j == 0:
                count = int(rows[j][i])
                continue
            if calc == "*":
                count*=int(rows[j][i])
            elif calc == "+":
                count+=int(rows[j][i])
        total += count
    print(total)





    




if __name__ == "__main__":
    main()
