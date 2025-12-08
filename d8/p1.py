from math import sqrt
from re import findall
def read_file(file_path):
    """Reads the content of a file and returns it as a string."""
    with open(file_path, 'r') as file:
        content = file.read().strip()
    return content



class Circuit:
    def __init__(self):
        self.nodes = []

    def add_nodes(self, n1, n2):
        if not n1.check_connected(n2):
            self.nodes.append(n1)
            self.nodes.append(n2)
        


class Node:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.connected_to = [self]

    def distance(self, other):
        d = sqrt((self.x - other.x)**2+ (self.y - other.y)**2 + (self.z - other.z)**2)
        return d

    def check_connected(self, other):
        return other in self.connected_to

    def __eq__(self, other):
        return self.x== other.x and self.y==other.y and self.z==other.z

    def __repr__(self) -> str:
        return f"[{self.x=} {self.y=} {self.z=}]"

    def __len__(self):
        return len(self.connected_to)



def main():
    content = read_file("eg.txt")
    junction_boxes = [list(map(lambda x: int(x), findall(r"\d+", row))) for row in content.splitlines()]
    all_nodes = []
    for box in junction_boxes:
        node = Node(*box)
        all_nodes.append(node)

    for i in range(10):
        smallest_distance = None
        shortest_pair = (None, None)

        circuits = []
        for n1 in all_nodes[:-1]:
            for n2 in all_nodes[1:]:
                if n1 == n2:
                    continue
                d = n1.distance(n2)
                if smallest_distance == None:
                    smallest_distance = d
                    shortest_pair = (n1, n2)
                elif d < smallest_distance and not n1.check_connected(n2):
                    smallest_distance = d
                    shortest_pair = (n1, n2)

        if not shortest_pair[0].check_connected(shortest_pair[1]):
            shortest_pair[0].connected_to.append(shortest_pair[1])
        if not shortest_pair[1].check_connected(shortest_pair[0]):
            shortest_pair[1].connected_to.append(shortest_pair[0])

    circuits = []
    for node in all_nodes:
        for n in node.connected_to:
            if len(circuits)>0:
                if node in circuits[-1]:
                    circuits[-1] = [n]
                    print(circuits)
                    #print([n])
                else:
                    circuits[-1].append(n)
            else:
                circuits.append([n])
    #print(len(circuits[1]))
    #for i in range(len(circuits[0])):
    #    print(len(circuits[0][i]))








    


if __name__ == "__main__":
    main()
