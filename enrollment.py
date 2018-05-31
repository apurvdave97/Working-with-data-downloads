import pandas as pd

if __name__=='__main__':
    data=pd.read_csv('CRDC2013_14.csv',
                     encoding='Latin-1')
    data['total_enrollment']=data['TOT_ENR_M']+data['TOT_ENR_F']
    
    all_enrollment =data['total_enrollment'].sum()
    l=['SCH_ENR_HI_M','SCH_ENR_HI_F','SCH_ENR_AM_M',
       'SCH_ENR_AM_F','SCH_ENR_AS_M','SCH_ENR_AS_F',
       'SCH_ENR_HP_M','SCH_ENR_HP_F','SCH_ENR_BL_M',
       'SCH_ENR_BL_F','SCH_ENR_WH_M','SCH_ENR_WH_F',
       'SCH_ENR_TR_M','SCH_ENR_TR_F',]
    total_HI=0
    total_AM=0
    total_AS=0
    total_HP=0
    total_BL=0
    total_WH=0
    total_TR=0
    l_1 = [total_HI,total_AM,total_AS,
           total_HP,total_BL,total_WH,
           total_TR]
   
    l_2 = ['total_HI','total_AM','total_AS',
           'total_HP','total_BL','total_WH',
           'total_TR']

    
    dict={}
    for i in range(0,7):
        l_1[i] = 0
        for j in range(2*i,(2*i)+1):
            l_1[i]= l_1[i] + data[l[j]].sum()
        dict[l_2[i]] = l_1[i]
        
    percent = {}
    for k,v in dict.items():
        percent[k] = (v/all_enrollment)*100
        
    print(percent)
        