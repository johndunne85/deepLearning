

import re

infile = open('the_answer.txt','rt')
outfile = open('thirty-six.txt','wt')

for line in infile:
    if re.search('One-pair',line):
        print(line.rstrip(), file=outfile)

outfile.close()
