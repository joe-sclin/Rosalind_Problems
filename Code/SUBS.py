import argparse

parser = argparse.ArgumentParser()
parser.add_argument('s', type=str)

with open(parser.parse_args().s) as f: lines = f.readlines()
s = lines[0].strip()
t = lines[1].strip()
res = list()
for i in range(len(s) - len(t) + 1):
    if s[i] == t[0]:
        if s[i:i + len(t)] == t:
            res.append(i + 1)

print(*res)

# Naive exact pattern matching approach is used (Highest no. of comparison but easy to implement)