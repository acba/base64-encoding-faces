import os
import multiprocessing
import hashlib
import csv
import base64
import sqlite3

import pandas as pd
import face_recognition

import utils.misc as misc


number_of_workers = 8

data_path = './data'
if not os.path.exists(data_path):
  os.makedirs(data_path)

def __run(idx, filename, path, num_jitters=1, upsample=False):
  if filename.endswith(".jpg"):
    filepath = os.path.join(path, filename)

    cpf = filename.split('-')[0]
    img = face_recognition.load_image_file(filepath)
    hash = hashlib.sha256(misc.read_img(filepath)).hexdigest().upper()

    # if not existe:
    encodings = face_recognition.face_encodings(img, num_jitters=num_jitters)
    if upsample:
      if len(encodings) == 0: # Não encontrou ninguem
        face_locations = face_recognition.face_locations(img, number_of_times_to_upsample=2)
        encodings = face_recognition.face_encodings(img, known_face_locations=face_locations, num_jitters=100)

    if len(encodings) == 1:
      encoding = encodings[0]
      byte_encoding = encoding.tostring()
      str_base64_encoding = base64.b64encode(byte_encoding).decode('utf-8')

      return {
        'cpf': cpf,
        'encoding': str_base64_encoding,
        'hash': hash
      }
    elif len(encodings) > 1:
      with open(os.path.join(data_path, 'errors.log'), mode='a') as f:
        print(f'{filepath} não pode ser codificado, mais de um rosto detectado.')
        print(f'{filepath} não pode ser codificado, mais de um rosto detectado.', file=f)

    else:
      with open(os.path.join(data_path, 'errors.log'), mode='a') as f:
        print(f'{filepath} não pode ser codificado.')
        print(f'{filepath} não pode ser codificado.', file=f)

  return None

def process(rootpath, num_jitters=1, upsample=False):

  print('\n')
  print(' ------------- Iniciando ------------- ')
  print(f' num_jitters: {num_jitters}')
  print(f' upsample: {upsample}')
  print('\n')

  paths = os.listdir(rootpath)
  print(f'Pastas de fotos: {paths}')

  with open(os.path.join(data_path, f'tb_facial_encoding.jitter_{num_jitters}.upsample_{upsample}.csv'), mode='w') as f:
    fieldnames = ['hash', 'cpf', 'encoding']
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    writer.writeheader()

    for p in paths:
      path = os.path.join(rootpath, p)
      n_files = len(os.listdir(path))
      print(f'Processando {n_files} arquivos de {path}')

      entradas = [(idx, filename, path, num_jitters, upsample) for idx, filename in enumerate(os.listdir(path))]
      print('Entradas processadas.')

      with multiprocessing.Pool(number_of_workers) as p:
        encodings = p.starmap(__run, entradas)
        encodings = list(filter(lambda x: x is not None, encodings))
        tuples = [(e['cpf'], e['hash'], e['encoding']) for e in encodings]

        writer.writerows(encodings)

  print(' ------------- Finalizado ------------- ')

rootpath = '/home/cesar/workspace/dados/fotos_sem_assinatura'

# process(rootpath, num_jitters=1)
# process(rootpath, num_jitters=1, upsample=True)
# process(rootpath, num_jitters=2)
# process(rootpath, num_jitters=2, upsample=True)
process(rootpath, num_jitters=3)
process(rootpath, num_jitters=3, upsample=True)
process(rootpath, num_jitters=5)
process(rootpath, num_jitters=5, upsample=True)
# process(rootpath, num_jitters=10)