def compare_single_wires_materials(obsolete_materials, active_materials):

    for material in obsolete_materials:

        for i in range(len(active_materials)):

            compared_material = active_materials[i]

            if material.material_number == compared_material.material_number:
                continue

            length_difference = material.compare_length(compared_material)
            material_difference = material.compare_components(compared_material)

            if length_difference and len(material_difference) == 0:
                material.close_materials[compared_material] = length_difference

            if length_difference and len(material_difference) == 1:
                material.rework[compared_material] = ''.join(material_difference)


def compare_twisted_wires(obsolete_materials, active_materials, single_wires):

    for obsolete in obsolete_materials:

        obsolete.wires[0] = [x for x in single_wires if x.material_number == obsolete.wires[0]]
        obsolete.wires[1] = [x for x in single_wires if x.material_number == obsolete.wires[1]]

        for active in active_materials:

            active.wires[0] = [x for x in single_wires if x.material_number == active.wires[0]]
            active.wires[1] = [x for x in single_wires if x.material_number == active.wires[1]]

            if obsolete.material_number == active.material_number:
                continue


            length_difference = obsolete.compare_length(active)
            material_difference = obsolete.compare_components(active)

            if length_difference and len(material_difference) == 0:
                obsolete.close_materials[active] = length_difference
