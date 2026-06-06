import pandas as pd

df = pd.read_csv('data\data.csv', encoding = 'utf-8', delimiter = ',')
df['avg_chek'] = round(df['total_spend'] / df['cnt_trans'], 2)
df['group'] = pd.cut(df['total_spend'],
                     bins = [0, 1000, 5000, 10000],
                     labels = ['Low', 'Med', 'VIP'])
df['status'] = 'active'
df.loc[df['days_last_act'] > 90, 'status'] = 'inactive'
#print(df)
df.to_csv('data\data_transform.csv', index = False)
