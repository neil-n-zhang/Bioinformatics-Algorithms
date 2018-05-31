#http://rosalind.info/problems/ba7c/
import heapq
import numpy as np
import copy
from itertools import combinations

def readdata(address):
    f=open(address,'r')
    text=f.readlines()
    f.seek(0)
    n=list(map(int,f.readline().split()))[0]
    data=np.zeros([len(text)-1,n])
    for i in list(range(1,len(text))):
        data[i-1,:]=list(map(float,text[i].split()))
    return data

def isadditive(data):
    for num in list(combinations(list(range(len(data))),4)):
        len_sum=np.zeros(3)
        len_sum[0]=data[num[0],num[1]]+data[num[2],num[3]]
        len_sum[1] = data[num[0], num[2]] + data[num[1], num[3]]
        len_sum[2] = data[num[2], num[1]] + data[num[0], num[3]]
        unique_index=np.unique(len_sum,return_index=True)[1]
        dup_index=np.setdiff1d([0,1,2],unique_index)
        if len(dup_index)==1:
            if sum(len_sum[dup_index]<len_sum[unique_index]):
                return False
        else:
            return False
    return True

def limb(data,n):
    node_list=list(range(len(data)))
    node_list.pop(n)
    limblength_all=[]
    for i,k in list(combinations((node_list),2)):
        limblength=(data[n,i]+data[n,k]-data[i,k])/2
        heapq.heappush(limblength_all,[limblength,i,k])
    limblength,i,k=heapq.heappop(limblength_all)
    return limblength,i,k

def pathsearch(start,end,node1, edge1):
    node=copy.deepcopy(node1)
    edge=copy.deepcopy(edge1)
    for nextnode in node[start]:
        if nextnode==end:
            route_node.append(end)
            route_edge.append(edge[start][node[start].index(nextnode)])
            break
        else:
            route_node.append(nextnode)
            route_edge.append(edge[nextnode][node[nextnode].index(start)])
            edge[nextnode].remove(edge[nextnode][node[nextnode].index(start)])
            node[nextnode].remove(start)
            if len(node[nextnode])==0:
                route_node.pop()
                route_edge.pop()
                continue
            else:
                pathsearch(nextnode,end,node1, edge1)
                if route_node[-1]==end:
                    break
                else:
                    route_node.pop()
                    route_edge.pop()
    return

def additivephy(data1):
    data=data1.copy()
    n=len(data)-1
    if n==1:
        return {0:[1],1:[0]}, {0:[data[0][1]],1:[data[1][0]]}
    elif not isadditive(data):
        return 'Not additive.','Not additive.'

    limblength,i1,k1=limb(data,n)
    for j in list(range(n)):
        data[j,n]=data[j,n]-limblength
        data[n, j]=data[n, j]-limblength

    x=data[i1,n]
    y=data[n,k1]
    data=data[:-1,:-1]
    tree_node, tree_edge=additivephy(data)
    global route_node,route_edge
    route_node = [i1]
    route_edge = []

    pathsearch(i1,k1,tree_node, tree_edge)

    if x>sum(route_edge):
        tree_node[n]=[i1,k1]
        tree_edge[n]=[x+limblength,y+limblength]
        tree_node[i1].append(n)
        tree_edge[i1].append(x + limblength)
        tree_node[k1].append(n)
        tree_edge[k1].append(y + limblength)
    else:
        if limblength==0:
            totaledge_length=0
            for edgenum in list(range(len(route_edge))):
                totaledge_length=totaledge_length+route_edge[edgenum]
                if totaledge_length==x:
                    break
                elif totaledge_length>x:
                    tree_node[n] = [route_node[edgenum], route_node[edgenum+1]]
                    tree_edge[n] = [x - (totaledge_length-route_edge[edgenum]), totaledge_length-x]

                    tree_node[route_node[edgenum]].append(n)
                    tree_node[route_node[edgenum+1]].append(n)
                    tree_edge[route_node[edgenum]].append(x - (totaledge_length-route_edge[edgenum]))
                    tree_edge[route_node[edgenum + 1]].append(totaledge_length-x)

                    tree_node[route_node[edgenum]].pop(tree_node[route_node[edgenum]].index(route_node[edgenum + 1]))
                    tree_edge[route_node[edgenum]].pop(tree_edge[route_node[edgenum]].index(route_edge[edgenum]))
                    tree_node[route_node[edgenum + 1]].pop(tree_node[route_node[edgenum + 1]].index(route_node[edgenum]))
                    tree_edge[route_node[edgenum + 1]].pop(tree_edge[route_node[edgenum + 1]].index(route_edge[edgenum]))
        else:
            totaledge_length = 0
            for edgenum in list(range(len(route_edge))):
                totaledge_length = totaledge_length + route_edge[edgenum]
                if totaledge_length == x:
                    tree_node[n] = [route_node[edgenum+1]]
                    tree_edge[n] =[limblength]
                    tree_node[route_node[edgenum+1]].append(n)
                    tree_edge[route_node[edgenum + 1]].append(limblength)
                elif totaledge_length > x:
                    global totalvertex_num
                    totalvertex_num=totalvertex_num+1
                    tree_node[totalvertex_num] = [route_node[edgenum], route_node[edgenum + 1]]
                    tree_edge[totalvertex_num] = [x - (totaledge_length - route_edge[edgenum]), totaledge_length - x]

                    tree_node[route_node[edgenum]].pop(tree_node[route_node[edgenum]].index(route_node[edgenum+1]))
                    tree_edge[route_node[edgenum]].pop(tree_edge[route_node[edgenum]].index(route_edge[edgenum]))
                    tree_node[route_node[edgenum + 1]].pop(tree_node[route_node[edgenum+1]].index(route_node[edgenum]))
                    tree_edge[route_node[edgenum + 1]].pop(tree_edge[route_node[edgenum+1]].index(route_edge[edgenum]))

                    tree_node[route_node[edgenum]].append(totalvertex_num)
                    tree_node[route_node[edgenum + 1]].append(totalvertex_num)
                    tree_edge[route_node[edgenum]].append(x - (totaledge_length - route_edge[edgenum]))
                    tree_edge[route_node[edgenum + 1]].append(totaledge_length - x)

                    tree_node[n] = [totalvertex_num]
                    tree_edge[n] = [limblength]
                    tree_node[totalvertex_num].append(n)
                    tree_edge[totalvertex_num].append(limblength)
    return tree_node, tree_edge


#end of function
data=readdata('D:\Bioinformatics_Algorithms\Chapter10\AdditivePhylogeny.txt')
totalvertex_num=len(data)-1
tree_node=[]
tree_edge=[]
additivephy(data)


#test pathsearch
i1=0
k1=2
tree_node1={0:[4],1:[4],2:[5],3:[5],4:[0,1,5],5:[2,3,4,6],6:[5]}
tree_edge1={0:[3],1:[1],2:[5],3:[4],4:[3,1,2],5:[5,4,2,1],6:[1]}
route_node=[i1]
route_edge=[]
pathsearch(i1,k1,tree_node1, tree_edge1)
