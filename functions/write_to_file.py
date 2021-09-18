import csv


def write_to_file(file_name, close_materials_collection, single_wires=True):
    if single_wires:
        header = ['Material', 'Description', 'Length', 'Wire', 'Left Terminal', 'Right Terminal', 'Left Seal',
                  'Right Seal', 'Material', 'Description', 'Length', 'Wire', 'Left Terminal', 'Right Terminal',
                  'Left Seal', 'Right Seal', 'Length Difference', 'Comment'
                  ]
        with open(file_name, 'w', encoding='UTF8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(header)

            for material in close_materials_collection:
                if material.close_materials:
                    sorted_materials = sorted(material.close_materials.items(), key=lambda x: x[1])
                    for close_material, length_difference in sorted_materials:
                        row = [material.material_number,
                               material.description,
                               material.length,
                               material.components['Wire'],
                               material.components['Left Terminal'],
                               material.components['Right Terminal'],
                               material.components['Left Seal'],
                               material.components['Right Seal'],
                               close_material.material_number,
                               close_material.description,
                               close_material.length,
                               close_material.components['Wire'],
                               close_material.components['Left Terminal'],
                               close_material.components['Right Terminal'],
                               close_material.components['Left Seal'],
                               close_material.components['Right Seal'],
                               length_difference,
                               'Length Difference'
                               ]
                        writer.writerow(row)

            for material in close_materials_collection:
                if material.rework:
                    for rework_material, different_material in material.rework.items():
                        row = [material.material_number,
                               material.description,
                               material.length,
                               material.components['Wire'],
                               material.components['Left Terminal'],
                               material.components['Right Terminal'],
                               material.components['Left Seal'],
                               material.components['Right Seal'],
                               rework_material.material_number,
                               rework_material.description,
                               rework_material.length,
                               rework_material.components['Wire'],
                               rework_material.components['Left Terminal'],
                               rework_material.components['Right Terminal'],
                               rework_material.components['Left Seal'],
                               rework_material.components['Right Seal'],
                               material.compare_length(rework_material),
                               different_material
                               ]
                        writer.writerow(row)
    else:
        header = ['Material', 'Description', 'Material', 'Description', 'Length Difference']

        with open(file_name, 'w', encoding='UTF8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(header)

            for material in close_materials_collection:
                if material.close_materials:
                    sorted_materials = sorted(material.close_materials.items(), key=lambda x: x[1])
                    for close_material, length_difference in sorted_materials:
                        row = [material.material_number,
                               material.description,
                               close_material.material_number,
                               close_material.description,
                               close_material.length,
                               length_difference,
                               ]
                        writer.writerow(row)