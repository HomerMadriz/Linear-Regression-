import regression as reg
import load_data as ld


ld.create_sample('airfoil_self_noise_.csv','new_file.csv', 10)
ld.createSets('new_file.csv', 75)
b_vector = reg.linear_regression('train_set.csv')
error = reg.test("test_set.csv", b_vector)
