import argparse

parser = argparse.ArgumentParser()
parser.add_argument('k', type=int)
parser.add_argument('m', type=int)
parser.add_argument('n', type=int)

k = parser.parse_args().k
m = parser.parse_args().m
n = parser.parse_args().n

t = k+m+n
pr = (k/t * (k-1)/(t-1)) + (k/t * m/(t-1) * 2) + (k/t * n/(t-1) * 2) + (m/t * (m-1)/(t-1) * 3/4)\
     + (m/t * n/(t-1) * 2 * (1/2))

print(pr)
# Combination to generate offspring with dominant allele (H?):
# HH X HH   ;   HH X Hh ;   HH X hh ;   Hh X Hh ;   Hh X hh
