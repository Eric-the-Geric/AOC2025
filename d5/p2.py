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
    highs, lows = [], []
    for rang in ingredient_id_range:
        lo, hi = tuple(map(lambda x: int(x), rang.split('-')))
        highs.append(hi)
        lows.append(lo)

    sorted_ranges = sorted(zip(lows, highs), key=lambda x: x[0])
    merged_ranges = []
    for current in sorted_ranges:
        # logging
        #print(f"current: {current}")
        #print(f"merged_ranges[-1]: {merged_ranges[-1]}" if merged_ranges else "empty")
        #print(f"merged_ranges: {merged_ranges}")

        if not merged_ranges or merged_ranges[-1][1] < current[0]:
            merged_ranges.append(current)
        else:
            merged_ranges[-1] = (merged_ranges[-1][0], max(merged_ranges[-1][1], current[1]))

    total = 0
    for merged in merged_ranges:
        total += merged[1] - merged[0] + 1
    print(total)







if __name__ == "__main__":
    main()
