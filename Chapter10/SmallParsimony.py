from collections import defaultdict
import numpy as np
from math import log2

class seqtree():
    def __init__(self):
        layer=lambda:defaultdict(list)
        score = lambda: defaultdict(list)
        connection=lambda:defaultdict(list)
        self.layers=defaultdict(layer)
        self.scores=defaultdict(score)
        self.connections=defaultdict(connection)
        self.leaf_num=0
        self.node_num=0

    def readdata(self,path):
        f=open(path,'r')
        self.leaf_num=int(f.readline().split()[0])
        for i in list(range(self.leaf_num)):
            n,seq=f.readline().split('->')
            n=int(n)
            self.layers[0][n].append(seq[:-1])
            score = np.full((4, len(seq[:-1])), np.inf)
            for i in list(range(len(seq[:-1]))):
                if seq[i]=='A':
                    score[0,i]=0
                elif seq[i]=='T':
                    score[1,i]=0
                elif seq[i]=='C':
                    score[2,i]=0
                else:
                    score[3, i] = 0
            self.scores[0][n].append(score)
        for i in list(range(2,int(log2(self.leaf_num))+1)):
            for j in list(range(int(self.leaf_num/2**(i-1)))):
                vertex1,vertex2=f.readline().split('->')
                vertex1=int(vertex1)
                vertex2 = int(vertex2)
                self.connections[i][vertex1].append(vertex2)

        self.node_num=max(self.layers[0].keys())

    def commenseq(self,score1,score2):
        score=np.zeros(score1.shape)
        seq=''
        for j in list(range(score1.shape[1])):
            for i in [0, 1, 2, 3]:
                min1=score1[:,j]+1
                min1[i]-=1
                min1=min(min1)
                min2 = score2[:, j] + 1
                min2[i] -= 1
                min2=min(min2)
                score[i,j]=min1+min2
            if score[:,j].argmin()==0:
                seq+='A'
            if score[:,j].argmin()==1:
                seq+='T'
            if score[:, j].argmin() == 2:
                seq += 'C'
            if score[:,j].argmin()==3:
                seq+='G'
        return seq,score

    def generatetree(self):
        for n in self.layers[0]:
            seq, score = self.commenseq(self.scores[0][n][0],self.scores[0][n][1])
            self.layers[1][n].append(seq)
            self.scores[1][n].append(score)

        for i in list(range(2,int(log2(self.leaf_num))+1)):
            for n in self.connections[i]:
                son1=self.connections[i][n][0]
                son2=self.connections[i][n][1]
                seq,score=self.commenseq(self.scores[i-1][son1][0],self.scores[i-1][son2][0])
                self.layers[i][n].append(seq)
                self.scores[i][n].append(score)

a = seqtree()
a.readdata('D:\Bioinformatics_Algorithms\Chapter10\smallparsimony.txt')
a.generatetree()