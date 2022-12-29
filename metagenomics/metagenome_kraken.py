import pandas as pd
import numpy as np
import os
import os.path
import argparse
from os import path

parser = argparse.ArgumentParser()
parser.add_argument('-r', '--reads_dir', dest='reads_dir')
parser.add_argument('-id','--ids_list',dest='ids_list')
parser.add_argument('-db','--kraken2_db',dest='kraken2_db')
parser.add_argument('-id2','--ids_list2',dest='ids_list2')
args=parser.parse_args()

#make output directories
os.system('mkdir '+str(args.reads_dir)+'/bbduk_output')
os.system('mkdir '+str(args.reads_dir)+'/'+str(args.kraken2_db))
os.system('mkdir '+str(args.reads_dir)+'/'+str(args.kraken2_db)+'/kraken2_output')
os.system('mkdir '+str(args.reads_dir)+'/'+str(args.kraken2_db)+'/bracken_output')
os.system('mkdir '+str(args.reads_dir)+'/'+str(args.kraken2_db)+'/mpa_output')

#import id list and make list
df1=pd.read_csv(str(args.ids_list), sep='\t').dropna()
IDs=df1['ids'].tolist()

#import id list and make list
df2=pd.read_csv(str(args.ids_list2), sep='\t').dropna()
IDs2=df2['ids'].tolist()

for id in IDs:

	print ('BBduk on '+str(id))
	os.system('/home/dcm/BBMap_38.90/bbmap/bbduk.sh in='+str(args.reads_dir)+'/'+str(id)+'_1_sequence.fastq in2='+str(args.reads_dir)+'/'+str(id)+'_2_sequence.fastq out='+str(args.reads_dir)+'/bbduk_output/bbduk_'+str(id)+'_1.fastq out2='+str(args.reads_dir)+'/bbduk_output/bbduk_'+str(id)+'_2.fastq outm='+str(args.reads_dir)+'/bbduk_output/ref_match_'+str(id)+'_1.fastq outm2='+str(args.reads_dir)+'/bbduk_output/ref_match_'+str(id)+'_2.fastq stats='+str(args.reads_dir)+'/bbduk_output/ref_match_'+str(id)+'_sequence_stats.txt ref=/home/dcm/BBMap_38.90/bbmap/resources/adapters.fa ktrim=r k=23 mink=11 hdist=1 tpe tbo')

	print ('Kraken2 on '+str(id))
	os.system('./kraken2/kraken2 --db /home/dcm/kraken2/'+str(args.kraken2_db)+' --threads 90 --report '+str(args.reads_dir)+'/'+str(args.kraken2_db)+'/kraken2_output/'+str(id)+'.kreport2 --paired '+str(args.reads_dir)+'/bbduk_output/bbduk_'+str(id)+'_1_sequence.fastq.gz '+str(args.reads_dir)+'/bbduk_output/bbduk_'+str(id)+'_2_sequence.fastq.gz > '+str(args.reads_dir)+'/'+str(args.kraken2_db)+'/kraken2_output/'+str(id)+'.kraken2')

for id2 in IDs2:

	print ('Combine Kraken2 kreports on '+str(id2))
	os.system('python kraken2/combine_kreports.py -r '+str(args.reads_dir)+'/'+str(args.kraken2_db)+'/kraken2_output/'+str(id2)+'-1.kreport2 '+str(args.reads_dir)+'/'+str(args.kraken2_db)+'/kraken2_output/'+str(id2)+'-2.kreport2 -o '+str(args.reads_dir)+'/'+str(args.kraken2_db)+'/kraken2_output/'+str(id2)+'.kreport2 --no-headers --only-combined')

	print ('Bracken on '+str(id2))
	os.system('./Bracken/bracken -d /home/dcm/kraken2/'+str(args.kraken2_db)+' -i '+str(args.reads_dir)+'/'+str(args.kraken2_db)+'/kraken2_output/'+str(id2)+'.kreport2 -o '+ str(args.reads_dir)+'/'+str(args.kraken2_db)+'/bracken_output/'+str(id2)+'_species.Bracken -l S -r 250')
	os.system('./Bracken/bracken -d /home/dcm/kraken2/'+str(args.kraken2_db)+' -i '+str(args.reads_dir)+'/'+str(args.kraken2_db)+'/kraken2_output/'+str(id2)+'.kreport2 -o '+ str(args.reads_dir)+'/'+str(args.kraken2_db)+'/bracken_output/'+str(id2)+'_genus.Bracken -l G -r 250')
	os.system('./Bracken/bracken -d /home/dcm/kraken2/'+str(args.kraken2_db)+' -i '+str(args.reads_dir)+'/'+str(args.kraken2_db)+'/kraken2_output/'+str(id2)+'.kreport2 -o '+ str(args.reads_dir)+'/'+str(args.kraken2_db)+'/bracken_output/'+str(id2)+'_family.Bracken -l F -r 250')
	os.system('./Bracken/bracken -d /home/dcm/kraken2/'+str(args.kraken2_db)+' -i '+str(args.reads_dir)+'/'+str(args.kraken2_db)+'/kraken2_output/'+str(id2)+'.kreport2 -o '+ str(args.reads_dir)+'/'+str(args.kraken2_db)+'/bracken_output/'+str(id2)+'_class.Bracken -l C -r 250')
	os.system('./Bracken/bracken -d /home/dcm/kraken2/'+str(args.kraken2_db)+' -i '+str(args.reads_dir)+'/'+str(args.kraken2_db)+'/kraken2_output/'+str(id2)+'.kreport2 -o '+ str(args.reads_dir)+'/'+str(args.kraken2_db)+'/bracken_output/'+str(id2)+'_order.Bracken -l O -r 250')
	os.system('./Bracken/bracken -d /home/dcm/kraken2/'+str(args.kraken2_db)+' -i '+str(args.reads_dir)+'/'+str(args.kraken2_db)+'/kraken2_output/'+str(id2)+'.kreport2 -o '+ str(args.reads_dir)+'/'+str(args.kraken2_db)+'/bracken_output/'+str(id2)+'_phylum.Bracken -l P -r 250')
	os.system('./Bracken/bracken -d /home/dcm/kraken2/'+str(args.kraken2_db)+' -i '+str(args.reads_dir)+'/'+str(args.kraken2_db)+'/kraken2_output/'+str(id2)+'.kreport2 -o '+ str(args.reads_dir)+'/'+str(args.kraken2_db)+'/bracken_output/'+str(id2)+'_kingdom.Bracken -l K -r 250')

	print ('Bracken to MPA on '+str(id2))
	os.system('python kraken2/kreport2mpa.py -r '+str(args.reads_dir)+'/'+str(args.kraken2_db)+'/kraken2_output/'+str(id2)+'_bracken_species.kreport2 -o '+str(args.reads_dir)+'/'+str(args.kraken2_db)+'/mpa_output/'+str(id2)+'_bracken_species_mpa.txt --display-header')
	os.system('python kraken2/kreport2mpa.py -r '+str(args.reads_dir)+'/'+str(args.kraken2_db)+'/kraken2_output/'+str(id2)+'_bracken_genuses.kreport2 -o '+str(args.reads_dir)+'/'+str(args.kraken2_db)+'/mpa_output/'+str(id2)+'_bracken_genus_mpa.txt --display-header')
	os.system('python kraken2/kreport2mpa.py -r '+str(args.reads_dir)+'/'+str(args.kraken2_db)+'/kraken2_output/'+str(id2)+'_bracken_families.kreport2 -o '+str(args.reads_dir)+'/'+str(args.kraken2_db)+'/mpa_output/'+str(id2)+'_bracken_family_mpa.txt --display-header')
	os.system('python kraken2/kreport2mpa.py -r '+str(args.reads_dir)+'/'+str(args.kraken2_db)+'/kraken2_output/'+str(id2)+'_bracken_classes.kreport2 -o '+str(args.reads_dir)+'/'+str(args.kraken2_db)+'/mpa_output/'+str(id2)+'_bracken_class_mpa.txt --display-header')
	os.system('python kraken2/kreport2mpa.py -r '+str(args.reads_dir)+'/'+str(args.kraken2_db)+'/kraken2_output/'+str(id2)+'_bracken_orders.kreport2 -o '+str(args.reads_dir)+'/'+str(args.kraken2_db)+'/mpa_output/'+str(id2)+'_bracken_order_mpa.txt --display-header')
	os.system('python kraken2/kreport2mpa.py -r '+str(args.reads_dir)+'/'+str(args.kraken2_db)+'/kraken2_output/'+str(id2)+'_bracken_phylums.kreport2 -o '+str(args.reads_dir)+'/'+str(args.kraken2_db)+'/mpa_output/'+str(id2)+'_bracken_phylum_mpa.txt --display-header')
	os.system('python kraken2/kreport2mpa.py -r '+str(args.reads_dir)+'/'+str(args.kraken2_db)+'/kraken2_output/'+str(id2)+'_bracken_K.kreport2 -o '+str(args.reads_dir)+'/'+str(args.kraken2_db)+'/mpa_output/'+str(id2)+'_bracken_kingdom_mpa.txt --display-header')

print ('Combining Bracken MPAs for Species')
MPA_files_species=[str(args.reads_dir)+'/'+str(args.kraken2_db)+'/mpa_output/'+str(id2)+'_bracken_species_mpa.txt' for id2 in IDs2]
Joined_map_species_files = ' '.join(MPA_files_species)
os.system('python kraken2/combine_mpa.py -i '+str(Joined_map_species_files)+' -o '+str(args.reads_dir)+'/'+str(args.kraken2_db)+'/mpa_output/combined_bracken_species_mpa.txt')
df=pd.read_csv(str(args.reads_dir)+'/'+str(args.kraken2_db)+'/mpa_output/combined_bracken_species_mpa.txt', sep='\t')
df = df[df['#Classification'].str.contains('\\|s__')]
#pipe character '|' needs double backslash '\\' to ignore because by default the pipe operator '|' in python is by default the bitwise OR operator
df = df[~df['#Classification'].str.contains('Homo_sapiens', na=False)]
df = df.replace('k__Eukaryota\\|k__Fungi' ,'k__Fungi', regex=True)
df.to_csv(str(args.reads_dir)+'/'+str(args.kraken2_db)+'/mpa_output/filtered_combined_bracken_species_mpa.txt', sep='\t', index=False)

print ('Combining Bracken MPAs for Genus')
MPA_files_species=[str(args.reads_dir)+'/'+str(args.kraken2_db)+'/mpa_output/'+str(id2)+'_bracken_genus_mpa.txt' for id2 in IDs2]
Joined_map_species_files = ' '.join(MPA_files_species)
os.system('python kraken2/combine_mpa.py -i '+str(Joined_map_species_files)+' -o '+str(args.reads_dir)+'/'+str(args.kraken2_db)+'/mpa_output/combined_bracken_genus_mpa.txt')
df=pd.read_csv(str(args.reads_dir)+'/'+str(args.kraken2_db)+'/mpa_output/combined_bracken_genus_mpa.txt', sep='\t')
df = df[df['#Classification'].str.contains('\\|g__')]
#pipe character '|' needs double backslash '\\' to ignore because by default the pipe operator '|' in python is by default the bitwise OR operator
df = df[~df['#Classification'].str.contains('Homo_sapiens', na=False)]
df = df.replace('k__Eukaryota\\|k__Fungi' ,'k__Fungi', regex=True)
df.to_csv(str(args.reads_dir)+'/'+str(args.kraken2_db)+'/mpa_output/filtered_combined_bracken_genus_mpa.txt', sep='\t', index=False)

print ('Combining Bracken MPAs for Family')
MPA_files_species=[str(args.reads_dir)+'/'+str(args.kraken2_db)+'/mpa_output/'+str(id2)+'_bracken_family_mpa.txt' for id2 in IDs2]
Joined_map_species_files = ' '.join(MPA_files_species)
os.system('python kraken2/combine_mpa.py -i '+str(Joined_map_species_files)+' -o '+str(args.reads_dir)+'/'+str(args.kraken2_db)+'/mpa_output/combined_bracken_family_mpa.txt')
df=pd.read_csv(str(args.reads_dir)+'/'+str(args.kraken2_db)+'/mpa_output/combined_bracken_family_mpa.txt', sep='\t')
df = df[df['#Classification'].str.contains('\\|f__')]
#pipe character '|' needs double backslash '\\' to ignore because by default the pipe operator '|' in python is by default the bitwise OR operator
df = df[~df['#Classification'].str.contains('Homo_sapiens', na=False)]
df = df.replace('k__Eukaryota\\|k__Fungi' ,'k__Fungi', regex=True)
df.to_csv(str(args.reads_dir)+'/'+str(args.kraken2_db)+'/mpa_output/filtered_combined_bracken_family_mpa.txt', sep='\t', index=False)

print ('Combining Bracken MPAs for Class')
MPA_files_species=[str(args.reads_dir)+'/'+str(args.kraken2_db)+'/mpa_output/'+str(id2)+'_bracken_class_mpa.txt' for id2 in IDs2]
Joined_map_species_files = ' '.join(MPA_files_species)
os.system('python kraken2/combine_mpa.py -i '+str(Joined_map_species_files)+' -o '+str(args.reads_dir)+'/'+str(args.kraken2_db)+'/mpa_output/combined_bracken_class_mpa.txt')
df=pd.read_csv(str(args.reads_dir)+'/'+str(args.kraken2_db)+'/mpa_output/combined_bracken_class_mpa.txt', sep='\t')
df = df[df['#Classification'].str.contains('\\|c__')]
#pipe character '|' needs double backslash '\\' to ignore because by default the pipe operator '|' in python is by default the bitwise OR operator
df = df[~df['#Classification'].str.contains('Homo_sapiens', na=False)]
df = df.replace('k__Eukaryota\\|k__Fungi' ,'k__Fungi', regex=True)
df.to_csv(str(args.reads_dir)+'/'+str(args.kraken2_db)+'/mpa_output/filtered_combined_bracken_class_mpa.txt', sep='\t', index=False)

print ('Combining Bracken MPAs for Order')
MPA_files_species=[str(args.reads_dir)+'/'+str(args.kraken2_db)+'/mpa_output/'+str(id2)+'_bracken_order_mpa.txt' for id2 in IDs2]
Joined_map_species_files = ' '.join(MPA_files_species)
os.system('python kraken2/combine_mpa.py -i '+str(Joined_map_species_files)+' -o '+str(args.reads_dir)+'/'+str(args.kraken2_db)+'/mpa_output/combined_bracken_order_mpa.txt')
df=pd.read_csv(str(args.reads_dir)+'/'+str(args.kraken2_db)+'/mpa_output/combined_bracken_order_mpa.txt', sep='\t')
df = df[df['#Classification'].str.contains('\\|o__')]
#pipe character '|' needs double backslash '\\' to ignore because by default the pipe operator '|' in python is by default the bitwise OR operator
df = df[~df['#Classification'].str.contains('Homo_sapiens', na=False)]
df = df.replace('k__Eukaryota\\|k__Fungi' ,'k__Fungi', regex=True)
df.to_csv(str(args.reads_dir)+'/'+str(args.kraken2_db)+'/mpa_output/filtered_combined_bracken_order_mpa.txt', sep='\t', index=False)

print ('Combining Bracken MPAs for Phylum')
MPA_files_species=[str(args.reads_dir)+'/'+str(args.kraken2_db)+'/mpa_output/'+str(id2)+'_bracken_phylum_mpa.txt' for id2 in IDs2]
Joined_map_species_files = ' '.join(MPA_files_species)
os.system('python kraken2/combine_mpa.py -i '+str(Joined_map_species_files)+' -o '+str(args.reads_dir)+'/'+str(args.kraken2_db)+'/mpa_output/combined_bracken_phylum_mpa.txt')
df=pd.read_csv(str(args.reads_dir)+'/'+str(args.kraken2_db)+'/mpa_output/combined_bracken_phylum_mpa.txt', sep='\t')
df = df[df['#Classification'].str.contains('\\|p__')]
#pipe character '|' needs double backslash '\\' to ignore because by default the pipe operator '|' in python is by default the bitwise OR operator
df = df[~df['#Classification'].str.contains('Homo_sapiens', na=False)]
df = df.replace('k__Eukaryota\\|k__Fungi' ,'k__Fungi', regex=True)
df.to_csv(str(args.reads_dir)+'/'+str(args.kraken2_db)+'/mpa_output/filtered_combined_bracken_phylum_mpa.txt', sep='\t', index=False)

print ('Combining Bracken MPAs for Kingdom')
MPA_files_species=[str(args.reads_dir)+'/'+str(args.kraken2_db)+'/mpa_output/'+str(id2)+'_bracken_kingdom_mpa.txt' for id2 in IDs2]
Joined_map_species_files = ' '.join(MPA_files_species)
os.system('python kraken2/combine_mpa.py -i '+str(Joined_map_species_files)+' -o '+str(args.reads_dir)+'/'+str(args.kraken2_db)+'/mpa_output/combined_bracken_kingdom_mpa.txt')
df=pd.read_csv(str(args.reads_dir)+'/'+str(args.kraken2_db)+'/mpa_output/combined_bracken_kingdom_mpa.txt', sep='\t')
df = df[df['#Classification'].str.contains('\\|k__')]
#pipe character '|' needs double backslash '\\' to ignore because by default the pipe operator '|' in python is by default the bitwise OR operator
df = df[~df['#Classification'].str.contains('Homo_sapiens', na=False)]
df = df.replace('k__Eukaryota\\|k__Fungi' ,'k__Fungi', regex=True)
df.to_csv(str(args.reads_dir)+'/'+str(args.kraken2_db)+'/mpa_output/filtered_combined_bracken_kingdom_mpa.txt', sep='\t', index=False)


