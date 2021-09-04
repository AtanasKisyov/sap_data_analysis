def compare_materials(obsolete_materials, active_materials):

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
