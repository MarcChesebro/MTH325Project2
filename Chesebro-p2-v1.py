#########################################################
#
# Python 3.6
# Author: Marc Chesebro
#
#########################################################


#edge object containing the start and end point
class edge(object):
    def __init__(self, vertA, vertB):
        self.A = vertA
        self.B = vertB


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
    edges.append(edge(tempV[0], tempV[1]))