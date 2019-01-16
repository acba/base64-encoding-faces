import pandas as pd
import numpy as np
import base64
import time
import csv

def base64_to_numpy(data):
  _bytes = data.encode('utf-8')
  return np.frombuffer(base64.b64decode(_bytes), dtype=np.float64)

ti = time.time()
df = pd.read_csv('./data/encodings.csv')
print(f'Carregamento da base em {time.time() - ti} s')

print(df.head())
print(df.dtypes)
# str_base = df['encoding'].iloc[0]
# byte_base = str_base.encode('utf-8')

# e = base64.b64decode(byte_base)
# print(np.frombuffer(e, dtype=np.float64))
# print(df['encoding'].iloc[0])
# encoding = df['encoding'].iloc[0]

# print(np.frombuffer(encoding, dtype=np.float64))

ti = time.time()
arr = [ base64_to_numpy(r) for r in df['encoding']]
print(f'Processamento da base em {time.time() - ti} s')

ti = time.time()
arr = [ {'cpf': r[2], 'encoding': base64_to_numpy(r[3]) } for r in df.to_records()]
print(f'Processamento da base em {time.time() - ti} s')

ti = time.time()
arr_enc = [ base64_to_numpy(r) for r in df['encoding']]
arr_cpf = [ r for r in df['cpf']]
arr = [ {'cpf': arr_cpf[idx], 'encoding': enc } for idx, enc in enumerate(arr_enc)]
print(f'Processamento da base em {time.time() - ti} s')

ti = time.time()
arr = [ { 'cpf': r['cpf'], 'encoding': base64_to_numpy(r['encoding']) } for idx, r in df.iterrows()]
print(f'Processamento da base em {time.time() - ti} s')
