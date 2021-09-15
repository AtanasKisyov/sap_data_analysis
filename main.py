import time
from functions.create_wires import create_single_wires
from functions.compare_materials import compare_materials
from functions.write_to_file import write_to_file

start = time.time()

print("File opened...")

obsolete_materials = create_single_wires("Files/obsolete_wires.csv")

print("Obsolete material objects created...")

active_materials = create_single_wires("Files/active_wires.csv")

print("Active material objects created...")

compare_materials(obsolete_materials, active_materials)

print("Materials are compared. Starting to write results into file...")

write_to_file("Files/Analysis.csv", obsolete_materials)

print("Workbook saved and closed!")

end = time.time()

difference = end - start

print(f"Analysis finished in {difference:.2f} seconds")
