import pandas as pd
import numpy as np
import base64

df = pd.read_csv('./encodings.csv')
print(df.head())
print(df.dtypes)
str_base = df['encoding'].iloc[0]
byte_base = str_base.encode('utf-8')

e = base64.b64decode(byte_base)
print(np.frombuffer(e, dtype=np.float64))
# print(df['encoding'].iloc[0])
# encoding = df['encoding'].iloc[0]

# print(np.frombuffer(encoding, dtype=np.float64))
