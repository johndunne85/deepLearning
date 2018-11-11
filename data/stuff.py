import re


infile = open('sand.txt','rt')
outfile= open('the_answer.txt','wt')

for line in infile:
    if re.search('loss$', line):
        print(line.rstrip(), file=outfile)

outfile.close()
