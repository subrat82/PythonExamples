import pandas as pd
import numpy as np
from datetime import datetime

with open('logfile.txt') as f:
    txt = f.readlines()

len(txt)

n = len(txt)
print(n)
for i in range(n):
    txt[i] = txt[i].strip()

    txt[0].split(']')
   # txt[0].split(']')[1]
    #txt[0].split(']')[1].upper()

    s = txt[0].split(']')[0].strip('[')
    dtfmt = '%m/%d/%Y %I:%M:%S %p'  # %H -> 24 hours, %I-> 12 hours
    dt = datetime.strptime(s, dtfmt)

    col1 = []
    col2 = []
    col3 = []

for line in txt:
    s1=line.split(']')[0].strip('[')
    dt = datetime.strptime(s1, dtfmt)
    col1.append(dt)
    s= line.split(']')[1].strip().split(':')
    col2.append(s[0])
    if len(s) == 2:
        col3.append(s[1])
    else:
        col3.append(np.nan)

        df = pd.DataFrame([col1, col2, col3])
        df = df.T
        df.columns = ['datetime', 'event_name', 'event_result']

        df['delta_t'] = df.datetime - df.datetime[0]

        df['delta_t_seconds'] = 0
        for i in range(df.shape[0]):
            df.ix[i, 'delta_t_seconds'] = df.delta_t.iloc[i].seconds

            df.to_csv('test_log.csv', index=False)

