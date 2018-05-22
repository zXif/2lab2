# -*- coding: cp1251 -*-
import pandas as pd
import os

def readframe():
        print "Loading data, please  wait..."
        files = os.listdir('data')
        df1 = pd.DataFrame()
        for filename in files:
                province=int(filename.split('_')[2])
                provkeys={1: 22, 2: 24, 3: 23, 4: 25, 5: 3, 6: 4, 7: 8, 8: 19, 9: 20, 10: 21, 11: 9, 12: 26, 13: 10, 14: 11, 15: 12, 16: 13, 17: 14, 18: 15, 19: 16, 20: 27, 21: 17, 22: 18, 23: 6, 24: 1, 25: 2, 26: 7, 27: 5}
                dfile = pd.read_csv('data/'+filename,index_col=False, skiprows=1,
                         sep=r'\s+,*|,\s*', 
                         names=['year', 'week', 'SMN', 'SMT', 'VCI', 'TCI', 'VHI'], engine = 'python')
                dfile=dfile[:-1].dropna(axis=0, how='any')
                dfile= dfile[(dfile['VHI'] >= 0) & (dfile['VHI'] <= 100)]
                dfile['province']=provkeys.get(province)
                df1 = df1.append(dfile)
        files = os.listdir('data2')
        df2 = pd.DataFrame()
        print "I need some extra seconds..."
        for filename in files:
                dfile = pd.read_csv('data2/'+filename,index_col=False, skiprows=1,
                         sep=r'\s+,*|,\s*', 
                         names=['year', 'week', '0', '5', '10', '15', '20', '25', '30', '35', '40', '45', '50', '55', '60', '65', '70', '75', '80', '85', '90', '95','100'], engine = 'python')
                dfile=dfile[:-1].dropna(axis=0, how='any')
                df2 = df2.append(dfile)
        result= pd.concat([df1.iloc[:,:], df2.iloc[:,2:]], axis=1)
        analyze(result)

     
def analyze(df):
        province=int(input("Enter province ID for analyze:"))
        sindex = int(input("1 - for selected year, 2 - for all years\n"))
        if sindex == 1:
                year=str(input("Enter year:"))
                dfs=df[(df['year'] == year) & (df['province'] == province)]
                print dfs
                print "Maximum VHI", dfs['VHI'].max()
                print "Minimum VHI", dfs['VHI'].min()
        elif sindex == 2:
                dfs=df[df['province'] == province]
                print dfs
                svhiindex = raw_input("E - extremal years, N - normal years\n")
                if svhiindex == "E":
                        dfl = dfs[dfs['VHI'] < 40]
                elif svhiindex == "N":
                        dfl = dfs[dfs['VHI'] > 60]
                print svhiindex, "VHI-index years:", sorted(list(set(dfl['year'])))
readframe()
