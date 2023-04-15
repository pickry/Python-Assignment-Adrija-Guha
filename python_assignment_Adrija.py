# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 14:31:01 2023

@author: Adrija Guha
"""
import pandas as pd
dp = pd.read_excel("C:/Users/Adrija Guha/Documents/pandas/Input1.xlsx")
dp2 = pd.read_excel("C:/Users/Adrija Guha/Documents/pandas/input2.xlsx")

df = pd.DataFrame(dp)
df2 = pd.DataFrame(dp2)
Names = df['Name']
Teams = df['Team Name']
U_id = df['User ID']
statements = df2['total_statements']
reasons = df2['total_reasons']
n = len(Names)
LB1 = {}
LB2 = []
for i in range(n):
    if Teams[i] in LB1:
        LB1[Teams[i]][0] += statements[i]
        LB1[Teams[i]][1] += reasons[i]
        LB1[Teams[i]][2] += 1
    else:
        LB1[Teams[i]] = [statements[i], reasons[i], 1]
    LB2.append([(reasons[i]+ statements[i]), Names[i], statements[i], reasons[i], U_id[i]])
output1 = []
for i in LB1:
    LB1[i][0] = round(LB1[i][0] / LB1[i][2], 2)
    LB1[i][1] = round(LB1[i][1] / LB1[i][2], 2)
    output1.append([LB1[i][0],LB1[i][1], i])
output1.sort(reverse = True)
LB2.sort(reverse = True)

o = len(output1)
print("                   Team Wise Leaderboard")
print(['Team Rank','Thinking Teams Leaderboard','Average Statements','Average Reasons'])
for i in range(o):
    print(f'{i+1} ,{output1[i][2]}, {output1[i][0]}, {output1[i][1]}')
    print('\n')

print("                   Leaderboard Individual")
print(['Rank','Name','UID','No. of Statements','No. of Reasons'])
for i in range(n):
    print(f'{i+1}, {LB2[i][1]}, {LB2[i][4]}, {LB2[i][2]}, {LB2[i][3]}')
    print('\n')
    
    



