from functions.create_wires import create_single_wires, create_twisted_wires
from functions.compare_materials import compare_single_wires_materials, compare_twisted_wires
from functions.write_to_file import write_to_file


def single_wire_comparison():
    obsolete_materials = create_single_wires("Files/obsolete_wires.csv")

    active_materials = create_single_wires("Files/active_wires.csv")

    compare_single_wires_materials(obsolete_materials, active_materials)

    write_to_file("Files/Analysis.csv", obsolete_materials)


def twisted_wire_comparison():

    single_wires = create_single_wires("Files/lower_wires.csv")

    obsolete_materials = create_twisted_wires("Files/obsolete_wires.csv")

    active_materials = create_twisted_wires("Files/active_wires.csv")

    compare_twisted_wires(obsolete_materials, active_materials, single_wires)

    write_to_file('Files/Analysis.csv', obsolete_materials, False)


if __name__ == '__main__':
    function_mapper = {'single wires': single_wire_comparison, 'twisted wires': twisted_wire_comparison}
    choice = input('What types of wires will be compared?\n')
    function_mapper[choice]()
