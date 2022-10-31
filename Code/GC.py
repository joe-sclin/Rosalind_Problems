import argparse


def gc(t):
    if len(t) > 0:
        count = 0
        for c in t:
            if c == 'C' or c == 'G': count += 1
        return count / len(t) * 100
    else:
        return 0


parser = argparse.ArgumentParser()
parser.add_argument('s', type=str)
seq = ''
GCcontent = 0
currseq = ''
currDNA = ''

with open(parser.parse_args().s) as f: lines = f.readlines()
for i in range(len(lines)):
    s = lines[i].strip()
    if s[0] == '>' or i == len(lines) - 1:
        if i == len(lines) - 1:
            currDNA += s
        if gc(currDNA) > GCcontent:
            seq = currseq
            GCcontent = gc(currDNA)
            currDNA = ''
        else:
            currDNA = ''
        currseq = s[1:]
    else:
        currDNA += s

print(seq)
print(round(GCcontent,6))

"""
currseq and currDNA stored the current name and DNA sequence
seq and GCcontent stored the name of GC content percentage with the highest value

Instead of storing all name-GC content pairs / name-DNA sequence pairs in fasta files
This method largely reduced the resource consumption, especially for long DNA sequence 
"""