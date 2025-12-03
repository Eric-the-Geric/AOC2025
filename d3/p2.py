def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content
# from stackoverflow (so cool!) https://stackoverflow.com/questions/6422700/how-to-get-indices-of-a-sorted-array-in-python


def main():
    file_path = 'eg.txt'  # Replace with your file path
    content = read_file(file_path)
    banks = content.splitlines()
    jolts = 0
    for bank in banks:
        queue = []
        bats = [int(c) for c in bank]
        indices =[i[0] for i in sorted(enumerate(bats), key=lambda x:x[1])]
        for bat in bats:
            print(f"queue: {queue}")
            if len(queue) > 11:
                ind = queue.index(min(queue))
                print(f"full indices ascending: {indices}")
                print(f"lowest index of min: {ind}")
                queue.pop(ind)
                indices.pop(ind)
            queue.append(bat)

        battery_array = [str(q) for q in queue]
        #print(battery_array)
        batt = "".join(battery_array)
        #print(batt)
        jolts += int("".join(battery_array))
    print(jolts)
        



if __name__ == "__main__":
    main()
