import pandas as pd

import numpy as np


df1 = pd.read_csv('combined_OTUs_binary_table.txt', sep='\t') # change if deliminter is "\t" for non-csv files 

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
	df3['scores'].eq(31),
	df3['scores'].eq(10),
	df3['scores'].eq(20),
	df3['scores'].eq(30),
]

#codes
#1= Culture (+)
#11 = Culture (+), 16s rRNA (+)
#21 = Culture (+), Metagenomics (+)
#31 = Culture (+), 16s rRNA (+), Metagenomics (+)
#10 = 16s rRNA (+)
#20 = Metagenomics (+)
#30 = 16s rRNA (+), Metagenomics (+)

choices2 = ['Culture (+)','Culture (+), 16s rRNA (+)','Culture (+), Metagenomics (+)','Culture (+), 16s rRNA (+), Metagenomics (+)','16s rRNA (+)','Metagenomics (+)','16s rRNA (+), Metagenomics (+)']

df3['detection_results'] = np.select(conditions2, choices2, default='drop_row')

conditions3 = [
    df3['scores'].eq(1),
    df3['scores'].eq(11),
    df3['scores'].eq(21),
	df3['scores'].eq(31),
	df3['scores'].eq(10),
	df3['scores'].eq(20),
	df3['scores'].eq(30),
]

#codes
#1= Culture (+)
#11 = Culture (+), 16s rRNA (+)
#21 = Culture (+), Metagenomics (+)
#31 = Culture (+), 16s rRNA (+), Metagenomics (+)
#10 = 16s rRNA (+)
#20 = Metagenomics (+)
#30 = 16s rRNA (+), Metagenomics (+)

choices3 = ['Culture (+)','16s rRNA (+)','WMS (+)','16s rRNA (+), WMS (+)','16s rRNA (+)','WMS (+)','16s rRNA (+), WMS (+)']

df3['category'] = np.select(conditions3, choices3, default='drop_row')


conditions4 = [
    df3['scores'].eq(1),
    df3['scores'].eq(11),
    df3['scores'].eq(21),
	df3['scores'].eq(31),
	df3['scores'].eq(10),
	df3['scores'].eq(20),
	df3['scores'].eq(30),
]

#codes
#1= Culture (+)
#11 = Culture (+), 16s rRNA (+)
#21 = Culture (+), Metagenomics (+)
#31 = Culture (+), 16s rRNA (+), Metagenomics (+)
#10 = 16s rRNA (+)
#20 = Metagenomics (+)
#30 = 16s rRNA (+), Metagenomics (+)

choices4 = ['Yes','Yes','Yes','Yes','No','No','No']


df3['culture'] = np.select(conditions4, choices4, default='drop_row')



df3['Sample_ID_Genus']=df3.index
df3[['Sample_ID','Genus']] = df3['Sample_ID_Genus'].str.split('_',expand=True)





df4=df3[df3['category'].str.contains('drop')==False]

df5 = pd.read_csv('meta.txt', sep='\t') # change if deliminter is "\t" for non-csv files 

df6 = df4.merge(df5, left_on='Sample_ID', right_on='Location')


df6.to_csv('melted_combined_OTUs_binary_table.txt', sep='\t',columns = ['Sample_ID','Genus','category','Hp_Status','Risk_Group','culture','detection_results'])
