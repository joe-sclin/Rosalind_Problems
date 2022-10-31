import argparse

parser = argparse.ArgumentParser()
parser.add_argument('s',type=str)

with open(parser.parse_args().s) as f:
	s=f.read()
print(s.replace("T","U"))
