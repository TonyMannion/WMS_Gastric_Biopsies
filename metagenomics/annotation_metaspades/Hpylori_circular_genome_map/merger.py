import numpy as np
import pandas as pd

# Read the two files into pandas dataframes
df1 = pd.read_csv('merged_protein_85962_blast_out.txt', sep='\t')
df2 = pd.read_csv('85962.8.PATRIC.features_VF_merged.txt', sep='\t')

# Merge the two dataframes on the specified column
merged_df = pd.merge(df1, df2, left_on='sseqid', right_on='patric_id', how='left')

# Write the merged dataframe to a new file
merged_df.to_csv('merged_file.txt', sep='\t', index=False)
