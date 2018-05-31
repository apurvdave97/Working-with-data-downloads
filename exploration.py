import pandas as pd
import numpy as np

if __name__=="__main__":
    data=pd.read_csv('CRDC2013_14.csv',
                     encoding='Latin-1')
    print(data['JJ'].value_counts())
    print(data['SCH_STATUS_MAGNET'].value_counts())
    
    pivot_jj=pd.pivot_table(data,values=
                   ['TOT_ENR_M', 'TOT_ENR_F'],
                   index='JJ',aggfunc=np.sum)
    pivot_sch=pd.pivot_table(data,values=
                   ['TOT_ENR_M', 'TOT_ENR_F'],
                   index='SCH_STATUS_MAGNET',
                             aggfunc=np.sum)
    print(pivot_jj)
    print(pivot_sch)
    