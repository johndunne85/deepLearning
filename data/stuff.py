import re


infile = open('iris.data.txt','rt')
outfile= open('the_answer.txt','wt')

for line in infile:
    if re.search('Three-of-akind$', line):
        print(line.rstrip(), file=outfile)

outfile.close()
