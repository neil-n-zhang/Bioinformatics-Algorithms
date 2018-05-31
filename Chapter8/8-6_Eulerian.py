#Fleury’s Algorithm for printing Eulerian Path or Circuit
#https://www.geeksforgeeks.org/fleurys-algorithm-for-printing-eulerian-path/
from collections import defaultdict
class vertex():
    def __init__(self):
        self.inedge=[]
        self.outedge =[]
        self.verseq=''

class Graph():
    def __init__(self):
        self.v={}
        self.vnum=len(self.v)

    def addEdges(self,seq):
        prefix=seq[:-1]
        suffix=seq[1:]
        if not prefix in self.v:
            self.v[prefix]=vertex()
        if not suffix in self.v:
            self.v[suffix]=vertex()
        self.v[prefix].outedge.append(suffix)
        self.v[suffix].inedge.append(prefix)


    def rmEdges(self,vertex,next_ver):
        for index,val in enumerate(self.v[vertex].outedge):
            if val==next_ver:
                self.v[vertex].outedge.pop(index)

        for index,val in enumerate(self.v[next_ver].inedge):
            if val==vertex:
                self.v[next_ver].inedge.pop(index)


    def DFScount(self,vertex,visited):
        count=1
        visited[vertex]=True
        for i in self.v[vertex].outedge:
            if visited[i]==False:
                count=count+self.DFScount(i,visited)
        return count

    def route(self,vertex):
        if len(self.v[vertex].outedge)==1:
            next_ver=self.v[vertex].outedge[0]
            self.rmEdges(vertex,next_ver)
            return next_ver
        else:
            visited={}
            for next_ver in self.v[vertex].outedge:
                for key in list(a.v.keys()):
                    visited[key] = False
                count1=self.DFScount(vertex,visited)
                self.rmEdges(vertex,next_ver)
                for key in list(a.v.keys()):
                    visited[key] = False
                count2 = self.DFScount(vertex, visited)
                if count1==count2:
                    return next_ver
                else:
                    self.addEdges(vertex+next_ver[-1])

    def printpath(self):
        wholeseq=[]
        indegree={}
        outdegree = {}
        for i in self.v:
            indegree[i] = len(self.v[i].inedge)
            outdegree[i] = len(self.v[i].outedge)
            if indegree[i]==0 and outdegree[i]==0:
                print('One vertex is not connected.')
                return
        degreediff=[]
        for i,j in zip(indegree.values(),outdegree.values()):
            degreediff.append(i-j)

        if sum(list(map(abs,degreediff)))==0:
            vertex1=list(indegree.keys())[0]
            wholeseq.append(vertex1)
            while len(self.v[vertex1].outedge)!=0:
                vertex2=self.route(vertex1)
                wholeseq.append(vertex2[-1])
                vertex1=vertex2
            print(''.join(wholeseq))
            return
        elif sum(list(map(abs,degreediff)))==2:
            vertex1 = list(indegree.keys())[degreediff.index(-1)]
            wholeseq.append(vertex1)
            while len(self.v[vertex1].outedge)!=0:
                vertex2=self.route(vertex1)
                wholeseq.append(vertex2[-1])
                vertex1 = vertex2
            print(''.join(wholeseq))
            return

seq=['AGT', 'AAA', 'ACT', 'AAC', 'CTT', 'GTA', 'TTT', 'TAA']
a=Graph()
for x in seq:
    a.addEdges(x)
a.printpath()

