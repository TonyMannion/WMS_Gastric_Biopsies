import pandas as pd
import numpy as np
import os
import os.path
import argparse
from os import path

parser = argparse.ArgumentParser()
parser.add_argument('-r', '--reads_dir', dest='reads_dir')
parser.add_argument('-id2','--ids_list2',dest='ids_list2')
parser.add_argument('-db','--kraken2_db',dest='kraken2_db')
args=parser.parse_args()


#import id list and make list
df2=pd.read_csv(str(args.ids_list2), sep='\t').dropna()
IDs2=df2['ids'].tolist()



for id2 in IDs2:
	
	print ('Bacteria_Archaea reads contig assemlby for '+str(id))
	os.system('cat '+str(args.reads_dir)+'/'+str(args.kraken2_db)+'/extracted_reads/Bacteria_Archaea/Bacteria_Archaea_'+str(id2)+'-*_1.fastq > '+str(args.reads_dir)+'/'+str(args.kraken2_db)+'/extracted_reads/Bacteria_Archaea/Bacteria_Archaea_'+str(id2)+'-1_concat.fastq')
	os.system('cat '+str(args.reads_dir)+'/'+str(args.kraken2_db)+'/extracted_reads/Bacteria_Archaea/Bacteria_Archaea_'+str(id2)+'-*_2.fastq > '+str(args.reads_dir)+'/'+str(args.kraken2_db)+'/extracted_reads/Bacteria_Archaea/Bacteria_Archaea_'+str(id2)+'-2_concat.fastq')
	os.system('python SPAdes-3.15.2-Linux/bin/spades.py -t 90 --meta -1 '+str(args.reads_dir)+'/'+str(args.kraken2_db)+'/extracted_reads/Bacteria_Archaea/Bacteria_Archaea_'+str(id2)+'-1_concat.fastq -2 '+str(args.reads_dir)+'/'+str(args.kraken2_db)+'/extracted_reads/Bacteria_Archaea/Bacteria_Archaea_'+str(id2)+'-2_concat.fastq -o '+str(args.reads_dir)+'/'+str(args.kraken2_db)+'/contig_assembly/Bacteria_Archaea/metaspades_Bacteria_Archaea_'+str(id2))

	print ('Viruses reads contig assemlby for '+str(id))
	os.system('cat '+str(args.reads_dir)+'/'+str(args.kraken2_db)+'/extracted_reads/Viruses/Viruses_'+str(id2)+'-*_1.fastq > '+str(args.reads_dir)+'/'+str(args.kraken2_db)+'/extracted_reads/Viruses/Viruses_'+str(id2)+'-1_concat.fastq')
	os.system('cat '+str(args.reads_dir)+'/'+str(args.kraken2_db)+'/extracted_reads/Viruses/Viruses_'+str(id2)+'-*_2.fastq > '+str(args.reads_dir)+'/'+str(args.kraken2_db)+'/extracted_reads/Viruses/Viruses_'+str(id2)+'-2_concat.fastq')
	os.system('python SPAdes-3.15.2-Linux/bin/spades.py -t 90 --meta -1 '+str(args.reads_dir)+'/'+str(args.kraken2_db)+'/extracted_reads/Viruses/Viruses_'+str(id2)+'-1_concat.fastq -2 '+str(args.reads_dir)+'/'+str(args.kraken2_db)+'/extracted_reads/Viruses/Viruses_'+str(id2)+'-2_concat.fastq -o '+str(args.reads_dir)+'/'+str(args.kraken2_db)+'/contig_assembly/Viruses/metaspades_Viruses_'+str(id2))

	print ('Eukaryota_not_human reads contig assemlby for '+str(id))
	os.system('cat '+str(args.reads_dir)+'/'+str(args.kraken2_db)+'/extracted_reads/Eukaryota_not_human/Eukaryota_not_human_'+str(id2)+'-*_1.fastq > '+str(args.reads_dir)+'/'+str(args.kraken2_db)+'/extracted_reads/Eukaryota_not_human/Eukaryota_not_human_'+str(id2)+'-1_concat.fastq')
	os.system('cat '+str(args.reads_dir)+'/'+str(args.kraken2_db)+'/extracted_reads/Eukaryota_not_human/Eukaryota_not_human_'+str(id2)+'-*_2.fastq > '+str(args.reads_dir)+'/'+str(args.kraken2_db)+'/extracted_reads/Eukaryota_not_human/Eukaryota_not_human_'+str(id2)+'-2_concat.fastq')
	os.system('python SPAdes-3.15.2-Linux/bin/spades.py -t 90 --meta -1 '+str(args.reads_dir)+'/'+str(args.kraken2_db)+'/extracted_reads/Eukaryota_not_human/Eukaryota_not_human_'+str(id2)+'-1_concat.fastq -2 '+str(args.reads_dir)+'/'+str(args.kraken2_db)+'/extracted_reads/Eukaryota_not_human/Eukaryota_not_human_'+str(id2)+'-2_concat.fastq -o '+str(args.reads_dir)+'/'+str(args.kraken2_db)+'/contig_assembly/Eukaryota_not_human/metaspades_Eukaryota_not_human_'+str(id2))

	print ('Unclassified reads contig assemlby for '+str(id))
	os.system('cat '+str(args.reads_dir)+'/'+str(args.kraken2_db)+'/extracted_reads/Unclassified/Unclassified_'+str(id2)+'-*_1.fastq > '+str(args.reads_dir)+'/'+str(args.kraken2_db)+'/extracted_reads/Unclassified/Unclassified_'+str(id2)+'-1_concat.fastq')
	os.system('cat '+str(args.reads_dir)+'/'+str(args.kraken2_db)+'/extracted_reads/Unclassified/Unclassified_'+str(id2)+'-*_2.fastq > '+str(args.reads_dir)+'/'+str(args.kraken2_db)+'/extracted_reads/Unclassified/Unclassified_'+str(id2)+'-2_concat.fastq')
	os.system('python SPAdes-3.15.2-Linux/bin/spades.py -t 90 --meta -1 '+str(args.reads_dir)+'/'+str(args.kraken2_db)+'/extracted_reads/Unclassified/Unclassified_'+str(id2)+'-1_concat.fastq -2 '+str(args.reads_dir)+'/'+str(args.kraken2_db)+'/extracted_reads/Unclassified/Unclassified_'+str(id2)+'-2_concat.fastq -o '+str(args.reads_dir)+'/'+str(args.kraken2_db)+'/contig_assembly/Unclassified/metaspades_Unclassified_'+str(id2))



