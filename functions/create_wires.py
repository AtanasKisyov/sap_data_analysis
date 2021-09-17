from classes.wire_types import SingleWire, TwistedWire


def create_single_wires(file):

    with open(file, 'r') as sheet:

        for _ in range(4):
            sheet.__next__()

        columns = [x.strip() for x in sheet.readline().split('|')]
        previous_material_number = ''
        materials = []
        material_index = columns.index("Material")
        description_index = columns.index('Material Number')
        ict_index = columns.index('ICt')
        spare_index = columns.index('Spare')
        component_index = columns.index('Component')
        component_descr_index = columns.index('BOM component')
        sheet.__next__()

        while True:

            current_line = [x.strip() for x in sheet.readline().split('|')]

            if len(current_line) == 1:
                break

            current_material_number = current_line[material_index]
            description = current_line[description_index]
            ict = current_line[ict_index]
            spare = current_line[spare_index]
            component = current_line[component_index]
            component_description = current_line[component_descr_index]

            if current_material_number == 'Material':
                continue

            if ict == 'X':
                continue

            if not previous_material_number == current_material_number:
                current_material = SingleWire(current_material_number, description)
            previous_material_number = current_material_number

            if ict == 'L' and not spare:
                length = current_line[9].strip()
                if len(length) > 3:
                    length = length.replace(' ', '')
                length = int(length)
                current_material.length = length
                current_material.add_wire(component)

            if ict == 'L' and spare == 'L':
                if 'Term' in component_description:
                    current_material.add_left_terminal(component)
                    continue
                current_material.add_left_seal(component)

            if ict == 'L' and spare == 'R':
                if 'Term' in component_description:
                    current_material.add_right_terminal(component)
                    continue
                current_material.add_right_seal(component)

            materials.append(current_material)

    return materials


def create_twisted_wires(file):

    with open(file, 'r') as sheet:

        for _ in range(4):
            sheet.__next__()

        columns = [x.strip() for x in sheet.readline().split('|')]
        previous_material_number = ''
        materials = []
        material_index = columns.index("Material")
        description_index = columns.index('Material Number')
        component_index = columns.index('Component')
        sheet.__next__()

        while True:

            current_line = [x.strip() for x in sheet.readline().split('|')]

            if len(current_line) == 1:
                break

            current_material_number = current_line[material_index]
            description = current_line[description_index]
            component = current_line[component_index]

            if current_material_number == 'Material':
                continue

            if not previous_material_number == current_material_number:
                current_material = TwistedWire(current_material_number, description)
            previous_material_number = current_material_number

            if component.startswith("S"):
                current_material.wires.append(component)
            else:
                current_material.spot_tape = component

            materials.append(current_material)

    return materials
