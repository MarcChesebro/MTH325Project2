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

#get user input
userVerts = input("enter the vertices(a, b, c): \n")
userEdges = input("enter the edges(a-b, b-c): \n")

#get rid of spaces and split on commas
userVerts = userVerts.replace(" ", "")
userEdges = userEdges.replace(" ", "")

verts = userVerts.split(',')
edgesStr = userEdges.split(',')

#turn the edge strings into a list of edge objects
edges = []
for str in edgesStr:
    tempV = str.split('-')
    edges.append(edge(tempV[0], tempV[1], tempV[2]))
