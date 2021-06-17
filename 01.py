import os
import fnmatch
import time

path = 'v:/'
pattern = "*result.log"
dirs = os.listdir(path)
with open('out.csv', 'w') as data:
    data.write('Дата;Кол-во\n')

for m in range(1, 7):  # <-- количество месяцев +1
    res = {}
    res_m = set()
    for dr in dirs:
        if '2021_' + str(m).zfill(2) in dr:
            res[dr] = set()
            print('______{}______'.format(dr))
            for name in os.listdir(path + '/' + dr):
                din = name.replace('#', '_').split('_')[1]
                res[dr].add(din)
                res_m.add(din)
    with open('out.csv', 'a') as data:
        for key, val in res.items():
            data.write(key + ';' + str(len(val)) + '\n')
        data.write(str(m).zfill(2) + ';' + str(len(res_m)) + '\n')