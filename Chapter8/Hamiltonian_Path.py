from collections import defaultdict
class Graph():
    def __init__(self,vertex_num):
        self.edges=defaultdict(list)
        self.vnum=vertex_num

    def addEdges(self,v,u):
        self.edges[v].append(u)
        self.edges[u].append(v)

    def pathsearch(self,v,visited,path):
        visited[v]=True
        path.append(v)
        next_vertex=[x for x in self.edges[v] if visited[x]==False]
        if len(next_vertex)==0:
            return path
        else:
            for i in next_vertex:
                path=self.pathsearch(i,visited,path)
                if len(path)==self.vnum:
                    break
                else:
                    visited[i]=False
                    path.remove(i)
            return path

    def pathprint(self):
        for i in list(range(self.vnum)):
            visited = [False] * a.vnum
            path = []
            path = a.pathsearch(i, visited, path)
            if len(path)==self.vnum:
                print(path)

a=Graph(3)
a.addEdges(0,1)
a.addEdges(0,2)
a.addEdges(1,2)
a.pathprint()

a=Graph(4)
a.addEdges(0,1)
a.addEdges(1,3)
a.addEdges(1,2)
a.addEdges(2,3)
a.pathprint()

#(0)--(1)--(2)
# |   / \   |
# |  /   \  |
# | /     \ |
#(3)      (4)

a=Graph(5)
a.addEdges(0,1)
a.addEdges(0,3)
a.addEdges(1,3)
a.addEdges(1,2)
a.addEdges(1,4)
a.addEdges(2,4)
a.pathprint()