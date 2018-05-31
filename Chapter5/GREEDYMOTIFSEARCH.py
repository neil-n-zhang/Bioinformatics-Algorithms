DNA=['GGCGTTCAGGCA',
'AAGAATCAGTCA',
'CAAGGAGTTCGC',
'CACGTCAATCAC',
'CAATAATATTCG']

def seq2matrix(DNA):
    import numpy as np
    seq=np.zeros((len(DNA),len(DNA[0])))
    for i in list(range(len(DNA))):
        for j in list(range(len(DNA[0]))):
            if DNA[i][j]=='A':
                seq[i,j]=1
            if DNA[i][j]=='T':
                seq[i,j]=2
            if DNA[i][j]=='C':
                seq[i,j]=3
            if DNA[i][j]=='G':
                seq[i,j]=4
    return seq

#total number of nucleotides that are the same in each column
def score(s,i,l,seq):
    motif=np.zeros((i,l))
    for j in list(range(i)):
        motif[j]=seq[j,s[j]:s[j]+l]
    profile=np.zeros((4,l))
    for j in list(range(4)):
        for k in list(range(l)):
            profile[j,k]=np.count_nonzero(motif[:,k]==j+1)
    return sum(np.amax(profile,axis=0))


def motifsearch(DNA,l):
    t=len(DNA)
    n=len(DNA[0])
    seq=seq2matrix(DNA)
    bestmotif=np.zeros(t).astype(int)
    s=np.zeros(t).astype(int)
    for s[0] in list(range(n-l+1)):
        for s[1] in list(range(n-l+1)):
            if score(s,2,l,seq)>score(bestmotif,2,l,seq):
                bestmotif=s.copy()
    s=bestmotif.copy()
    for i in list(range(2,t)):
        for s[i] in list(range(n-l+1)):
            if score(s,i+1,l,seq)>score(bestmotif,i+1,l,seq):
                bestmotif=s.copy()
        s = bestmotif.copy()

    motif=np.zeros((len(bestmotif),l))
    for i in list(range(len(motif))):
        motif[i]=seq[i,bestmotif[i]:bestmotif[i]+l]
    return motif.astype(int)


motif=motifsearch(DNA,3)
lettermotif=np.chararray((len(motif),len(motif[0])))
for i in list(range(len(motif))):
    for j in list(range(len(motif[0]))):
        if motif[i][j]==1:
            lettermotif[i,j]='A'
        if motif[i][j]==2:
            lettermotif[i,j]='T'
        if motif[i][j]==3:
            lettermotif[i,j]='C'
        if motif[i][j]==4:
            lettermotif[i,j]='G'