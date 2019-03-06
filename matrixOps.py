import load_data as ld

def mult_matrix(A, B):
    res = []
    if(len(A[0]) != len(B)):
        return -1
    else:
        for i in range(len(A)):
            res.append([0 for i in range(len(A))])
            for j in range(len(B[0])):
                for k in range(len(B)):
                    res[i][j] += (A[i][k] * B[k][j])
    return res 

def transMatrix(A):
    AT = []
    for i in range(len(A[0])):
        AT.append([0 for i in range(len(A))])
        for j in range(len(A)):
            AT[i][j] = A[j][i]
    return AT

ld.create_sample('new_file.csv', 'airfoil_self_noise_.csv', 10)
A, Y = ld.createRegMatrix('new_file.csv')
AT = transMatrix(A)
for i in range(len(A)):
    print(A[i])
for i in range(len(AT)):
    print(AT[i])

ATA = mult_matrix(AT,A)
for i in range(len(ATA)):
    print(ATA[i])
'''
C = [[1,1,1,1],[2,3,5,6],[4,9,25,36]]
D = [[1,2,4],[1,3,9],[1,5,25], [1,6,36]]

result = mult_matrix(C,D)
'''
