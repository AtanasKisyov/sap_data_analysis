import csv
import json
from combinations import create_sfg_collection

# read sfg information from csv extract
active = create_sfg_collection('wires.csv')
collection = {}

# sort sfg's by combinations
for material in active:
    material['combination_key'].sort()
    combination = ''.join(material['combination_key'])
    if combination not in collection:
        collection[combination] = []
    collection[combination].append(material)

# save sfg's to json (avoid future iterations)
with open('circuits.json', 'w') as f:
    json.dump(collection, f, indent=4)

# write results to csv
with open('result.csv', 'w', newline='', encoding='UTF-8') as f:
    writer = csv.writer(f)
    header = ['combination', 'material', 'description', 'length', 'wire', 'left_terminal', 'right_terminal',
              'left_seal', 'right_seal', 'ks_code']
    writer.writerow(header)

    for comb, materials in collection.items():

        for mat in materials:
            row = [comb, mat['number'], mat['description'], mat['length'], mat['left_terminal'], mat['right_terminal'],
                   mat['left_seal'], mat['right_seal'], mat['ks_code']]
            writer.writerow(row)
