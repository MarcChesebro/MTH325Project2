#########################################################
#
# Python 3.6
# Author: Marc Chesebro
#
#########################################################


#edge object containing the start and end point
class edge(object):
    def __init__(self, vertA, vertB, weight):
        self.A = vertA
        self.B = vertB
        self.w = weight

class vertex(object):
    def __init__(self, label):
        self.label = label
        self.pathLength = -1

#function to find the degree of a vertex given a name
#and list of edges
def findDegree(vert, edgeList):
    deg = 0
    for e in edgeList:
        if(e.A == vert or e.B == vert):
            deg = deg + 1
    return deg

#checks if val is in the list
def contains(val, list):
    for i in list:
        if i == val:
            return True
    return False

def labelToVertex(label, vertList):
    for v in vertList:
        if v.label == label:
            return v
    return -1

def findMinTree(vertList, edgeList):
    sortEdge = sorted(edgeList, key=lambda edge: edge.age)
    tree = []
    verts = []

    for edge in edgeList:
        if(not(contains(edge.A, verts) and contains(edge.B, verts))):
            if(contains(edge.A, verts)):
                verts.append(edge.B)
                tree.append(edge)
            elif(contains(edge.B, verts)):
                verts.append(edge.A)
                tree.append(edge)
    print(tree)
    return tree

def findMinLength(VertList, edgeList):
    i = 0
    curr = VertList[i]
    vertVisited = [curr]
    curr.pathLength = 0

    while len(vertVisited) < len(VertList):

        # find all vert next to it
        for e in edgeList:
            if e.A.label == curr.label:
                if e.B.pathLength >= (curr.pathLength + e.w) or e.B.pathLength == -1:
                    e.B.pathLength = curr.pathLength + e.w
            if e.B.label == curr.label:
                if e.A.pathLength >= (curr.pathLength + e.w) or e.A.pathLength == -1:
                    e.A.pathLength = curr.pathLength + e.w

        # pick vert to visit
        if len(vertVisited) < len(VertList):
            min = -1
            smallest = curr
            for v in VertList:
                if not contains(v, vertVisited) and v.pathLength != -1:
                    if min == -1:
                        min = v.pathLength
                        smallest = v
                    elif v.pathLength < min:
                        min = v.pathLength
                        smallest = v

            curr = smallest
            # add vert to list of Visited verts
            vertVisited.append(curr)

#get user input
userVerts = input("enter the vertices(a, b, c): \n")
userEdges = input("enter the edges(a-b, b-c): \n")

#get rid of spaces and split on commas
userVerts = userVerts.replace(" ", "")
userEdges = userEdges.replace(" ", "")

vertsStr = userVerts.split(',')
edgesStr = userEdges.split(',')

verts = []
for str in vertsStr:
    verts.append(vertex(str))

#turn the edge strings into a list of edge objects
edges = []
for str in edgesStr:
    tempV = str.split('-')
    edges.append(edge(labelToVertex(tempV[0], verts), labelToVertex(tempV[1], verts) , int(tempV[2])))

findMinLength(verts, edges)

for v in verts:
    print(v.label, v.pathLength)