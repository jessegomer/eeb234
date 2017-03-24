#!/usr/bin/python
from configobj import ConfigObj
config = ConfigObj(/Users/zackgold/Documents/UCLA_phd/Projects/anacapa/config_file.txt)



import numpy
import pandas as pd
alldata=pd.read_csv(config['OTU_TABLE_TXT'],sep='\t', header=1)
labels=alldata[[config['LABEL_OTU'],config['LABEL_TAX']]]
controls=alldata[[config['CONTROLS_ALL']]]
data=alldata.drop(['#OTU ID','taxonomy',config['CONTROLS_ALL']],axis=1)
def decontaminate_column(data_column,control_column):
    column = data_column.copy()
    column.ix[column <= control_column] = 0
    return column

def decontaminate(dataframe,control):
    for control_name in control.columns.values.tolist():
        print(control_name)
        dataframe=dataframe.apply(lambda c: decontaminate_column(c, control[control_name]), axis=0)
    return dataframe
data=decontaminate(data,controls)
cleaned_otu_table = pd.concat([labels['#OTU ID'],controls,data,labels['taxonomy']],axis=1)
with open(config['OTU_TABLE_TXT'], 'r') as f:
    comment=f.readline()
    print(comment.strip())
with open(config['CLEANED_OTU'], 'w') as f:
    f.write(comment)
cleaned_otu_table.to_csv(config['CLEANED_OTU'], sep='\t', mode='a',index=False)