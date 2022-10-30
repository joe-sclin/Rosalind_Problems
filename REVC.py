import argparse

parser = argparse.ArgumentParser()
parser.add_argument('s',type=str)

with open(parser.parse_args().s) as f:
	s=f.read()
re = ''
for c in s:
	if c == 'A': re = 'T' + re
	if c == 'C': re = 'G' + re
	if c == "G": re = 'C' + re
	if c == "T": re = 'A' + re
print(re)
