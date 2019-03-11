import load_data as ld
import matrixOps as mops

def linear_regression(data_file):
    A, Y = ld.createRegMatrix(data_file)
    At = mops.transMatrix(A)
    AtA = mops.mult_matrix(At,A)
    AtY = mops.mult_matrix(At, Y)

    for i in range(len(AtY)):
        AtA[i].append(AtY[i][0])

    b_vector = mops.gauss_solve(AtA)

    print("b_vector: ")
    mops.printMatrix(b_vector)

    return b_vector

def test(test_file, b_vector):
    A, Y = ld.createRegMatrix(test_file)
    Y_est = mops.dotProduct(A, b_vector)
    RMSE = 0
    
    if (len(Y) != len(Y_est)):
        return -1
    
    for i in range(len(Y)):
        RMSE += (Y_est[i] - Y[i][0])
    
    RMSE = (RMSE / len(Y))**(1/2)

    print(f"RMSE = {RMSE}")

    return RMSE

    