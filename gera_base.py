import os
import multiprocessing
import hashlib
import csv
import base64
import sqlite3

import numpy as np
import pandas as pd
import face_recognition

number_of_workers = 16

data_path = './data'
if not os.path.exists(data_path):
  os.makedirs(data_path)

connection = sqlite3.connect(os.path.join(data_path,'db.sqlite3'))

def __run(idx, filename, path):
  if filename.endswith(".jpg"):
    filepath = os.path.join(path, filename)

    cpf = filename.split('-')[0]
    img = face_recognition.load_image_file(filepath)
    hash = hashlib.sha256(img).hexdigest().upper()

    res = connection.execute(f'SELECT EXISTS(SELECT 1 FROM encodings WHERE hash=?)', (hash,))
    existe, = res.fetchone()
   
    if not existe:
      encodings = face_recognition.face_encodings(img)
      if len(encodings) == 1:
        encoding = encodings[0]
        byte_encoding = encoding.tostring()
        str_base64_encoding = base64.b64encode(byte_encoding).decode('utf-8')

        connection.execute('INSERT INTO encodings VALUES (?,?,?)', (hash, cpf, str_base64_encoding))
        connection.commit()
        return True
        # return {
        #   'cpf': cpf,
        #   'encoding': str_base64_encoding,
        #   'hash': hash
        # }
      elif len(encodings) > 1:
        print(f'Arquivo {filepath} não pode ser codificado, mais de um rosto detectado - concluído.')
      else:
        print(f'Arquivo {filepath} não pode ser codificado - concluído.')


  return None

def process(rootpath):
  paths = os.listdir(rootpath)
  print(f'Pastas de fotos: {paths}')

  connection.execute('CREATE TABLE IF NOT EXISTS encodings(hash, cpf, encoding)')

  with open(os.path.join(data_path, 'encodings.csv'), mode='w') as f:
    fieldnames = ['hash', 'cpf', 'encoding']
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    writer.writeheader()
      
    for p in paths[:1]:
      path = os.path.join(rootpath, p)
      n_files = len(os.listdir(path))
      print(f'Processando {n_files} arquivos de {path}')

      entradas = [(idx, filename, path) for idx, filename in enumerate(os.listdir(path))]
      print('Entradas processadas.')

      with multiprocessing.Pool(number_of_workers) as p:
        encodings = p.starmap(__run, entradas)
        # encodings = list(filter(lambda x: x is not None, encodings))
        # tuples = [(e['cpf'], e['hash'], e['encoding']) for e in encodings]
        
        # writer.writerows(encodings)

rootpath = '/home/acba/workspace/github/siap-reconhecimentofacial/data/fotos'
process(rootpath)