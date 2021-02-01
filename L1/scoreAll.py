# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 10:16:40 2021

@author: LanTian
"""
#import numpy as np
import pandas as pd

df = pd.read_csv("./score.csv")
maxChinese = df[df['语文']==df['语文'].max()]
maxMath= df[df['数学']==df['数学'].max()]
maxEnglish =df[df['英语']==df['英语'].max()]


meanChinese = df['语文'].mean()
meanMath = df['数学'].mean()
meanEnglish = df['英语'].mean()
#meanSum=df['和'].mean()

varChinese = df['语文'].var()
varMath = df['数学'].var()
varEnglish = df['英语'].var()
#varSum=df['和'].var()
scoreAll=df
scoreAll['和']=scoreAll['数学']+scoreAll['语文']+scoreAll['英语']
scoreAll=scoreAll.sort_values('和',ascending=False)
#
#df['maxscore']=df.max(axis=1)
