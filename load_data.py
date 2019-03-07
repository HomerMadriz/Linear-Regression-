import csv
import random as rd

def create_sample(src, dest, percentage):
    with open(dest, 'w', newline="") as new_file:
        new_file_writer = csv.writer(new_file)
        with open(src, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            line_count = 0
            for row in csv_reader:
                rand = rd.randint(0, 100) / 100
                if(rand <= percentage/100):
                    new_file_writer.writerow(row)
                    line_count += 1
    csv_file.close()
    new_file.close()
    print(f'New sample created with {line_count} lines')


def createRegMatrix(src):
    A = []
    Y = []
    with open(src, 'r') as csv_sample:
        csv_reader = csv.reader(csv_sample, delimiter="\t")
        for row in csv_reader:
            A.append([1] + [float(e) for e in row[:-1]])
            Y.append([float(row[-1])])
    return A, Y   

def createSets(src, train_percentage):
    with open("train_set", "w", newline="") as train_file:
        train_writer = csv.writer(train_file)
        with open("test_set", "w", newline="") as test_file:
            test_writer = csv.writer(test_file)
            with open(src, "r") as sample_file:
                sample_reader = csv.reader(sample_file)
                count_train = 0
                count_test = 0
                for row in sample_reader:
                    rand = rd.randint(0,100) / 100
                    if(rand <= train_percentage/100):
                        train_writer.writerow(row)
                        count_train +=1
                    else:
                        test_writer.writerow(row)
                        count_test +=1
    print(f"Train set created with {count_train} lines \n Test set created with {count_test} lines")
    train_file.close()
    test_file.close()
    sample_file.close()
