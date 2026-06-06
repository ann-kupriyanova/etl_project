import pandas as pd
df = pd.read_csv('data\data_transform.csv', encoding = 'utf-8', delimiter = ',')
a = df.describe()
a = str(a)
with open ('data\describe_data.txt', 'w') as i:
    i.write(a)