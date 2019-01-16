import pandas as pd
import numpy as np
import base64

def base64_to_numpy(data):
  _bytes = data.encode('utf-8')
  return np.frombuffer(base64.b64decode(_bytes), dtype=np.float64)


def read_img(filepath):
  ''' Retorna o conteudo em binario da imagem '''

  with open(filepath, "rb") as f:
    return f.read()
