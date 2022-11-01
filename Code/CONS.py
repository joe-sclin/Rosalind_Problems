import argparse
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument('s', type=str)

currDNA = ''
matrix = np.zeros((1, 1))  # Initiate matrix object with minimum size
with open(parser.parse_args().s) as f: lines = f.readlines()
for i in range(len(lines)):
    s = lines[i].strip()
    if s[0] == '>' or i == len(lines) - 1:
        if i == len(lines) - 1:
            currDNA += s
        if currDNA != '':
            if matrix.shape[1] == 1:
                matrix = np.zeros((4, len(currDNA))).astype(int)  # Initiate profile matrix with length of 1st DNA
            for j in range(len(currDNA)):
                if currDNA[j] == 'A': matrix[0, j] += 1
                if currDNA[j] == 'C': matrix[1, j] += 1
                if currDNA[j] == "G": matrix[2, j] += 1
                if currDNA[j] == "T": matrix[3, j] += 1
            currDNA = ''
    else:
        currDNA += s

DNA = ['A:', 'C:', 'G:', 'T:']
constr = ''
for i in range(matrix.shape[1]):    # Construct consensus string
    constr += DNA[np.argmax(matrix[:, i])][:1]
print(constr)
for i in range(matrix.shape[0]):    # Output profile matrix
    print(DNA[i], *matrix[i])
# Numpy module is imported to create and process matrix object easier
