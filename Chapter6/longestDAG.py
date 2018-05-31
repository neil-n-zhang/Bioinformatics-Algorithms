#Longest Path in a Directed Acyclic Graph
#Dijkstra’s algorithm, adapted from https://algocoding.wordpress.com/2015/03/18/dijkstras-shortest-path-algorithm-part-1/
# 1->28:36 means there are 36 steps from point 1 to point 28

import numpy as np
import heapq
f=open('D:\Bioinformatics_Algorithms\Chapter6\dataset_245_7.txt','r')
data=f.readlines()

start=int(data[0].rstrip())
end=int(data[1].rstrip())

graph=np.zeros([len(data)-2,3])
for i in list(range(len(graph))):
    line=data[i+2].rstrip().split('->')
    graph[i,0]=int(line[0])
    graph[i,1:]=list(map(int,line[1].split(':')))

graph=graph[np.lexsort((graph[:,1],graph[:,0]))]
disgraph={}
group=graph[0,0]
disgraph[group]=[]
for line in graph:
    if line[0]==group:
        disgraph[group].append((line[1],line[2]))
    else:
        group=line[0]
        disgraph[group]=[(line[1],line[2])]

maxpoint=int(max(graph[:,1]))

pred={x:x for x in list(range(maxpoint+1))}
dist={x:0 for x in list(range(maxpoint+1))}
PQ=[]
heapq.heappush(PQ,[dist[start],start])
while(PQ):
    u=heapq.heappop(PQ)
    u_dist=u[0]
    u_id = u[1]
    if u_dist == dist[u_id]:
            #if u_id == target:
            #    break
        if u_id in disgraph:
            for v in disgraph[u_id]:
                v_id = v[0]
                w_uv = v[1]
                if dist[u_id]+w_uv>dist[v_id]:
                    dist[v_id] = dist[u_id] + w_uv
                    heapq.heappush(PQ, [dist[v_id], v_id])
                    pred[v_id] = u_id

print(int(dist[end]))
path=[end]
node=end
while start!=node:
    node=pred[node]
    path.append(int(node))

spath=''
for node in path[-1:0:-1]:
    spath=spath+str(node)+'->'
spath=spath+str(path[0])
print(spath)