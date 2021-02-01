# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 14:03:29 2021

@author: LanTian
"""


import pandas as pd
def qx(x):
    x=x.replace('一汽-大众','一汽大众')
    return x

df = pd.read_csv('./car_complain.csv')
df['brand']=df['brand'].apply(qx)
resultCount=df.groupby(['brand'])['status'].agg(['count'])
resultstatus=df.drop('status',axis=1).join(df['status'].str.get_dummies())
tags=resultstatus.columns[7:]
resultstatus=resultstatus.groupby(['brand'])[tags].agg('sum')
result=resultstatus.merge(resultCount,left_index=True,right_index=True,how='left')
result['反馈率']=result['处理反馈']/result['count']
result=result.sort_values(['反馈率'],ascending=False)
print(result[0:10])#获取处理率前十名的汽车品牌
#carstatus2=carstatsu2.merge()