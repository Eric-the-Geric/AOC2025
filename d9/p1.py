"""
All the board stuff was for debugging and generating a board for input would be
infesible haha. Maybe I'll clean it later
"""
from re import findall


FILE = "in.txt"
def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read().strip()
        return content

#def calculate_area(p1, p2):
#    """
#    okay so how do we create a rectangle from two points?
#    (7, 11) and (5, 10)
#    then we create two other points:
#        (5, 11) and (7, 10)
#    """


def generate_board(m):
    return [["." for _ in range(m+3)] for x in range(m+2)]

def main():
    content = read_file(FILE)
    content = content.splitlines()

    positions = [tuple(map(lambda x: int(x), findall(r"\d+", row))) for row in content]

    #max_h = max(positions)[0]
    #max_w = max(positions, key= lambda x: x[1])[1]
    #maximum = max(max_h, max_w)

    #board = [["." for _ in range(max_h+3)] for x in range(max_w+2)]
    #board = generate_board(maximum)

    areas = []
    for i in range(len(positions)):
        for j in range(len(positions)):
            if i == j:
                continue
            p1 = positions[i]
            p2 = positions[j]
            p3 = (p1[0], p2[1])
            p4 = (p2[0], p1[1])
            #board[p1[0]][p1[1]] = f'{p1}'
            #board[p2[0]][p2[1]] = f'{p2}'
            #board[p3[0]][p3[1]] = f'{p3}'
            #board[p4[0]][p4[1]] = f'{p4}'

            # p1 and 2 should be opposite sides
            # so then it should matter which direction I go...



            height = abs(p1[0] - p4[0])+1
            width = abs(p1[1] - p3[1]) +1
            areas.append(height*width)
            #print('-'*10)
            #for row in board:
            #    print(row)
            #print('-'*10)

            #board = generate_board(maximum)
            #h = abs(p1[0] - p3[0])
            #w = (p1[1] - p2[1])
            #areas.append(h*w)
    print(max(areas))






    #board[positions[0][0]][positions[0][1]] = "#"
    #board[positions[1][0]][positions[1][1]] = "#"

    #board[positions[0][0]][positions[1][1]] = "#"
    #board[positions[1][0]][positions[0][1]] = "#"
    
if __name__ == "__main__":
    main()


