# Project for comparing obsolete or excessive wires with active wires on the shop floor

Python 3.9.5 (No external libraries)

SAP requirements: PP BOM Evaluation table (tcode YQ298 or similar).

Current version works with single circuit wires and twisted wires.

Use:

Export the information from SAP in unconverted csv named 'wires.csv' 

All your materials will be sorted by a 'combination key' which is a concatenated string of all used components
for the current material.

Update: 

Cut Big O complexity which with all materials loaded from shop floor hit 81 000 000 iterations.

Now its just one and all result are saved in a json file for quick future updates and analysis.

