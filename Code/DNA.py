import argparse

parser = argparse.ArgumentParser()
parser.add_argument('s',type=str)

with open(parser.parse_args().s) as f:
	s=f.read()
count = [0,0,0,0]
for c in s:
	if c == 'A': count[0] += 1
	if c == 'C': count[1] += 1
	if c == "G": count[2] += 1
	if c == "T": count[3] += 1
print(*count)
