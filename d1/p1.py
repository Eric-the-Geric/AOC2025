def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

def main():
    # get the file content
    file_path = 'input.txt'  # Replace with your file path
    #file_path = 'example.txt'  # Replace with your file path
    content = read_file(file_path)
    lines = content.splitlines()
    pointer = 50
    dial = [i for i in range(100)]


    count = 0
    for line in lines:
        #print(line[1:])
        if line.startswith("L"):
            pointer = (pointer - int(line[1:])) % 100
        elif line.startswith("R"):
            pointer = (pointer + int(line[1:])) % 100
        if pointer == 0:
            count += 1
    print(count)





    



if __name__ == "__main__":
    main()
