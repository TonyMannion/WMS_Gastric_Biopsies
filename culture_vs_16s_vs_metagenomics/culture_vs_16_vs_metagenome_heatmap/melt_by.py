import pandas as pd

import numpy as np


df1 = pd.read_csv('combined_OTUs_binary_table.txt', sep='\t') # change if deliminter is "\t" for non-csv files 
print df1
df2 =df1.melt(id_vars=['Key'])

df2['Sample_ID']=df2['Key'].str.split('_').str[0]
df2['Sample_ID_Genus']=df2['Sample_ID']+'_'+df2['variable']


conditions = [
    df2['Key'].str.contains("16s") & df2['value'].eq(1),
    df2['Key'].str.contains("metagenome") & df2['value'].eq(1),
    df2['Key'].str.contains("culture") & df2['value'].eq(1)
]

#codes
#16s =10
#metagenome =20
#culture = 1

choices = [10,20,1]


df2['scores'] = np.select(conditions, choices, default=0)

df3 = pd.pivot_table(df2, values='scores', index='Sample_ID_Genus', aggfunc='sum')


conditions2 = [
    df3['scores'].eq(1),
    df3['scores'].eq(11),
    df3['scores'].eq(21),
	df3['scores'].eq(31)
]

#codes
#1= Culture (+)
#11 = Culture (+), 16s rRNA (+)
#21 = Culture (+), Metagenomics (+)
#31 = Culture (+), 16s rRNA (+), Metagenomics (+)

choices2 = ['Culture (+)','Culture (+), 16s rRNA (+)','Culture (+), Metagenomics (+)','Culture (+), 16s rRNA (+), Metagenomics (+)']

df3['category'] = np.select(conditions2, choices2, default='drop_row')
df3['Sample_ID_Genus']=df3.index
df3[['Sample_ID','Genus']] = df3['Sample_ID_Genus'].str.split('_',expand=True)


df4=df3[df3['category'].str.contains('drop')==False]

df4.to_csv('melted_combined_OTUs_binary_table.txt', sep='\t',columns = ['Sample_ID','Genus','category'])
