import time
from functions.material_objects import material_objects_csv
from functions.compare_materials import compare_materials
from functions.write_to_file import write_to_file

start = time.time()

print("File opened...")

obsolete_materials = material_objects_csv("Files/obsolete.csv")

print("Obsolete material objects created...")

active_materials = material_objects_csv("Files/active.csv")

print("Active material objects created...")

compare_materials(obsolete_materials, active_materials)

print("Materials are compared. Starting to write results into file...")

write_to_file("Files/Analysis.csv", obsolete_materials)

print("Workbook saved and closed!")

end = time.time()

difference = end - start

print(f"Analysis finished in {difference:.2f} seconds")
