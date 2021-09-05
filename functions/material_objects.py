from classes.material import Material


def material_objects_csv(file):

    with open(file, "r") as sheet:

        for _ in range(5):
            sheet.__next__()

        previous_material_number = ""
        materials = []
        current_line = sheet.readline()

        while True:

            current_line = sheet.readline().split("|")

            if len(current_line) == 1:
                break

            current_material_number, description = current_line[1].strip(), current_line[2].strip()
            ict = current_line[3].strip()
            spare = current_line[4].strip()
            component = current_line[5].strip()
            component_description = current_line[6].strip()

            if current_material_number == "Material":
                continue

            if ict == "X":
                continue

            if not previous_material_number == current_material_number:
                current_material = Material(current_material_number, description)
            previous_material_number = current_material_number

            if ict == "L" and not spare:
                length = current_line[9].strip()
                if len(length) > 3:
                    length = length.replace(" ", "")
                length = int(length)
                current_material.length = length
                current_material.add_wire(component)

            if ict == "L" and spare == "L":
                if "Term" in component_description:
                    current_material.add_left_terminal(component)
                    continue
                current_material.add_left_seal(component)

            if ict == "L" and spare == "R":
                if "Term" in component_description:
                    current_material.add_right_terminal(component)
                    continue
                current_material.add_right_seal(component)

            materials.append(current_material)

    return materials
