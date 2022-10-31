import argparse

parser = argparse.ArgumentParser()
parser.add_argument('s', type=str)

with open(parser.parse_args().s) as f: lines = f.readlines()
seqone = lines[0].strip()
seqtwo = lines[1].strip()
if len(seqone) == len(seqtwo):
    count = 0
    for i in range(len(seqone)):
        if seqone[i] != seqtwo[i]: count += 1
    print(count)
else:
    raise ValueError("Length of sequence one and two are not the same.")