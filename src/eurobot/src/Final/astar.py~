from itertools import product
from math import sqrt, atan, pi

gridString="""000000000000000010000000000001100000000000010000000000000000
000000000000000010000000000001100000000000010000000000000000
000000000000000010000000000001100000000000010000000000000000
000000000000000010000000000001100000000000010000000000000000
000000000000000000000000000001100000000000000000000000000000
000000000000000000000000000001100000000000000000000000000000
000000000000000000000000000001100000000000000000000000000000
000000000000000000000000000001100000000000000000000000000000
000000000000000000000000000001100000000000000000000000000000
000000000000000000000000000001100000000000000000000000000000
000000000000000000000000000001100000000000000000000000000000
000000000000000000000000000001100000000000000000000000000000
000000000000000000000000000111111000000000000000000000000000
000000000000000000000000000111111000000000000000000000000000
000000000000000000000000000111111000000000000000000000000000
000000000000000001111111111111111111111111000000000000000000
000000000000000000000000000001100000000000000000000000000000
000000000000000000000000000001100000000000000000000000000000
000000000000000000000000000001100000000000000000000000000000
000000000000000000000010000001100000100000000000000000000000
000000000000000000000010000001100000100000000000000000000000
000000000000000000000010000001100000100000000000000000000000
000000000000000000000010000001100000100000000000000000000000
000000000000000000000010000001100000100000000000000000000000
000000000000000000000010000001100000100000000000000000000000
000000000000000000000010000001100000100000000000000000000000
000000000000000000000010000001100000100000000000000000000000
000000000000000000000010000000000000100000000000000000000000
000000000000000000000010000000000000100000000000000000000000
000000000000000000000010000000000000100000000000000000000000
000000000000000000000011111111111111100000000000000000000000
000000000000000000000000000001000000000000000000000000000000
000000000000000000000000000001000000000000000000000000000000
000000000000000000000000000001000000000000000000000000000000
000000000000000000000000000001000000000000000000000000000000
111000000000000000000000000001000000000000000000000000000111
111100000000000000000000000001000000000000000000000000001111
111110000000000000000000000001000000000000000000000000011111
111110000000000000000000000001000000000000000000000000011111
111110000000000000000000000001000000000000000000000000011111"""


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
        self.obst = False
        super(AStarGridNode, self).__init__()

    def move_cost(self, other):
        diagonal = abs(self.x - other.x) == 1 and abs(self.y - other.y) == 1
        return 14 if diagonal else 10 # fourteen comes from 1.414 = sqrt(2) for diagonals

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
    #print("All Obstacles")
    for row in gridString.split("\n"):
        for x in range(len(row)):
            if (row[x]=='1'):
                node=nodes[x][y]
                #print(node.x, '\t', node.y)
                node.obst=True
                for i, j in product([-1, 0, 1], [-1, 0, 1]): #returns pairs such as 00 01 10 11 0-1 -10 -11 1-1
                    #print ("not1")
                    if not (0 <= x + i < width):
                        continue
                    #print ("not2")
                    if not (0 <= y + j < height):
                        continue

                    if (nodes[x+i][y+j] in graph):
                        if (node in graph[nodes[x+i][y+j]]):
                            graph[nodes[x+i][y+j]].remove(node)

        y += 1

#works out the distance from a node to the line plotted by node1 and node2
def distance(node1, node2, node):
    x1, y1 = node1.x, node1.y
    x2, y2 = node2.x, node2.y
    x0, y0 = node.x, node.y
    nom = abs((y2 - y1) * x0 - (x2 - x1) * y0 + (x2 * y1) - (y2 * x1))
    denom = ((y2 - y1)**2 + (x2 - x1) ** 2) ** 0.5
    if denom == 0 or nom ==0:
        result = 999999.0
    else:
        result = nom / denom
    return result

def obsticle_under_line(node1, node2,nodes):
    if abs(node1.x-node2.x)<=1 and abs(node1.y-node2.y)<=1:
        return False

    minX=min(node1.x,node2.x)
    maxX=max(node1.x,node2.x)
    minY=min(node1.y,node2.y)
    maxY=max(node1.y,node2.y)
    for x, y in product(range(minX,maxX), range(minY,maxY)):
        node = nodes[x][y]
        if node.obst:
            if (node1 is not node) or (node2 is not node):
                dist = distance(node1,node2,node)
                if dist < 0.7:
                    print(node.x, '\t', node.y)
                    return True
    return False

def generalise(graph, nodes, path):
    newpath=[] #list of generalised points
    count=0
    newpath.append(path[count])
    prevNode=path[count]
    print("Obstacles")
    for node in path:
        if (node is not prevNode):
            if obsticle_under_line(newpath[count],node,nodes):
                newpath.append(prevNode)
                count+=1
            prevNode=node

    if newpath[count] is not prevNode:
        newpath.append(prevNode)
    print ('New Path')
    return newpath

def dist(node1, node2):
    x1, y1 = node1.x, node1.y
    x2, y2 = node2.x, node2.y
    return ((y2 - y1)**2 + (x2 - x1) ** 2) ** 0.5

def bearing(node1, node2):
    x1, y1 = node1.x, node1.y
    x2, y2 = node2.x, node2.y
    d_x = (x2 - x1) #delta x
    d_y = (y2 - y1) #delta y
    if d_y==0:
        d_y=0.0000000001
    if d_x>=0 and d_y>0:
        return atan(d_x/d_y)
    if d_x>=0 and d_y<0:
        return pi-atan(d_x/-d_y)
    if d_x<=0 and d_y<0:
        return pi+atan(d_x/d_y)
    if d_x<=0 and d_y>0:
        return 2*pi-atan(-d_x/d_y)

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

    instructions=[]
    currentDirection = 0 # some direction relative to north
    newpath = generalise(graph, nodes, path)
    prevNode = newpath[0]
    for node in newpath:
        print (node.x,"\t",node.y)
        instruct = ("t",round(bearing(prevNode,node),2))
        instructions.append(instruct)
        instruct = ("d",round(dist(prevNode,node)*5,2))
        instructions.append(instruct)
        prevNode=node

    """for i in instructions:
        print (i)"""
    print(instructions)
