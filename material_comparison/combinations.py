# calculate iterations
def get_row_count(file):
    with open(file, 'r') as file:
        return sum(1 for _ in file) - 7


# read sfg information and return collection
def create_sfg_collection(file):
    row_count = get_row_count(file)
    with open(file, 'r') as sheet:

        # skip 'empty' rows
        for _ in range(4):
            sheet.__next__()

        # clear header cells and get needed column indices
        columns = [x.strip() for x in sheet.readline().split('|')]
        previous_material_number = ''
        materials = []
        material_index = columns.index('Material')
        description_index = columns.index('Material Number')
        ict_index = columns.index('ICt')
        spare_index = columns.index('Spare')
        component_index = columns.index('Component')
        component_descr_index = columns.index('BOM component')
        ks_code_index = columns.index('Item Text Line 1')
        unit_index = columns.index('Un')
        sheet.__next__()

        # iterate through the file
        for _ in range(row_count):

            # clear cells for current row
            current_line = [x.strip() for x in sheet.readline().split('|')]

            # read value from needed cells
            current_material_number = current_line[material_index]
            description = current_line[description_index]
            ict = current_line[ict_index]
            spare = current_line[spare_index]
            component = current_line[component_index]
            component_description = current_line[component_descr_index]
            ks_code = current_line[ks_code_index]
            unit = current_line[unit_index]

            if ict == 'X':
                current_material['KS'] = ks_code
                current_material['combination_key'].append(component)
                continue

            if not previous_material_number == current_material_number:
                current_material = {'number': current_material_number,
                                    'description': description,
                                    'combination_key': [],
                                    'left_terminal': '',
                                    'right_terminal': '',
                                    'left_seal': '',
                                    'right_seal': '',
                                    'ks_code': ''}
            previous_material_number = current_material_number

            # logical checks for type of components
            if unit == 'MM':
                length = current_line[9].strip()
                if len(length) > 3:
                    length = length.replace(' ', '')
                length = int(length)
                current_material['length'] = length
                current_material['wire'] = component
                current_material['combination_key'].append(component)

            if ict == 'L' and spare == 'L':
                if 'Term' in component_description:
                    current_material['left_terminal'] = component
                    current_material['combination_key'].append(component)
                    continue
                current_material['left_seal'] = component
                current_material['combination_key'].append(component)
                continue

            if ict == 'L' and spare == 'R':
                if 'Term' in component_description:
                    current_material['right_terminal'] = component
                    current_material['combination_key'].append(component)
                    continue
                current_material['right_seal'] = component
                current_material['combination_key'].append(component)
                continue

            if current_material not in materials:
                materials.append(current_material)

    return materials
