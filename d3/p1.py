def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content
# from stackoverflow (so cool!) https://stackoverflow.com/questions/6422700/how-to-get-indices-of-a-sorted-array-in-python


def main():
    file_path = 'in.txt'  # Replace with your file path
    content = read_file(file_path)
    banks = content.splitlines()
    jolts = 0
    for bank in banks:
        bats = [int(c) for c in bank]
        indices =[i[0] for i in sorted(enumerate(bats), key=lambda x:x[1], reverse=True)]
        if indices[0] == len(bats) -1:
            jolt = int(str(bats[indices[1]])+str(bats[indices[0]]))
            jolts+=jolt
        else:
            for ind in indices[1:]:
                if ind < indices[0]:
                    continue
                else:
                    jolt = int(str(bats[indices[0]])+str(bats[ind]))
                    jolts+=jolt
                break
    print(jolts)

if __name__ == "__main__":
    main()
