import pandas as pd

pandas_read = pd.read_csv('mcd.csv',sep= ',')
pandas_read.columns = pandas_read.columns['sat_fat','trans_fat']

print(pandas_read)