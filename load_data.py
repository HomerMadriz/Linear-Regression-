import csv
import random as rd

def create_sample(src, dest, percentage):
    with open(src, 'w', newline="") as new_file:
        new_file_writer = csv.writer(new_file)
        with open(dest, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            line_count = 0
            for row in csv_reader:
                rand = rd.randint(0, 100) / 100
                if(rand <= percentage/100):
                    new_file_writer.writerow(row)
                    print(row)
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
            Y.append(float(row[-1]))
    return A, Y   



