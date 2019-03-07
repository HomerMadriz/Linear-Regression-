import load_data as ld
import matrixOps as mops

def linear_regression(data_file):
    A, Y = ld.createRegMatrix('data_file')
    At = mops.transMatrix(A)
    AtA = mops.mult_matrix(At,A)
    AtY = mops.mult_matrix(At, Y)

    for i in range(len(AtY)):
        AtA[i].append(AtY[i][0])

    mops.printMatrix(AtA)
    print()
    mops.printMatrix(AtY)

    b_vector = mops.gauss_solve(AtA)

    mops.printMatrix(b_vector)

    return b_vector

def test(test_file, b_vector):
    A, Y = ld.createRegMatrix(test_file)
    