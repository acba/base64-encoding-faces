import csv
import os

import pandas as pd

import utils.misc as misc


data_path = './data'
if not os.path.exists(data_path):
  os.makedirs(data_path)

def main(filename='encodings.csv'):

  dtypes = {'hash': object, 'cpf': object, 'encoding': object}
  df = pd.read_csv(f'./data/{filename}', dtype=dtypes)

  with open(os.path.join(data_path, f'{filename}.novo'), mode='w') as f:
    fieldnames = ['hash', 'cpf', 'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8',
                  'f9', 'f10', 'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17',
                  'f18', 'f19', 'f20', 'f21', 'f22', 'f23', 'f24', 'f25', 'f26',
                  'f27', 'f28', 'f29', 'f30', 'f31', 'f32', 'f33', 'f34', 'f35',
                  'f36', 'f37', 'f38', 'f39', 'f40', 'f41', 'f42', 'f43', 'f44',
                  'f45', 'f46', 'f47', 'f48', 'f49', 'f50', 'f51', 'f52', 'f53',
                  'f54', 'f55', 'f56', 'f57', 'f58', 'f59', 'f60', 'f61', 'f62',
                  'f63', 'f64', 'f65', 'f66', 'f67', 'f68', 'f69', 'f70', 'f71',
                  'f72', 'f73', 'f74', 'f75', 'f76', 'f77', 'f78', 'f79', 'f80',
                  'f81', 'f82', 'f83', 'f84', 'f85', 'f86', 'f87', 'f88', 'f89',
                  'f90', 'f91', 'f92', 'f93', 'f94', 'f95', 'f96', 'f97', 'f98',
                  'f99', 'f100', 'f101', 'f102', 'f103', 'f104', 'f105', 'f106',
                  'f107', 'f108', 'f109', 'f110', 'f111', 'f112', 'f113', 'f114',
                  'f115', 'f116', 'f117', 'f118', 'f119', 'f120', 'f121', 'f122',
                  'f123', 'f124', 'f125', 'f126', 'f127', 'f128']
    writer = csv.DictWriter(f, fieldnames=fieldnames)

    writer.writeheader()

    encodings = []
    for row in df.to_records():
      hash = row[1]
      cpf = row[2]
      encoding = misc.base64_to_numpy(row[3])

      encodings.append({
        'hash': hash,
        'cpf': cpf,
        'f1': encoding[0], 'f2': encoding[1], 'f3': encoding[2], 'f4': encoding[3], 'f5': encoding[4], 'f6': encoding[5], 'f7': encoding[6], 'f8': encoding[7], 'f9': encoding[8], 'f10': encoding[9], 'f11': encoding[10], 'f12': encoding[11], 'f13': encoding[12], 'f14': encoding[13], 'f15': encoding[14], 'f16': encoding[15], 'f17': encoding[16], 'f18': encoding[17], 'f19': encoding[18], 'f20': encoding[19], 'f21': encoding[20], 'f22': encoding[21], 'f23': encoding[22], 'f24': encoding[23], 'f25': encoding[24], 'f26': encoding[25], 'f27': encoding[26], 'f28': encoding[27], 'f29': encoding[28], 'f30': encoding[29], 'f31': encoding[30], 'f32': encoding[31], 'f33': encoding[32], 'f34': encoding[33], 'f35': encoding[34], 'f36': encoding[35], 'f37': encoding[36], 'f38': encoding[37], 'f39': encoding[38], 'f40': encoding[39], 'f41': encoding[40], 'f42': encoding[41], 'f43': encoding[42], 'f44': encoding[43], 'f45': encoding[44], 'f46': encoding[45], 'f47': encoding[46], 'f48': encoding[47], 'f49': encoding[48], 'f50': encoding[49], 'f51': encoding[50], 'f52': encoding[51], 'f53': encoding[52], 'f54': encoding[53], 'f55': encoding[54], 'f56': encoding[55], 'f57': encoding[56], 'f58': encoding[57], 'f59': encoding[58], 'f60': encoding[59], 'f61': encoding[60], 'f62': encoding[61], 'f63': encoding[62], 'f64': encoding[63], 'f65': encoding[64], 'f66': encoding[65], 'f67': encoding[66], 'f68': encoding[67],
        'f69': encoding[68], 'f70': encoding[69], 'f71': encoding[70], 'f72': encoding[71], 'f73': encoding[72], 'f74': encoding[73], 'f75': encoding[74], 'f76': encoding[75], 'f77': encoding[76], 'f78': encoding[77], 'f79': encoding[78], 'f80': encoding[79], 'f81': encoding[80], 'f82': encoding[81], 'f83': encoding[82], 'f84': encoding[83], 'f85': encoding[84], 'f86': encoding[85], 'f87': encoding[86], 'f88': encoding[87], 'f89': encoding[88], 'f90': encoding[89], 'f91': encoding[90], 'f92': encoding[91], 'f93': encoding[92], 'f94': encoding[93], 'f95': encoding[94], 'f96': encoding[95], 'f97': encoding[96], 'f98': encoding[97], 'f99': encoding[98], 'f100': encoding[99], 'f101': encoding[100], 'f102': encoding[101], 'f103': encoding[102], 'f104': encoding[103], 'f105': encoding[104], 'f106': encoding[105], 'f107': encoding[106], 'f108': encoding[107], 'f109': encoding[108], 'f110': encoding[109], 'f111': encoding[110], 'f112': encoding[111], 'f113': encoding[112], 'f114': encoding[113], 'f115': encoding[114], 'f116': encoding[115], 'f117': encoding[116], 'f118': encoding[117], 'f119': encoding[118], 'f120': encoding[119], 'f121': encoding[120], 'f122': encoding[121], 'f123': encoding[122], 'f124': encoding[123], 'f125': encoding[124], 'f126': encoding[125], 'f127': encoding[126], 'f128': encoding[127],
      })

    writer.writerows(encodings)

main('tb_facial_encoding.jitter_1.upsample_False.csv')
main('tb_facial_encoding.jitter_1.upsample_True.csv')
main('tb_facial_encoding.jitter_3.upsample_False.csv')
main('tb_facial_encoding.jitter_3.upsample_True.csv')