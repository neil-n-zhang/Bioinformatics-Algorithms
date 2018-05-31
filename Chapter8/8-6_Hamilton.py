from collections import defaultdict
class Graph():
    def __init__(self,vertex_num):
        self.edges=defaultdict(list)
        self.vnum=vertex_num

    def addEdges(self,v,u):
        self.edges[v].append(u)

    def addseq(self,seq):
        for i in list(range(self.vnum)):
            for j in list(range(self.vnum)):
                if i==j:
                    continue
                else:
                    if seq[i][1:]==seq[j][:-1]:
                        self.addEdges(i,j)


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
                whole_seq=[seq[path[0]]]
                for j in list(range(1,len(path))):
                    whole_seq.append(seq[path[j]][-1])
                print(''.join(whole_seq))

seq=['AGT', 'AAA', 'ACT', 'AAC', 'CTT', 'GTA', 'TTT', 'TAA']
a=Graph(len(seq))
a.addseq(seq)
a.pathprint()