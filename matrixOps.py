def mult_matrix(A, B):
    res = []
    if(len(A[0]) != len(B)):
        return -1
    else:
        for i in range(len(A)):
            res.append([0 for i in range(len(B[0]))])
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


def gauss_solve(A):
    """Gaussian eliminator method  Author: j9ac9k (github member)
    url: https://gist.github.com/j9ac9k/6b5cd12aa9d2e5aa861f942b786293b4"""
    m = len(A)
    assert all([len(row) == m + 1 for row in A[1:]]), "Matrix rows have non-uniform length"
    n = m + 1
    
    for k in range(m):
        pivots = [abs(A[i][k]) for i in range(k, m)]
        i_max = pivots.index(max(pivots)) + k
        
        # Check for singular matrix
        assert A[i_max][k] != 0, "Matrix is singular!"
        
        # Swap rows
        A[k], A[i_max] = A[i_max], A[k]
        
        for i in range(k + 1, m):
            f = A[i][k] / A[k][k]
            for j in range(k + 1, n):
                A[i][j] -= A[k][j] * f

            # Fill lower triangular matrix with zeros:
            A[i][k] = 0
    
    # Solve equation Ax=b for an upper triangular matrix A         
    x = []
    for i in range(m - 1, -1, -1):
        x.insert(0, A[i][m] / A[i][i])
        for k in range(i - 1, -1, -1):
            A[k][m] -= A[k][i] * x[0]
    return x

def printMatrix(M):
    for i in M:
        print(i)
    print()

def dotProduct(M,V):
    result = []
    sum = 0
    if(len(M[0]) != len(V)):
        return -1

    for i in range(len(M)):
        for j in range(len(M[0])):
           sum += (M[i][j] * V[j])
        result.append(sum)
        sum = 0
    return result

