import argparse

parser = argparse.ArgumentParser()
parser.add_argument('s',type=str)

with open(parser.parse_args().s) as f:
	s=f.read()
re = ''
for c in s:
	if c == 'A': re = 'T' + re
	elif c == 'C': re = 'G' + re
	elif c == "G": re = 'C' + re
	elif c == "T": re = 'A' + re
print(re)
