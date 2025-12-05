def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

def main():
    file_path = 'eg.txt'  # Replace with your file path
    content = read_file(file_path)
    rows = content.splitlines()
    ingredient_id_range = []
    ids = []
    on_range = True
    for r in rows:
        if r == "":
            on_range = False
            continue
        if on_range:
            ingredient_id_range.append(r)
        else:
            ids.append(r)

    #print(ingredient_id_range)
    #print(ids)
    ranges = []
    count = 0
    for rang in ingredient_id_range:
        lo, hi = tuple(map(lambda x: int(x), rang.split('-')))
        for i in range(lo, hi+1):
            ranges.append(i)
    for id in ids:
        if int(id) in ranges:
            count+=1
    print(count)


if __name__ == "__main__":
    main()
