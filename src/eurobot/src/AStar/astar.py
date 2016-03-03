from itertools import product
from math import sqrt

gridString="""000000000000001111111110001111100000000000010000000000000000
000000000000000010000001111100100000000000010000000000000000
000000000000000010000000011100100000000000010000000000000000
000000000000000010000000011100100000000000010000000000000000
000000000000000000000000001100100000000000000000000000000000
000000000000000000000000001100100000000000000000000000000000
000000000000000000000000001100100000000000000000000000000000
000000000000000000000000001110100000000000000000000000000000
000000000000000000000000001110100000000000000000000000000000
000000000000000000000000001110100000000000000000000000000000
000000000000000000000000001110100000000000000000000000000000
000000000000000000000000001110100000000000000000000000000000
000000000000000000000000001110100000000000000000000000000000
000000000000000000000000001100100000000000000000000000000000
000000000000000000000000001111100000000000000000000000000000
000000000000000000111111111111111111111111000000000000000000
000000000000000000000000000001100000000000000000000000000000
000000000000000000000000000001100000000000000000000000000000
000000000000000000000000000001100000000000000000000000000000
000000000000000000000000000001100000000000000000000000000000
000000000000000000000000000001100000000000000000000000000000
000000000000000000000000000001100000000000000000000000000000
000000000000000000000000000001100000000111110000000000000000
000000000000000000000000000001100000001100011000000000000000
000000000000000000000000000001100000111100001011111111000000
000000000000000000000000000001100001111001001111111111100000
000000000000000000000000000001101111111001001111111111100000
000000000000000000000000000011111011110011001110111111100000
000000000000000000000000000011110111110011001110011111100000
000000000000000000000000000011110111110011001100001111100000
000000000000000000000000000011110111100110001100001111100000
000000000000000000000000000011111111000100001100101111100000
000000000000000000000000000011111111001100011100101111100000
000000000000000000000000000011111111001000111000101111100000
000000000000000000000000000111111110001001110000101111000000
111000000000000000000000000110011100001001110001101111000111
111100000000000000000000000111111000010001000001100000001111
111110000000000000000000000111110000010011000001110000011111
111110000000000000000000000000000001100000000001100000011111
111110000000000000000000000000001110000000000011100000011111"""


class AStar(object):
    def __init__(self, graph):
        self.graph = graph
        
    def heuristic(self, node, start, end):
        raise NotImplementedError
        
    def search(self, start, end):
        openset = set()
        closedset = set()
        current = start
        openset.add(current)
        while openset:
            current = min(openset, key=lambda o:o.g + o.h)
            if current == end:
                path = []
                while current.parent:
                    path.append(current)
                    current = current.parent
                path.append(current)
                return path[::-1]
            openset.remove(current)
            closedset.add(current)
            for node in self.graph[current]:
                if node in closedset:
                    continue
                if node in openset:
                    new_g = current.g + current.move_cost(node)
                    if node.g > new_g:
                        node.g = new_g
                        node.parent = current
                else:
                    node.g = current.g + current.move_cost(node)
                    node.h = self.heuristic(node, start, end)
                    node.parent = current
                    openset.add(node)
        return None


class AStarNode(object):
    def __init__(self):
        self.g = 0
        self.h = 0
        self.parent = None
        
    def move_cost(self, other):
        raise NotImplementedError

class AStarGrid(AStar):
    def heuristic(self, node, start, end):
        return sqrt((end.x - node.x)**2 + (end.y - node.y)**2)


class AStarGridNode(AStarNode):
    def __init__(self, x, y):
        self.x, self.y = x, y
        super(AStarGridNode, self).__init__()

    def move_cost(self, other):
        diagonal = abs(self.x - other.x) == 1 and abs(self.y - other.y) == 1
        return 14 if diagonal else 10 # forteen comes from 1.414 = sqrt(2) for diagonals

def make_graph(width, height):
    nodes = [[AStarGridNode(x, y) for y in range(height)] for x in range(width)]
    graph = {} #dictionary
    for x, y in product(range(width), range(height)):
        node = nodes[x][y]
        graph[node] = []
        # neighbours
        for i, j in product([-1, 0, 1], [-1, 0, 1]): #returns pairs such as 00 01 10 11 0-1 -10 -11 1-1
            if not (0 <= x + i < width):
                continue
            if not (0 <= y + j < height):
                continue
            graph[nodes[x][y]].append(nodes[x+i][y+j])
    return graph, nodes

def make_walls(gridString, graph, nodes, width, height):
    y=0
    for row in gridString.split("\n"):
        for x in range(len(row)):
            if (row[x]=='1'):
                for i, j in product([-1, 0, 1], [-1, 0, 1]): #returns pairs such as 00 01 10 11 0-1 -10 -11 1-1
                    #print ("not1")
                    if not (0 <= x + i < width):
                        continue
                    #print ("not2")
                    if not (0 <= y + j < height):
                        continue

                    if (nodes[x+i][y+j] in graph):
                        if (nodes[x][y] in graph[nodes[x+i][y+j]]):
                            graph[nodes[x+i][y+j]].remove(nodes[x][y])
        y=y+1


graph, nodes = make_graph(60, 40)
make_walls(gridString, graph, nodes, 60, 40)
paths = AStarGrid(graph)
start, end = nodes[15][20], nodes[45][20]
path = paths.search(start, end)
if path is None:
    print ('No path found')
    
else:
    print ('Path found:')
    for node in path:
        print (node.x,"\t",node.y)
    
