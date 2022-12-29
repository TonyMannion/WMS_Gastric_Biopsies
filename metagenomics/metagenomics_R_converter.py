import pandas as pd
import numpy as np
import os
import os.path
import argparse
from os import path

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--otu_input', dest='otu_input')
parser.add_argument('-m','--metadata',dest='metadata')
parser.add_argument('-k','--kingdom',dest='kingdom')
parser.add_argument('-g','--group',dest='group')
parser.add_argument('-g1','--group1',dest='group1')
parser.add_argument('-g2','--group2',dest='group2')
args=parser.parse_args()

#make output directories

f1 = open('metagenomics_template_R.txt', 'r')
f2 = open(str(args.kingdom)+"_"+str(args.group)+'_metagenomics_R.txt', 'w')

checkWords = ("otu_input.txt","metadata.txt","xxx","group","grp1","grp2")
repWords = (str(args.otu_input),str(args.metadata),str(args.kingdom),str(args.group),str(args.group1),str(args.group2))

for line in f1:
    for check, rep in zip(checkWords, repWords):
        line = line.replace(check, rep)
    f2.write(line)
f1.close()
f2.close()