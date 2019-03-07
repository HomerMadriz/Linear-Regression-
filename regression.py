import load_data as ld
import matrixOps as mops

def linear_regression(data_file,data_percentaje):
    ld.create_sample('new_file.csv', data_file, data_percentaje)
    A, Y = ld.createRegMatrix('new_file.csv')
    AT = mops.transMatrix(A)
    ATA = mops.mult_matrix(AT,A)
