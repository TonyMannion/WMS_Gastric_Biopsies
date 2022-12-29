import pandas as pd
import numpy as np
import os
import os.path
import argparse
from os import path

parser = argparse.ArgumentParser()
parser.add_argument('-r', '--reads_dir', dest='reads_dir')
parser.add_argument('-id','--ids_list',dest='ids_list')
#parser.add_argument('-db','--kraken2_db',dest='kraken2_db')
args=parser.parse_args()

#make output directories
os.system('mkdir '+str(args.reads_dir)+'/16S_SILVA138_k2db')
os.system('mkdir '+str(args.reads_dir)+'/16S_SILVA138_k2db/kraken2_output')
os.system('mkdir '+str(args.reads_dir)+'/16S_SILVA138_k2db/bracken_output')
os.system('mkdir '+str(args.reads_dir)+'/16S_SILVA138_k2db/biom_output')
os.system('mkdir '+str(args.reads_dir)+'/16S_SILVA138_k2db/mpa_output')
os.system('mkdir '+str(args.reads_dir)+'/16S_SILVA138_k2db/tree_output')

#import id list and make list
df1=pd.read_csv(str(args.ids_list), sep='\t').dropna()
IDs=df1['ids'].tolist()

for id in IDs:

	print ('BBduk on '+str(id))
	os.system('/home/dcm/BBMap_38.90/bbmap/bbduk.sh in='+str(args.reads_dir)+'/'+str(id)+'_1_sequence.fastq in2='+str(args.reads_dir)+'/'+str(id)+'_2_sequence.fastq out='+str(args.reads_dir)+'/bbduk_output/bbduk_'+str(id)+'_1.fastq out2='+str(args.reads_dir)+'/bbduk_output/bbduk_'+str(id)+'_2.fastq outm='+str(args.reads_dir)+'/bbduk_output/ref_match_'+str(id)+'_1.fastq outm2='+str(args.reads_dir)+'/bbduk_output/ref_match_'+str(id)+'_2.fastq stats='+str(args.reads_dir)+'/bbduk_output/ref_match_'+str(id)+'_sequence_stats.txt 
	print ('Kraken2 on '+str(id))
	os.system('./kraken2/kraken2 --db /home/dcm/kraken2/16S_SILVA138_k2db --threads 90 --report '+str(args.reads_dir)+'/16S_SILVA138_k2db/kraken2_output/'+str(id)+'.kreport2 --paired '+str(args.reads_dir)+'/bbduk_output/bbduk_'+str(id)+'_1.fastq '+str(args.reads_dir)+'/bbduk_output/bbduk_'+str(id)+'_2.fastq > '+str(args.reads_dir)+'/16S_SILVA138_k2db/kraken2_output/'+str(id)+'.kraken2')

	print ('Bracken on '+str(id))

	os.system('./Bracken/bracken -d /home/dcm/kraken2/16S_SILVA138_k2db -i '+str(args.reads_dir)+'/16S_SILVA138_k2db/kraken2_output/'+str(id)+'.kreport2 -o '+ str(args.reads_dir)+'/16S_SILVA138_k2db/bracken_output/'+str(id)+'_genus.Bracken -l G -r 250')
	os.system('./Bracken/bracken -d /home/dcm/kraken2/16S_SILVA138_k2db -i '+str(args.reads_dir)+'/16S_SILVA138_k2db/kraken2_output/'+str(id)+'.kreport2 -o '+ str(args.reads_dir)+'/16S_SILVA138_k2db/bracken_output/'+str(id)+'_family.Bracken -l F -r 250')
	os.system('./Bracken/bracken -d /home/dcm/kraken2/16S_SILVA138_k2db -i '+str(args.reads_dir)+'/16S_SILVA138_k2db/kraken2_output/'+str(id)+'.kreport2 -o '+ str(args.reads_dir)+'/16S_SILVA138_k2db/bracken_output/'+str(id)+'_class.Bracken -l C -r 250')
	os.system('./Bracken/bracken -d /home/dcm/kraken2/16S_SILVA138_k2db -i '+str(args.reads_dir)+'/16S_SILVA138_k2db/kraken2_output/'+str(id)+'.kreport2 -o '+ str(args.reads_dir)+'/16S_SILVA138_k2db/bracken_output/'+str(id)+'_order.Bracken -l O -r 250')
	os.system('./Bracken/bracken -d /home/dcm/kraken2/16S_SILVA138_k2db -i '+str(args.reads_dir)+'/16S_SILVA138_k2db/kraken2_output/'+str(id)+'.kreport2 -o '+ str(args.reads_dir)+'/16S_SILVA138_k2db/bracken_output/'+str(id)+'_phylum.Bracken -l P -r 250')

	print ('Bracken to MPA on '+str(id))

	os.system('python kraken2/kreport2mpa.py -r '+str(args.reads_dir)+'/16S_SILVA138_k2db/kraken2_output/'+str(id)+'_bracken_genuses.kreport2 -o '+str(args.reads_dir)+'/16S_SILVA138_k2db/mpa_output/'+str(id)+'_bracken_genus_mpa.txt --display-header')
	os.system('python kraken2/kreport2mpa.py -r '+str(args.reads_dir)+'/16S_SILVA138_k2db/kraken2_output/'+str(id)+'_bracken_families.kreport2 -o '+str(args.reads_dir)+'/16S_SILVA138_k2db/mpa_output/'+str(id)+'_bracken_family_mpa.txt --display-header')
	os.system('python kraken2/kreport2mpa.py -r '+str(args.reads_dir)+'/16S_SILVA138_k2db/kraken2_output/'+str(id)+'_bracken_classes.kreport2 -o '+str(args.reads_dir)+'/16S_SILVA138_k2db/mpa_output/'+str(id)+'_bracken_class_mpa.txt --display-header')
	os.system('python kraken2/kreport2mpa.py -r '+str(args.reads_dir)+'/16S_SILVA138_k2db/kraken2_output/'+str(id)+'_bracken_orders.kreport2 -o '+str(args.reads_dir)+'/16S_SILVA138_k2db/mpa_output/'+str(id)+'_bracken_order_mpa.txt --display-header')
	os.system('python kraken2/kreport2mpa.py -r '+str(args.reads_dir)+'/16S_SILVA138_k2db/kraken2_output/'+str(id)+'_bracken_phylums.kreport2 -o '+str(args.reads_dir)+'/16S_SILVA138_k2db/mpa_output/'+str(id)+'_bracken_phylum_mpa.txt --display-header')


print ('Combining Bracken kreports for Genuses')
bracken_output_files_genuses=[str(args.reads_dir)+'/16S_SILVA138_k2db/kraken2_output/'+str(id)+'_bracken_genuses.kreport2' for id in IDs]
Joined_bracken_output_genuses_files = ' '.join(bracken_output_files_genuses)
os.system('python kraken2/combine_kreports.py --only-combined -r '+str(Joined_bracken_output_genuses_files)+' -o '+str(args.reads_dir)+'/16S_SILVA138_k2db/kraken2_output/combined_bracken_genuses.kreport2')

print ('Combining Bracken kreports to Biom with GG ids for genuses')
os.system('kraken-biom '+str(Joined_bracken_output_genuses_files)+' -o '+str(args.reads_dir)+'/16S_SILVA138_k2db/biom_output/combined_bracken_genuses.biom')
os.system('biom convert  -i '+str(args.reads_dir)+'/16S_SILVA138_k2db/biom_output/combined_bracken_genuses.biom -o' +str(args.reads_dir)+'/16S_SILVA138_k2db/biom_output/combined_bracken_genuses_biom.txt --to-tsv --header-key taxonomy')


print ('Combining Bracken kreports for Families')
bracken_output_files_families=[str(args.reads_dir)+'/16S_SILVA138_k2db/kraken2_output/'+str(id)+'_bracken_families.kreport2' for id in IDs]
Joined_bracken_output_families_files = ' '.join(bracken_output_files_families)
os.system('python kraken2/combine_kreports.py --only-combined -r '+str(Joined_bracken_output_families_files)+' -o '+str(args.reads_dir)+'/16S_SILVA138_k2db/kraken2_output/combined_bracken_families.kreport2')

print ('Combining Bracken kreports to Biom with GG ids for families')
os.system('kraken-biom '+str(Joined_bracken_output_families_files)+' -o '+str(args.reads_dir)+'/16S_SILVA138_k2db/biom_output/combined_bracken_families.biom')
os.system('biom convert  -i '+str(args.reads_dir)+'/16S_SILVA138_k2db/biom_output/combined_bracken_families.biom -o' +str(args.reads_dir)+'/16S_SILVA138_k2db/biom_output/combined_bracken_families_biom.txt --to-tsv --header-key taxonomy')


print ('Combining Bracken kreports for Orders')
bracken_output_files_orders=[str(args.reads_dir)+'/16S_SILVA138_k2db/kraken2_output/'+str(id)+'_bracken_orders.kreport2' for id in IDs]
Joined_bracken_output_orders_files = ' '.join(bracken_output_files_orders)
os.system('python kraken2/combine_kreports.py --only-combined -r '+str(Joined_bracken_output_orders_files)+' -o '+str(args.reads_dir)+'/16S_SILVA138_k2db/kraken2_output/combined_bracken_orders.kreport2')

print ('Combining Bracken kreports to Biom with GG ids for orders')
os.system('kraken-biom '+str(Joined_bracken_output_orders_files)+' -o '+str(args.reads_dir)+'/16S_SILVA138_k2db/biom_output/combined_bracken_orders.biom')
os.system('biom convert  -i '+str(args.reads_dir)+'/16S_SILVA138_k2db/biom_output/combined_bracken_orders.biom -o' +str(args.reads_dir)+'/16S_SILVA138_k2db/biom_output/combined_bracken_orders_biom.txt --to-tsv --header-key taxonomy')

print ('Combining Bracken kreports for classes')
bracken_output_files_classes=[str(args.reads_dir)+'/16S_SILVA138_k2db/kraken2_output/'+str(id)+'_bracken_classes.kreport2' for id in IDs]
Joined_bracken_output_classes_files = ' '.join(bracken_output_files_classes)
os.system('python kraken2/combine_kreports.py --only-combined -r '+str(Joined_bracken_output_classes_files)+' -o '+str(args.reads_dir)+'/16S_SILVA138_k2db/kraken2_output/combined_bracken_classes.kreport2')

print ('Combining Bracken kreports to Biom with GG ids for classes')
os.system('kraken-biom '+str(Joined_bracken_output_classes_files)+' -o '+str(args.reads_dir)+'/16S_SILVA138_k2db/biom_output/combined_bracken_classes.biom')
os.system('biom convert  -i '+str(args.reads_dir)+'/16S_SILVA138_k2db/biom_output/combined_bracken_classes.biom -o' +str(args.reads_dir)+'/16S_SILVA138_k2db/biom_output/combined_bracken_classes_biom.txt --to-tsv --header-key taxonomy')


print ('Combining Bracken kreports for phylums')
bracken_output_files_phylums=[str(args.reads_dir)+'/16S_SILVA138_k2db/kraken2_output/'+str(id)+'_bracken_phylums.kreport2' for id in IDs]
Joined_bracken_output_phylums_files = ' '.join(bracken_output_files_phylums)
os.system('python kraken2/combine_kreports.py --only-combined -r '+str(Joined_bracken_output_phylums_files)+' -o '+str(args.reads_dir)+'/16S_SILVA138_k2db/kraken2_output/combined_bracken_phylums.kreport2')

print ('Combining Bracken kreports to Biom with GG ids for phylums')
os.system('kraken-biom '+str(Joined_bracken_output_phylums_files)+' -o '+str(args.reads_dir)+'/16S_SILVA138_k2db/biom_output/combined_bracken_phylums.biom')
os.system('biom convert  -i '+str(args.reads_dir)+'/16S_SILVA138_k2db/biom_output/combined_bracken_phylums.biom -o' +str(args.reads_dir)+'/16S_SILVA138_k2db/biom_output/combined_bracken_phylums_biom.txt --to-tsv --header-key taxonomy')


print ('Combining Bracken MPAs for Genus')
MPA_files_species=[str(args.reads_dir)+'/16S_SILVA138_k2db/mpa_output/'+str(id)+'_bracken_genus_mpa.txt' for id in IDs]
Joined_map_species_files = ' '.join(MPA_files_species)
os.system('python kraken2/combine_mpa.py -i '+str(Joined_map_species_files)+' -o '+str(args.reads_dir)+'/16S_SILVA138_k2db/mpa_output/combined_bracken_genus_mpa.txt')
df=pd.read_csv(str(args.reads_dir)+'/16S_SILVA138_k2db/mpa_output/combined_bracken_genus_mpa.txt', sep='\t')
df = df[df['#Classification'].str.contains('\\|g__')]
#pipe character '|' needs double backslash '\\' to ignore because by default the pipe operator '|' in python is by default the bitwise OR operator
df.to_csv(str(args.reads_dir)+'/16S_SILVA138_k2db/mpa_output/filtered_combined_bracken_genus_mpa.txt', sep='\t', index=False)

print ('Combining Bracken MPAs for Family')
MPA_files_species=[str(args.reads_dir)+'/16S_SILVA138_k2db/mpa_output/'+str(id)+'_bracken_family_mpa.txt' for id in IDs]
Joined_map_species_files = ' '.join(MPA_files_species)
os.system('python kraken2/combine_mpa.py -i '+str(Joined_map_species_files)+' -o '+str(args.reads_dir)+'/16S_SILVA138_k2db/mpa_output/combined_bracken_family_mpa.txt')
df=pd.read_csv(str(args.reads_dir)+'/16S_SILVA138_k2db/mpa_output/combined_bracken_family_mpa.txt', sep='\t')
df = df[df['#Classification'].str.contains('\\|f__')]
#pipe character '|' needs double backslash '\\' to ignore because by default the pipe operator '|' in python is by default the bitwise OR operator
df.to_csv(str(args.reads_dir)+'/16S_SILVA138_k2db/mpa_output/filtered_combined_bracken_family_mpa.txt', sep='\t', index=False)

print ('Combining Bracken MPAs for Class')
MPA_files_species=[str(args.reads_dir)+'/16S_SILVA138_k2db/mpa_output/'+str(id)+'_bracken_class_mpa.txt' for id in IDs]
Joined_map_species_files = ' '.join(MPA_files_species)
os.system('python kraken2/combine_mpa.py -i '+str(Joined_map_species_files)+' -o '+str(args.reads_dir)+'/16S_SILVA138_k2db/mpa_output/combined_bracken_class_mpa.txt')
df=pd.read_csv(str(args.reads_dir)+'/16S_SILVA138_k2db/mpa_output/combined_bracken_class_mpa.txt', sep='\t')
df = df[df['#Classification'].str.contains('\\|c__')]
#pipe character '|' needs double backslash '\\' to ignore because by default the pipe operator '|' in python is by default the bitwise OR operator
df.to_csv(str(args.reads_dir)+'/16S_SILVA138_k2db/mpa_output/filtered_combined_bracken_class_mpa.txt', sep='\t', index=False)

print ('Combining Bracken MPAs for Order')
MPA_files_species=[str(args.reads_dir)+'/16S_SILVA138_k2db/mpa_output/'+str(id)+'_bracken_order_mpa.txt' for id in IDs]
Joined_map_species_files = ' '.join(MPA_files_species)
os.system('python kraken2/combine_mpa.py -i '+str(Joined_map_species_files)+' -o '+str(args.reads_dir)+'/16S_SILVA138_k2db/mpa_output/combined_bracken_order_mpa.txt')
df=pd.read_csv(str(args.reads_dir)+'/16S_SILVA138_k2db/mpa_output/combined_bracken_order_mpa.txt', sep='\t')
df = df[df['#Classification'].str.contains('\\|o__')]
#pipe character '|' needs double backslash '\\' to ignore because by default the pipe operator '|' in python is by default the bitwise OR operator
df.to_csv(str(args.reads_dir)+'/16S_SILVA138_k2db/mpa_output/filtered_combined_bracken_order_mpa.txt', sep='\t', index=False)

print ('Combining Bracken MPAs for Phylum')
MPA_files_species=[str(args.reads_dir)+'/16S_SILVA138_k2db/mpa_output/'+str(id)+'_bracken_phylum_mpa.txt' for id in IDs]
Joined_map_species_files = ' '.join(MPA_files_species)
os.system('python kraken2/combine_mpa.py -i '+str(Joined_map_species_files)+' -o '+str(args.reads_dir)+'/16S_SILVA138_k2db/mpa_output/combined_bracken_phylum_mpa.txt')
df=pd.read_csv(str(args.reads_dir)+'/16S_SILVA138_k2db/mpa_output/combined_bracken_phylum_mpa.txt', sep='\t')
df = df[df['#Classification'].str.contains('\\|p__')]
#pipe character '|' needs double backslash '\\' to ignore because by default the pipe operator '|' in python is by default the bitwise OR operator
df.to_csv(str(args.reads_dir)+'/16S_SILVA138_k2db/mpa_output/filtered_combined_bracken_phylum_mpa.txt', sep='\t', index=False)



print ('Generating Phylogenetic Tree for genuses')
df1=pd.read_csv(str(args.reads_dir)+'/16S_SILVA138_k2db/biom_output/GG_id_combined_bracken_genuses.txt', sep='\t', usecols=['#OTU ID'])
df1.to_csv(str(args.reads_dir)+'/16S_SILVA138_k2db/tree_output/GG_id_fasta_genuses.txt', sep='\t',index=False)
os.system('seqtk subseq gg_13_5.fasta '+str(args.reads_dir)+'/16S_SILVA138_k2db/tree_output/GG_id_fasta_genuses.txt > '+str(args.reads_dir)+'/16S_SILVA138_k2db/tree_output/GG_id_fasta_genuses.fasta')
os.system('mafft '+str(args.reads_dir)+'/16S_SILVA138_k2db/tree_output/GG_id_fasta_genuses.fasta > '+str(args.reads_dir)+'/16S_SILVA138_k2db/tree_output/GG_id_msa_genuses.fasta')
os.system('FastTree -gtr -nt < '+str(args.reads_dir)+'/16S_SILVA138_k2db/tree_output/GG_id_msa_genuses.fasta > '+str(args.reads_dir)+'/16S_SILVA138_k2db/tree_output/GG_id_genuses.tree')

print ('Generating Phylogenetic Tree for families')
df1=pd.read_csv(str(args.reads_dir)+'/16S_SILVA138_k2db/biom_output/GG_id_combined_bracken_families.txt', sep='\t', usecols=['#OTU ID'])
df1.to_csv(str(args.reads_dir)+'/16S_SILVA138_k2db/tree_output/GG_id_fasta_families.txt', sep='\t',index=False)
os.system('seqtk subseq gg_13_5.fasta '+str(args.reads_dir)+'/16S_SILVA138_k2db/tree_output/GG_id_fasta_families.txt > '+str(args.reads_dir)+'/16S_SILVA138_k2db/tree_output/GG_id_fasta_families.fasta')
os.system('mafft '+str(args.reads_dir)+'/16S_SILVA138_k2db/tree_output/GG_id_fasta_families.fasta > '+str(args.reads_dir)+'/16S_SILVA138_k2db/tree_output/GG_id_msa_families.fasta')
os.system('FastTree -gtr -nt < '+str(args.reads_dir)+'/16S_SILVA138_k2db/tree_output/GG_id_msa_families.fasta > '+str(args.reads_dir)+'/16S_SILVA138_k2db/tree_output/GG_id_families.tree')

print ('Generating Phylogenetic Tree for orders')
df1=pd.read_csv(str(args.reads_dir)+'/16S_SILVA138_k2db/biom_output/GG_id_combined_bracken_orders.txt', sep='\t', usecols=['#OTU ID'])
df1.to_csv(str(args.reads_dir)+'/16S_SILVA138_k2db/tree_output/GG_id_fasta_orders.txt', sep='\t',index=False)
os.system('seqtk subseq gg_13_5.fasta '+str(args.reads_dir)+'/16S_SILVA138_k2db/tree_output/GG_id_fasta_orders.txt > '+str(args.reads_dir)+'/16S_SILVA138_k2db/tree_output/GG_id_fasta_orders.fasta')
os.system('mafft '+str(args.reads_dir)+'/16S_SILVA138_k2db/tree_output/GG_id_fasta_orders.fasta > '+str(args.reads_dir)+'/16S_SILVA138_k2db/tree_output/GG_id_msa_orders.fasta')
os.system('FastTree -gtr -nt < '+str(args.reads_dir)+'/16S_SILVA138_k2db/tree_output/GG_id_msa_orders.fasta > '+str(args.reads_dir)+'/16S_SILVA138_k2db/tree_output/GG_id_orders.tree')



