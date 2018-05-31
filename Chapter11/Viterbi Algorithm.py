#http://rosalind.info/problems/ba10c/
import numpy as np
class hmm():
    def __init__(self):
        self.em_string=[]
        self.em_char =['x','y','z']
        self.states=['A','B']
        self.tran_mat=np.log10(np.array([(0.634,0.366),(0.387,0.613)]))
        self.em_matrix=np.log10(np.array([(0.532,0.226,0.241),(0.457,0.192,0.351)]))

        self.score=np.array([])
        self.backtrace=np.array([])

    def addstring(self,string):
        for i in list(range(len(string))):
            for j in list(range(len(self.em_char))):
                if string[i]==self.em_char[j]:
                    self.em_string.append(j)

    def calc_score(self):
        self.score=np.zeros([len(self.states),len(self.em_string)])
        self.backtrace=np.zeros([len(self.states),len(self.em_string)-1])
        for i in list(range(self.score.shape[0])):
            self.score[i,0]=self.em_matrix[i,self.em_string[0]]
        for j in list(range(1,self.score.shape[1])):
            for i in list(range(self.score.shape[0])):
                rawscore=[]
                for k in list(range(self.score.shape[0])):
                    rawscore.append(self.score[k,j-1]+self.tran_mat[k,i])
                self.score[i,j]=max(rawscore)+self.em_matrix[i,self.em_string[j]]
                self.backtrace[i,j-1]=rawscore.index(max(rawscore))

    def printroute(self):
        #route=[self.states[self.score[:,-1].argmax()]]
        route=[self.score[:,-1].argmax()]
        trans=int(self.backtrace[route[-1],-1])
        for i in list(range(2,len(self.em_string)+1)):
            route.append(trans)
            if i==len(self.em_string):
                break
            trans=int(self.backtrace[route[-1],-i])
        route=route[::-1]
        route_char=[]
        for num in route:
            route_char.append(self.states[num])
        return ''.join(route_char)


a=hmm()
a.addstring('zxxxxy')
a.calc_score()
a.em_string
a.score
a.backtrace
a.printroute()