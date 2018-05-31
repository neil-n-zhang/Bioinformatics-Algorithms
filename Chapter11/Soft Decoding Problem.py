#http://rosalind.info/problems/ba10j/
import numpy as np
class hmm():
    def __init__(self):
        self.em_string=[]
        self.em_char =['x','y','z']
        self.states=['A','B']
        self.tran_mat=np.array([(0.911,0.089),(0.228,0.772)])
        self.em_matrix=np.array([(0.356,0.191,0.453),(0.04,0.467,0.493)])

        self.score=np.array([])
        self.stat_score=np.array([])
        self.fore_score=np.array([])
        self.back_score = np.array([])

    def addstring(self,string):
        for i in list(range(len(string))):
            for j in list(range(len(self.em_char))):
                if string[i]==self.em_char[j]:
                    self.em_string.append(j)

    def calc_score(self):
        self.score=np.zeros([len(self.states),len(self.em_string)])
        self.fore_score=np.zeros([len(self.states),len(self.em_string)])
        self.back_score=np.zeros([len(self.states),len(self.em_string)])
        self.stat_score=np.zeros([len(self.states),len(self.em_string)])

        for i in list(range(self.score.shape[0])):
            self.fore_score[i,0]=self.em_matrix[i,self.em_string[0]]
            #self.score[i,0]=self.em_matrix[i,self.em_string[0]]
            self.back_score[i,-1]=1

        for j in list(range(1,self.score.shape[1])):
            for i in list(range(self.score.shape[0])):
                #rawscore=[]
                fore_rawscore=[]
                back_rawscore = []
                for k in list(range(self.score.shape[0])):
                    #rawscore.append(self.score[k,j-1]*self.tran_mat[k,i])
                    fore_rawscore.append(self.fore_score[k,j-1]*self.tran_mat[k,i])
                    back_rawscore.append(self.back_score[k, -j] * self.tran_mat[i, k]*self.em_matrix[k,self.em_string[-j]])
                #self.score[i,j]=max(rawscore)*self.em_matrix[i,self.em_string[j]]
                self.fore_score[i,j]=sum(fore_rawscore)*self.em_matrix[i,self.em_string[j]]
                self.back_score[i,-(j+1)]=sum(back_rawscore)

        for j in list(range(self.score.shape[1])):
            px=sum(self.fore_score[:,j]*self.back_score[:,j])
            for i in list(range(self.score.shape[0])):
                self.stat_score[i,j]=self.fore_score[i,j]*self.back_score[i,j]/px

a=hmm()
a.addstring('zyxxxxyxzz')
a.calc_score()
a.stat_score

print(a.states)
for i in list(range(a.stat_score.shape[1])):
    print(a.stat_score[:,i])