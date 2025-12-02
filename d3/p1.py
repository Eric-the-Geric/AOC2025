def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content




def main():
    f = read_file("input.txt").removesuffix('\n')
    ranges = f.split(",")
    invalid_ids = []
    for r in ranges:
        SE = r.split("-")
        n_start = int(SE[0])
        n_end = int(SE[-1])
        for number in range(n_start, n_end+1):
            number_str = str(number)
            pointer = len(number_str)//2
            first = number_str[:pointer]
            second = number_str[pointer:]
            if first == second:
                invalid_ids.append(number)
    print(sum(invalid_ids))




if __name__ == "__main__":
    main()
