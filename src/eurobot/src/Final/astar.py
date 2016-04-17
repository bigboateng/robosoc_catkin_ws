from itertools import product
from math import sqrt, atan, pi

class AStar(object):
    def __init__(self, graph):
        self.graph = graph
        self.obstacles = []
        
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
                    parent = current.parent
                    current.parent = None
                    current = parent
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
        self.g = 0.0
        self.h = 0.0
        self.parent = None

    def move_cost(self, other):
        raise NotImplementedError

class AStarGrid(AStar):
    def heuristic(self, node, start, end):
        return 1.0*sqrt((end.x - node.x)**2 + (end.y - node.y)**2)


class AStarGridNode(AStarNode):
    def __init__(self, x, y):
        self.x, self.y = x, y
        self.obst = False
        super(AStarGridNode, self).__init__()

    def move_cost(self, other):
        diagonal = not (abs(self.x - other.x) <= 1 and abs(self.y - other.y) <= 1)
        return 142 if diagonal else 10 # fourteen comes from 1.414 = sqrt(2) for diagonals it should never be diagonal

class PathPlanner(object):
    
    def __init__(self):
        self.gridString="""000000000000000010000000000000000000000000010000000000000000
000000000000000010000000000000000000000000010000000000000000
000000000000000010000000000000000000000000010000000000000000
000000000000000010000000000000000000000000010000000000000000
000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000
000000000000000000111111111111111111111111000000000000000000
000000000000000000000000000001100000000000000000000000000000
000000000000000000000000000001100000000000000000000000000000
000000000000000000000000000001100000000000000000000000000000
000000000000000000000000000001100000000000000000000000000000
000000000000000000000000000001100000000000000000000000000000
000000000000000000000000000001100000000000000000000000000000
000000000000000000000000000001100000000000000000000000000000
000000000000000000000000000001100000000000000000000000000000
000000000000000000000000000001100000000000000000000000000000
000000000000000000000000000001100000000000000000000000000000
000000000000000000000000000001100000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000
000000000000000000000000000000000000000000000000000000000000
111000000000000000000000000000000000000000000000000000000111
111100000000000000000000000000000000000000000000000000001111
111110000000000000000000000000000000000000000000000000011111
111110000000000000000000000000000000000000000000000000011111
111110000000000000000000000000000000000000000000000000011111"""
        self.obsticles=[]
        self.height = 40
        self.width = 60
        self.graph, self.nodes = self.make_graph(self.width, self.height)
        self.make_walls(self.gridString, self.graph, self.nodes, self.height, self.height)
        
    def make_graph(self,width, height):
        nodes = [[AStarGridNode(x, y) for y in range(height)] for x in range(width)]
        graph = {} #dictionary
        for x, y in product(range(width), range(height)):
            node = nodes[x][y]
            graph[node] = []
            # neighbours
            for i, j in product([-2, -1, 0, 1, 2], [-2, -1, 0, 1, 2]): #returns pairs such as 00 01 10 11 0-1 -10 -11 1-1
                if not (0 <= x + i < width):
                    continue
                if not (0 <= y + j < height):
                    continue
                graph[nodes[x][y]].append(nodes[x+i][y+j])
        return graph, nodes

    def make_walls(self,gridString, graph, nodes, width, height):
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
    def distance(self,node1, node2, node):
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

    def obsticle_under_line(self, node1, node2, nodes):
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
                    dist = self.distance(node1,node2,node)
                    if dist < 0.707:
                        return True
        return False

    def generalise(self,graph, nodes, path):
        newpath=[] #list of generalised points
        count=0
        newpath.append(path[0])
        prevNode=path[0]
        #print("Obstacles")
        for node in path:
            #print (str(node.x) + ", " + str(node.y))
            if (node is not path[0]):
                if self.obsticle_under_line(newpath[count],node,nodes):
                    #print ("obs" + str(node.x) + ", " + str(node.y))
                    #print ("append" + str(prevNode.x) + ", " + str(prevNode.y))
                    newpath.append(prevNode)
                    count+=1
                prevNode=node

        if newpath[count] is not prevNode:
            newpath.append(prevNode)
        #print ('New Path')]
        return newpath

    def dist(self,node1, node2):
        x1, y1 = node1.x, node1.y
        x2, y2 = node2.x, node2.y
        return ((y2 - y1)**2 + (x2 - x1) ** 2) ** 0.5

    def bearing(self,node1, node2):
        x1, y1 = node1.x, node1.y
        x2, y2 = node2.x, node2.y
        d_x = (x2 - x1) #delta x
        d_y = (y1 - y2) #delta y
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

    #clockwise is positive
    def calcAngle(self, prevBearing, newBearing):
        angle=newBearing-prevBearing
        
        if (newBearing>270.0 and prevBearing<90.0):
            angle = angle-360
        elif (prevBearing>270.0 and newBearing<90.0):
            angle = angle+360
        elif (angle<-180):
            angle=360+angle
        elif (angle>180):
            angle=360-angle
        return angle
        

    # gets nodes in a format: start, end = (15,20), (45,20)
    def getPath(self,start, end, startdirection, enddirection):
        paths = AStarGrid(self.graph)
        start, end = self.nodes[start[0]][start[1]], self.nodes[end[0]][end[1]]
        path = paths.search(start, end)
        instructions=[]
        if path is None:
            instructions.append("NoPath")
        else:
            newpath = self.generalise(self.graph, self.nodes, path)
            prevNode = newpath[0]
            prevBearing = startdirection
            #print ("General")
            for node in newpath:
                #print (str(node.x) + ", " + str(node.y))
                if not node==newpath[0]:
                    newBearing = 360*self.bearing(prevNode,node)/(2*pi);
                    instruct = ("turn",round(self.calcAngle(prevBearing, newBearing),0))
                    instructions.append(instruct)
                    dist=round(self.dist(prevNode,node)*5)
                    for i in range(round(dist/100)):
                        instruct = ("drive", 100,0)
                        instructions.append(instruct)
                    instruct = ("drive", dist%100,0)
                    instructions.append(instruct)
                    prevBearing = newBearing;
                prevNode=node
                
            instruct = ("turn",round(self.calcAngle(prevBearing, enddirection),0))
            instructions.append(instruct)
        return instructions

    def add_obsticle(self, coords, direction):
        print("add obsticle coords " + str(coords[0])+", "+ str(coords[1]) + ", " + str(direction) )
        boxlist = product([0], [0])
        if (direction<23) or (direction>=338):
            #0
            boxlist=product([-1,0,1],[0,-1])
        elif (direction<68) and (direction>=23):
            #45
            boxlist=[(-1,-1),(0,-2),(0,-1),(0,0),(1,-1),(1,0),(1,1),(2,0)]
        elif (direction<103) and (direction>=68):
            #90
            boxlist=product([0,1], [-1,0,1])#([-1,0,1],[0,-1])
        elif (direction<158) and (direction>=113):
            #135
            boxlist=[(-1,1),(0,2),(0,1),(0,0),(1,-1),(1,0),(1,1),(2,0)]
        elif (direction<203) and (direction>=158):
            #180
            boxlist=product([-1,0,1],[0,1])#boxlist=product([0,-1], [-1,0,1])
        elif (direction<248) and (direction>=203):
            #225
            boxlist=[(-2,0),(-1,-1),(-1,0),(-1,1),(0,0),(0,1),(0,2),(1,1)]#[(-1,-1),(0,-2),(0,-1),(0,0),(1,-1),(1,0),(1,1),(2,0)]
        elif (direction<293) and (direction>=248):
            #270
            boxlist=product([0,-1], [-1,0,1])
        elif (direction<338) and (direction>=293):
            #315
            boxlist=[(-2,0),(-1,-1),(-1,0),(-1,1),(0,-2),(0,-1),(0,0),(1,-1)]

        obsticle = []
        for m, n in boxlist:
            #print (str(m) + ", " + str(n))
            x = coords[0] + m
            y = coords[1] + n
            #print(str(x) + ", " + str(y))
            node=self.nodes[x][y]
            node.obst=True
            for i, j in product([-1, 0, 1], [-1, 0, 1]):
                if not (0 <= x + i < self.width):
                    continue
                
                if not (0 <= y + j < self.height):
                    continue

                if (self.nodes[x+i][y+j] in self.graph):
                    if (node in self.graph[self.nodes[x+i][y+j]]):
                        self.graph[self.nodes[x+i][y+j]].remove(node)
                        if node not in obsticle:
                            obsticle.append(node)


        for node in obsticle:
            print(str(node.x) + ", " + str(node.y))
        self.obsticles.append(obsticle)

    #deletes the last obsticle
    def delete_obsticle(self):        
        obsticle = self.obsticles[0]
        
        for node in obsticle:
            node.obst=False
            x=node.x
            y=node.y
            for i, j in product([-1, 0, 1], [-1, 0, 1]):
                if not (0 <= x + i < self.width):
                    continue
                
                if not (0 <= y + j < self.height):
                    continue

                if (self.nodes[x+i][y+j] in self.graph):
                    if (node not in self.graph[self.nodes[x+i][y+j]]):
                        self.graph[self.nodes[x+i][y+j]].append(node)
                        #print(str(x+i) + ", " + str(y+j))
    
        del self.obsticles[0]
