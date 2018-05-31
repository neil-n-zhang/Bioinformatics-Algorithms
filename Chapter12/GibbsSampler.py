#http://rosalind.info/problems/ba2g/
import numpy as np
from random import randint,choices
def score(motifs):
    sum_score=0
    for i in list(range(len(motifs[0]))):
        nucleotide,score=np.unique(motifs[:,i],return_counts=True)
        sum_score=sum_score+max(score)
    return sum_score

class seq():
    def __init__(self):
        self.dna_seqs=[]
        self.dna_num=np.array([])
        self.k=0
        self.t=0
        self.n=0

    def readdata(self,address):
        f=open(address,'r')
        [self.k,self.t,self.n]=list(map(int,f.readline().split()))
        self.dna_seqs=[line.rstrip() for line in f]
        self.dna_num=np.zeros([len(self.dna_seqs),len(self.dna_seqs[0])])
        for i in list(range(self.t)):
            for j in list(range(len(self.dna_seqs[0]))):
                if self.dna_seqs[i][j]=='A':
                    seq_num=0
                elif self.dna_seqs[i][j]=='T':
                    seq_num=1
                elif self.dna_seqs[i][j]=='C':
                    seq_num=2
                elif self.dna_seqs[i][j]=='G':
                    seq_num=3
                self.dna_num[i][j]=seq_num
        return

    def search_motif(self,seqs):
        motif=np.zeros([len(seqs),self.k])
        for i in list(range(len(seqs))):
            start=randint(0,len(seqs[0])-self.k)
            motif[i,:]=seqs[i,start:start+self.k]
        bestmotif=motif.copy()
        for j in list(range(self.n)):
            i=randint(0,self.t-1)
            profile_seq=np.delete(motif,i,0)
            profile_probability=np.zeros([4,len(profile_seq[0])])
            for m in list(range(len(profile_seq[0]))):
                nucleotide,counts=np.unique(profile_seq[:,m],return_counts=True)
                for nucleotide_num in nucleotide:
                    profile_probability[int(nucleotide_num),m]=counts[int(np.where(nucleotide==nucleotide_num)[0])]/sum(counts)

            probability=np.zeros(len(self.dna_num[0])-self.k+1)
            for m in list(range(len(probability))):
                raw_probability=1
                for num in list(range(self.k)):
                    motifseq_i=self.dna_num[i,m:m+self.k]
                    raw_probability=raw_probability*profile_probability[int(motifseq_i[num]),num]
                probability[m]=raw_probability+0.01
            start=choices(list(range(len(probability))),weights=probability)[0]
            motif[i,:]=self.dna_num[i,start:start+self.k]
            if score(motif)>score(bestmotif):
                bestmotif = motif.copy()
            bestmotif_seq=np.chararray((bestmotif.shape[0],bestmotif.shape[1]))
            bestmotif_seq[bestmotif==0]='A'
            bestmotif_seq[bestmotif == 1] = 'T'
            bestmotif_seq[bestmotif == 2] = 'C'
            bestmotif_seq[bestmotif == 3] = 'G'
        print(bestmotif_seq)
        return

a=seq()
a.readdata('D:\Bioinformatics_Algorithms\Chapter12\GibbsSampler.txt')
a.search_motif(a.dna_num)