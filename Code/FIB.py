import argparse

parser = argparse.ArgumentParser()
parser.add_argument('n',type=int)
parser.add_argument('k',type=int)

k = parser.parse_args().k
n = parser.parse_args().n

n1 = 1
n2 = 1
for i in range(n-2):
	temp = n2
	n2 = n1*3+n2
	n1 = temp
print(n2)
