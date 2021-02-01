# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 10:32:11 2021

@author: LanTian
"""


import pandas as pd
def qx(x):
    x=x.replace('一汽-大众','一汽大众')
    return x

df = pd.read_csv('./car_complain.csv')
df['brand']=df['brand'].apply(qx)
df = df.drop('problem',axis=1).join(df.problem.str.get_dummies(','))
bresult = df.groupby(['car_model'])['id'].agg(['count'])
ptags=df.columns[7:]
bresult2 = df.groupby(['car_model'])[ptags].agg('sum')
bresult2 =bresult.merge(bresult2,left_index=True,right_index=True,how='left')
bresult2 = bresult2.sort_values('count',ascending = False)
print(bresult2)#输出按照车型统计的问题总数
bresult3 = bresult2.sort_values('A14',ascending = False)
bresult3.reset_index(inplace=True)
bresult3= bresult3[['car_model','A14']]
print(bresult3)#输出问题A14的车型排序
#print(bresult3)
