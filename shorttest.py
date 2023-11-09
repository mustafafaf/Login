import pandas as pd
import csv








df2=pd.read_csv('users.csv',index_col=0)
if 'me' in df2.index:
    print(df2)


