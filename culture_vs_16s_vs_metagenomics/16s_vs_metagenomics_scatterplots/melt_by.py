import pandas as pd

import numpy as np
from sys import argv

#python merger.py argv1=filename1 argv2=filename2 argv3=header1 argv4=header2

df1 = pd.read_csv('combo.txt', sep='\t') # change if deliminter is "\t" for non-csv files 
print df1
df2 =df1.melt(id_vars=['Data_type','Sample_ID'])




df2.to_csv('combo_out.txt', sep='\t')

