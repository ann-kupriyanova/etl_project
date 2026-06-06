import pandas as pd
import numpy as np

n = 1000
np.random.seed(42)
df = pd.DataFrame({
    'id': range(1, n + 1),
    'cnt_trans': np.random.randint(1, 100, n),
    'total_spend': np.random.randint(10, 10000, n),
    'days_last_act': np.random.randint(1, 365, n)
})
#print(df)
df.to_csv('data\data.csv', index = False)
