#!/usr/bin/python

import sys
infile_name = sys.argv[1]
outfile_name = sys.argv[2]
threshold = float(sys.argv[3])


def best_taxon_picker(line,threshold):
    output = []
    splitted = line.split(';')
    for i in range(0,len(splitted)-1,2):
        taxon = splitted[i]
        match_level = splitted[i+1]
        if float(match_level.strip()) >= threshold:
            output.append(taxon+';'+match_level)
    otu_taxon = ";".join(output) + ";"
    return otu_taxon

with open(infile_name) as infile, open(outfile_name, 'w') as outfile:
    for line in infile:
        outfile.write(best_taxon_picker(line,threshold)+'\n')