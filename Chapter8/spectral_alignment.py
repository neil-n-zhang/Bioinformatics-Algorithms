import numpy as np
def alignmatrix(spec1,spec2):
    matrix=np.zeros([max(spec1)+1,max(spec2)+1])
    for i in spec1:
        for j in spec2:
            matrix[i,j]=1
    return matrix

def score(matrix):
    score_mat=np.zeros([matrix.shape[0]+1,matrix.shape[1]+1])
    for i in list(range(2,score_mat.shape[0])):
        for j in list(range(2,score_mat.shape[1])):
            score1=score_mat[i-1,j]
            score2=score_mat[i,j-1]
            if matrix[i-1,j-1]==1:
                score3=score_mat[i-1,j-1]+1
            else:
                score3 = score_mat[i - 1, j - 1]
            score_mat[i, j]=max(score1,score2,score3)
    return score_mat


spec1=[1,2,3,6,7]
spec2=[1,2,3,5,6]
matrix=alignmatrix(spec1,spec2)
score_mat=score(matrix)