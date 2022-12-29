import pandas as pd
import numpy as np
import os
import os.path
import argparse
from os import path

parser = argparse.ArgumentParser()
parser.add_argument('-r', '--reads_dir', dest='reads_dir')
parser.add_argument('-id','--ids_list',dest='ids_list')
parser.add_argument('-id2','--ids_list2',dest='ids_list2')
parser.add_argument('-db','--kraken2_db',dest='kraken2_db')
args=parser.parse_args()

#make output directories
os.system('mkdir '+str(args.reads_dir)+'/'+str(args.kraken2_db)+'/extracted_reads')
os.system('mkdir '+str(args.reads_dir)+'/'+str(args.kraken2_db)+'/extracted_reads/Bacteria_Archaea')
os.system('mkdir '+str(args.reads_dir)+'/'+str(args.kraken2_db)+'/extracted_reads/Viruses')
os.system('mkdir '+str(args.reads_dir)+'/'+str(args.kraken2_db)+'/extracted_reads/Eukaryota_not_human')
os.system('mkdir '+str(args.reads_dir)+'/'+str(args.kraken2_db)+'/extracted_reads/Unclassified')
os.system('mkdir '+str(args.reads_dir)+'/'+str(args.kraken2_db)+'/extracted_reads/Toxoplasma')
os.system('mkdir '+str(args.reads_dir)+'/'+str(args.kraken2_db)+'/contig_assembly')
os.system('mkdir '+str(args.reads_dir)+'/'+str(args.kraken2_db)+'/contig_assembly/Bacteria_Archaea')
os.system('mkdir '+str(args.reads_dir)+'/'+str(args.kraken2_db)+'/contig_assembly/Viruses')
os.system('mkdir '+str(args.reads_dir)+'/'+str(args.kraken2_db)+'/contig_assembly/Eukaryota_not_human')
os.system('mkdir '+str(args.reads_dir)+'/'+str(args.kraken2_db)+'/contig_assembly/Unclassified')
os.system('mkdir '+str(args.reads_dir)+'/'+str(args.kraken2_db)+'/contig_assembly/Toxoplasma')

#import id list and make list
df1=pd.read_csv(str(args.ids_list), sep='\t').dropna()
IDs=df1['ids'].tolist()

#import id list and make list
df2=pd.read_csv(str(args.ids_list2), sep='\t').dropna()
IDs2=df2['ids'].tolist()

for id in IDs:
	
	print ('Extracting Bacteria_Archaea reads for '+str(id))
	os.system('python kraken2/extract_kraken_reads.py -s '+str(args.reads_dir)+'/bbduk_output/bbduk_'+str(id)+'_1_sequence.fastq.gz -s2 '+str(args.reads_dir)+'/bbduk_output/bbduk_'+str(id)+'_2_sequence.fastq.gz -o '+str(args.reads_dir)+'/'+str(args.kraken2_db)+'/extracted_reads/Bacteria_Archaea/Bacteria_Archaea_'+str(id)+'_1.fastq -o2 '+str(args.reads_dir)+'/'+str(args.kraken2_db)+'/extracted_reads/Bacteria_Archaea/Bacteria_Archaea_'+str(id)+'_2.fastq --fastq-output -t 2 2157 --include-children -k '+str(args.reads_dir)+'/'+str(args.kraken2_db)+'/kraken2_output/'+str(id)+'.kraken2 -r '+str(args.reads_dir)+'/'+str(args.kraken2_db)+'/kraken2_output/'+str(id)+'.kreport2')
	print ('Extracting Viruses reads for '+str(id))
	os.system('python kraken2/extract_kraken_reads.py -s '+str(args.reads_dir)+'/bbduk_output/bbduk_'+str(id)+'_1_sequence.fastq.gz -s2 '+str(args.reads_dir)+'/bbduk_output/bbduk_'+str(id)+'_2_sequence.fastq.gz -o '+str(args.reads_dir)+'/'+str(args.kraken2_db)+'/extracted_reads/Viruses/Viruses_'+str(id)+'_1.fastq -o2 '+str(args.reads_dir)+'/'+str(args.kraken2_db)+'/extracted_reads/Viruses/Viruses_'+str(id)+'_2.fastq --fastq-output -t 10239 --include-children -k '+str(args.reads_dir)+'/'+str(args.kraken2_db)+'/kraken2_output/'+str(id)+'.kraken2 -r '+str(args.reads_dir)+'/'+str(args.kraken2_db)+'/kraken2_output/'+str(id)+'.kreport2')
	print ('Extracting Eukaryota_not_human reads for '+str(id))
	os.system('python kraken2/extract_kraken_reads.py -s '+str(args.reads_dir)+'/bbduk_output/bbduk_'+str(id)+'_1_sequence.fastq.gz -s2 '+str(args.reads_dir)+'/bbduk_output/bbduk_'+str(id)+'_2_sequence.fastq.gz -o '+str(args.reads_dir)+'/'+str(args.kraken2_db)+'/extracted_reads/Eukaryota_not_human/Eukaryota_not_human_'+str(id)+'_1.fastq -o2 '+str(args.reads_dir)+'/'+str(args.kraken2_db)+'/extracted_reads/Eukaryota_not_human_'+str(id)+'_2.fastq --fastq-output  -t 9606 --exclude -t 2759 --include-children -k '+str(args.reads_dir)+'/'+str(args.kraken2_db)+'/kraken2_output/'+str(id)+'.kraken2 -r '+str(args.reads_dir)+'/'+str(args.kraken2_db)+'/kraken2_output/'+str(id)+'.kreport2')
	print ('Extracting Unclassified reads for '+str(id))
	os.system('python kraken2/extract_kraken_reads.py -s '+str(args.reads_dir)+'/bbduk_output/bbduk_'+str(id)+'_1_sequence.fastq.gz -s2 '+str(args.reads_dir)+'/bbduk_output/bbduk_'+str(id)+'_2_sequence.fastq.gz -o '+str(args.reads_dir)+'/'+str(args.kraken2_db)+'/extracted_reads/Unclassified/Unclassified_'+str(id)+'_1.fastq -o2 '+str(args.reads_dir)+'/'+str(args.kraken2_db)+'/extracted_reads/Unclassified/Unclassified_'+str(id)+'_2.fastq --fastq-output -t 0 --include-children -k '+str(args.reads_dir)+'/'+str(args.kraken2_db)+'/kraken2_output/'+str(id)+'.kraken2 -r '+str(args.reads_dir)+'/'+str(args.kraken2_db)+'/kraken2_output/'+str(id)+'.kreport2')

