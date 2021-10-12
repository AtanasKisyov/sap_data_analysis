import time
from functions.create_wires import create_single_wires
from functions.compare_materials import compare_single_wires_materials
from functions.write_to_file import write_to_file


def single_wire_comparison():
    obsolete_materials = create_single_wires("Files/obsolete_wires.csv")

    active_materials = create_single_wires("Files/active_wires.csv")

    compare_single_wires_materials(obsolete_materials, active_materials)

    write_to_file("Files/Analysis.csv", obsolete_materials)


if __name__ == '__main__':
    start = time.time()
    single_wire_comparison()
    end = time.time()
    print(f'{end - start:.2f}')
