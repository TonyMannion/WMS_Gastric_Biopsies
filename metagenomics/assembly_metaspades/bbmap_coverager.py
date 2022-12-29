import pandas as pd
import numpy as np
import os
import os.path
import argparse
from os import path

os.system('mkdir bbmap_coverage_out')

file_names_210222Fox=['210222Fox_D21-2140','210222Fox_D21-2141','210222Fox_D21-2142','210222Fox_D21-2143','210222Fox_D21-2144','210222Fox_D21-2145','210222Fox_D21-2146','210222Fox_D21-2147']

taxa_list=['Bacteria_Archaea','Viruses','Eukaryota_not_human','Unclassified']

for taxa in taxa_list:
	for file in file_names_210222Fox:


		os.system('mkdir bbmap_coverage_out/'+str(taxa))
		os.system('/home/dcm/BBMap_38.90/bbmap/bbmap.sh in=/home/dcm/210222Fox/all_masked_human/extracted_reads/'+str(taxa)+'/'+str(taxa)+'_'+str(file)+'-1_concat.fastq in2=/home/dcm/210222Fox/all_masked_human/extracted_reads/'+str(taxa)+'/'+str(taxa)+'_'+str(file)+'-2_concat.fastq ref=/home/dcm/210222Fox/all_masked_human/contig_assembly/'+str(taxa)+'/spades_'+str(taxa)+'_'+str(file)+'/contigs.fasta covstats=bbmap_coverage_out/'+str(taxa)+'/spades_'+str(taxa)+'_'+str(file)+'_constats.txt covhist=bbmap_coverage_out/'+str(taxa)+'/spades_'+str(taxa)+'_'+str(file)+'covhist.txt basecov=bbmap_coverage_out/'+str(taxa)+'/spades_'+str(taxa)+'_'+str(file)+'_basecov.txt bincov=bbmap_coverage_out/'+str(taxa)+'/spades_'+str(taxa)+'_'+str(file)+'_bincov.txt > bbmap_coverage_out/'+str(taxa)+'/bbmap_spades_'+str(taxa)+'_'+str(file)+'_out.txt')

		os.system('/home/dcm/BBMap_38.90/bbmap/bbmap.sh in=/home/dcm/210222Fox/all_masked_human/extracted_reads/'+str(taxa)+'/'+str(taxa)+'_'+str(file)+'-1_concat.fastq in2=/home/dcm/210222Fox/all_masked_human/extracted_reads/'+str(taxa)+'/'+str(taxa)+'_'+str(file)+'-2_concat.fastq ref=/home/dcm/210222Fox/all_masked_human/contig_assembly/'+str(taxa)+'/metaspades_'+str(taxa)+'_'+str(file)+'/contigs.fasta covstats=bbmap_coverage_out/'+str(taxa)+'/metaspades_'+str(taxa)+'_'+str(file)+'_constats.txt covhist=bbmap_coverage_out/'+str(taxa)+'/metaspades_'+str(taxa)+'_'+str(file)+'covhist.txt basecov=bbmap_coverage_out/'+str(taxa)+'/metaspades_'+str(taxa)+'_'+str(file)+'_basecov.txt bincov=bbmap_coverage_out/'+str(taxa)+'/metaspades_'+str(taxa)+'_'+str(file)+'_bincov.txt > bbmap_coverage_out/'+str(taxa)+'/bbmap_metaspades_'+str(taxa)+'_'+str(file)+'_out.txt')

		os.system('/home/dcm/BBMap_38.90/bbmap/bbmap.sh in=/home/dcm/210222Fox/all_masked_human/extracted_reads/'+str(taxa)+'/'+str(taxa)+'_'+str(file)+'-1_concat.fastq in2=/home/dcm/210222Fox/all_masked_human/extracted_reads/'+str(taxa)+'/'+str(taxa)+'_'+str(file)+'-2_concat.fastq ref=/home/dcm/210222Fox/all_masked_human/contig_assembly/'+str(taxa)+'/MEGAHIT/MEGAHIT_'+str(taxa)+'_'+str(file)+'/'+str(file)+'.contigs.fa covstats=bbmap_coverage_out/'+str(taxa)+'/MEGAHIT_'+str(taxa)+'_'+str(file)+'_constats.txt covhist=bbmap_coverage_out/'+str(taxa)+'/MEGAHIT_'+str(taxa)+'_'+str(file)+'covhist.txt basecov=bbmap_coverage_out/'+str(taxa)+'/MEGAHIT_'+str(taxa)+'_'+str(file)+'_basecov.txt bincov=bbmap_coverage_out/'+str(taxa)+'/MEGAHIT_'+str(taxa)+'_'+str(file)+'_bincov.txt > bbmap_coverage_out/'+str(taxa)+'/bbmap_MEGAHIT__'+str(taxa)+'_'+str(file)+'_out.txt')

		os.system('/home/dcm/BBMap_38.90/bbmap/bbmap.sh in=/home/dcm/210222Fox/all_masked_human/extracted_reads/'+str(taxa)+'/'+str(taxa)+'_'+str(file)+'-1_concat.fastq in2=/home/dcm/210222Fox/all_masked_human/extracted_reads/'+str(taxa)+'/'+str(taxa)+'_'+str(file)+'-2_concat.fastq ref=/home/dcm/210222Fox/all_masked_human/contig_assembly/'+str(taxa)+'/MEGAHIT_sensitive/MEGAHIT_sensitive_'+str(taxa)+'_'+str(file)+'/'+str(file)+'.contigs.fa covstats=bbmap_coverage_out/'+str(taxa)+'/MEGAHIT_sensitive_'+str(taxa)+'_'+str(file)+'_constats.txt covhist=bbmap_coverage_out/'+str(taxa)+'/MEGAHIT_sensitive_'+str(taxa)+'_'+str(file)+'covhist.txt basecov=bbmap_coverage_out/'+str(taxa)+'/MEGAHIT_sensitive_'+str(taxa)+'_'+str(file)+'_basecov.txt bincov=bbmap_coverage_out/'+str(taxa)+'/MEGAHIT_sensitive_'+str(taxa)+'_'+str(file)+'_bincov.txt > bbmap_coverage_out/'+str(taxa)+'/bbmap_MEGAHIT_sensitive_'+str(taxa)+'_'+str(file)+'_out.txt')


file_names_210713Fox=['210713Fox_D21-6682','210713Fox_D21-6683','210713Fox_D21-6684','210713Fox_D21-6685','210713Fox_D21-6686','210713Fox_D21-6687','210713Fox_D21-6688','210713Fox_D21-6689','210713Fox_D21-6690','210713Fox_D21-6691','210713Fox_D21-6692','210713Fox_D21-6693']

taxa_list=['Bacteria_Archaea','Viruses','Eukaryota_not_human','Unclassified']

for taxa in taxa_list:
	for file in file_names_210713Fox:
		os.system('mkdir bbmap_coverage_out/'+str(taxa))
		os.system('/home/dcm/BBMap_38.90/bbmap/bbmap.sh in=/home/dcm/210713Fox/all_masked_human/extracted_reads/'+str(taxa)+'/'+str(taxa)+'_'+str(file)+'-1_concat.fastq in2=/home/dcm/210713Fox/all_masked_human/extracted_reads/'+str(taxa)+'/'+str(taxa)+'_'+str(file)+'-2_concat.fastq ref=/home/dcm/210713Fox/all_masked_human/contig_assembly/'+str(taxa)+'/spades_'+str(taxa)+'_'+str(file)+'/contigs.fasta covstats=bbmap_coverage_out/'+str(taxa)+'/spades_'+str(taxa)+'_'+str(file)+'_constats.txt covhist=bbmap_coverage_out/'+str(taxa)+'/spades_'+str(taxa)+'_'+str(file)+'covhist.txt basecov=bbmap_coverage_out/'+str(taxa)+'/spades_'+str(taxa)+'_'+str(file)+'_basecov.txt bincov=bbmap_coverage_out/'+str(taxa)+'/spades_'+str(taxa)+'_'+str(file)+'_bincov.txt> bbmap_coverage_out/'+str(taxa)+'/bbmap_spades_'+str(taxa)+'_'+str(file)+'_out.txt')


		os.system('/home/dcm/BBMap_38.90/bbmap/bbmap.sh in=/home/dcm/210713Fox/all_masked_human/extracted_reads/'+str(taxa)+'/'+str(taxa)+'_'+str(file)+'-1_concat.fastq in2=/home/dcm/210713Fox/all_masked_human/extracted_reads/'+str(taxa)+'/'+str(taxa)+'_'+str(file)+'-2_concat.fastq ref=/home/dcm/210713Fox/all_masked_human/contig_assembly/'+str(taxa)+'/metaspades_'+str(taxa)+'_'+str(file)+'/contigs.fasta covstats=bbmap_coverage_out/'+str(taxa)+'/metaspades_'+str(taxa)+'_'+str(file)+'_constats.txt covhist=bbmap_coverage_out/'+str(taxa)+'/metaspades_'+str(taxa)+'_'+str(file)+'covhist.txt basecov=bbmap_coverage_out/'+str(taxa)+'/metaspades_'+str(taxa)+'_'+str(file)+'_basecov.txt bincov=bbmap_coverage_out/'+str(taxa)+'/metaspades_'+str(taxa)+'_'+str(file)+'_bincov.txt> bbmap_coverage_out/'+str(taxa)+'/bbmap_metaspades_'+str(taxa)+'_'+str(file)+'_out.txt')


		os.system('/home/dcm/BBMap_38.90/bbmap/bbmap.sh in=/home/dcm/210713Fox/all_masked_human/extracted_reads/'+str(taxa)+'/'+str(taxa)+'_'+str(file)+'-1_concat.fastq in2=/home/dcm/210713Fox/all_masked_human/extracted_reads/'+str(taxa)+'/'+str(taxa)+'_'+str(file)+'-2_concat.fastq ref=/home/dcm/210713Fox/all_masked_human/contig_assembly/'+str(taxa)+'/MEGAHIT/MEGAHIT_'+str(taxa)+'_'+str(file)+'/'+str(file)+'.contigs.fa covstats=bbmap_coverage_out/'+str(taxa)+'/MEGAHIT_'+str(taxa)+'_'+str(file)+'_constats.txt covhist=bbmap_coverage_out/'+str(taxa)+'/MEGAHIT_'+str(taxa)+'_'+str(file)+'covhist.txt basecov=bbmap_coverage_out/'+str(taxa)+'/MEGAHIT_'+str(taxa)+'_'+str(file)+'_basecov.txt bincov=bbmap_coverage_out/'+str(taxa)+'/MEGAHIT_'+str(taxa)+'_'+str(file)+'_bincov.txt > bbmap_coverage_out/'+str(taxa)+'/bbmap_MEGAHIT__'+str(taxa)+'_'+str(file)+'_out.txt')

		os.system('/home/dcm/BBMap_38.90/bbmap/bbmap.sh in=/home/dcm/210713Fox/all_masked_human/extracted_reads/'+str(taxa)+'/'+str(taxa)+'_'+str(file)+'-1_concat.fastq in2=/home/dcm/210713Fox/all_masked_human/extracted_reads/'+str(taxa)+'/'+str(taxa)+'_'+str(file)+'-2_concat.fastq ref=/home/dcm/210713Fox/all_masked_human/contig_assembly/'+str(taxa)+'/MEGAHIT_sensitive/MEGAHIT_sensitive_'+str(taxa)+'_'+str(file)+'/'+str(file)+'.contigs.fa covstats=bbmap_coverage_out/'+str(taxa)+'/MEGAHIT_sensitive_'+str(taxa)+'_'+str(file)+'_constats.txt covhist=bbmap_coverage_out/'+str(taxa)+'/MEGAHIT_sensitive_'+str(taxa)+'_'+str(file)+'covhist.txt basecov=bbmap_coverage_out/'+str(taxa)+'/MEGAHIT_sensitive_'+str(taxa)+'_'+str(file)+'_basecov.txt bincov=bbmap_coverage_out/'+str(taxa)+'/MEGAHIT_sensitive_'+str(taxa)+'_'+str(file)+'_bincov.txt > bbmap_coverage_out/'+str(taxa)+'/bbmap_MEGAHIT_sensitive_'+str(taxa)+'_'+str(file)+'_out.txt')
