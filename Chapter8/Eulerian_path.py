#Fleury’s Algorithm for printing Eulerian Path or Circuit
#https://www.geeksforgeeks.org/fleurys-algorithm-for-printing-eulerian-path/
from collections import defaultdict
class Graph():
    def __init__(self,vertex_num):
        self.edges=defaultdict(list)
        self.vnum=vertex_num

    def addEdges(self,v,u):
        self.edges[v].append(u)
        self.edges[u].append(v)

    def rmEdges(self,v,u):
        for index,val in enumerate(self.edges[v]):
            if val==u:
                self.edges[v].pop(index)

        for index,val in enumerate(self.edges[u]):
            if val==v:
                self.edges[u].pop(index)


    def DFScount(self,u,visited):
        count=1
        visited[u]=True
        for i in self.edges[u]:
            if visited[i]==False:
                count=count+self.DFScount(i,visited)
        return count

    def route(self,v):
        if len(self.edges[v])==1:
            u=self.edges[v][0]
            self.rmEdges(v,u)
            return u
        else:
            for u in self.edges[v]:
                visited=[False]*self.vnum
                count1=self.DFScount(u,visited)
                self.rmEdges(v,u)
                visited = [False] * self.vnum
                count2 = self.DFScount(u, visited)
                if count1==count2:
                    return u
                else:
                    self.addEdges(v,u)

    def printpath(self):
        degree=[0]*self.vnum
        for i in list(range(self.vnum)):
            if self.edges[i]==0:
                print('One vertex is not connected.')
                return
            else:
                degree[i]=len(self.edges[i])%2
        if sum(degree)==0:
            vertex1=0
            print(vertex1)
            while len(self.edges[vertex1])!=0:
                vertex2=self.route(vertex1)
                print(vertex2)
                vertex1=vertex2
            return
        elif sum(degree)==2:
            vertex1=degree.index(1)
            print(vertex1)
            while len(self.edges[vertex1]) != 0:
                vertex2 = self.route(vertex1)
                print(vertex2)
                vertex1 = vertex2
            return


a=Graph(3)
a.addEdges(0,1)
a.addEdges(0,2)
a.addEdges(1,2)

g3=Graph(5);
g3.addEdges(1, 0);
g3.addEdges(0, 2);
g3.addEdges(2, 1);
g3.addEdges(0, 3);
g3.addEdges(3, 4);
g3.addEdges(3, 2);
g3.addEdges(3, 1);
g3.addEdges(2, 4);
g3.printpath()
