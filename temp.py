import re

dins = {
    'BUD': '107',
    'BUDP': '123',
    'BUHL': '108',
    'JURP': '121',
    'KRF': '57',
    'LAW': '1',
    'MBP': '110',
    'RGN': '16',
    'SBOB': '143',
    'SBOO': '139',
    'SBOP': '135',
    'SKBB': '140',
    'SKBEM': '144',
    'SKBO': '136',
    'SKJB': '141',
    'SKJEM': '145',
    'SKJO': '137',
    'SKJP': '133',
    'SKS': '168',
    'SKUO': '138',
    'SKZO': '154',
    'SPK-I': '148',
    'SPK-II': '149',
    'SPK-III': '150',
    'SPK-IV': '151',
    'SPK-V': '152',
}

with open('temp.txt') as file:
    data = file.readlines()
with open('out.csv', 'w', encoding='utf-8') as file:
    file.write('kit,subhost\n')
    for line in data:
        x = re.findall('[A-Z-]*', line)[0]
        # print(x)
        y = re.findall('[^A-Z-]*', line.strip())[-2]
        if '_02' in y:
            y = y.split('_')[0] + '_2'
        # print(y)
        file.write(dins[x] + '_' + str(y).lstrip('0') + ',"ООО ""Консультант-Навигатор"""\n')