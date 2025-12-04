def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

def main():
    file_path = 'in.txt'  # Replace with your file path
    content = read_file(file_path)
    banks = content.splitlines()
    jolts = 0
    for bank in banks:
        bats = [int(c) for c in bank]
        stack = []
        n = len(bats)
        k = 12 # amout of batteries to choose
        # we have to drop n-k batteries
        drop = n - k
        for b in bats:
            while drop > 0 and len(stack) > 0 and b >stack[-1]:
                stack.pop()
                drop -= 1
            stack.append(b)
        if len(stack) > k:
            stack = stack[:k]
        jolts += int("".join([str(s) for s in stack]))
    print(jolts)
        
        



if __name__ == "__main__":
    main()
