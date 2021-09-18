# Project for comparing obsolete or excessive wires with active wires on the shop floor

Python 3.9.5 (No external libraries)

SAP requirements: PP BOM Evaluation table (tcode YQ298 or similar).

Current version works with single circuit wires and twisted wires.

Use:

Single Wires:

Export the information from SAP for your obsolete and active wires in separate files.
Be sure to name them "obsolete_wires.csv" and "active_wires.csv".

Twisted Wires:

Export the information for your obsolete and active twisted wires in separate files.
There should be a third file which must contain the information for all circuit wires in your system.
Be sure to name them "obsolete_wires.csv", "active_wires.csv" and "lower_wires.csv"

Run the "main.py" file the console. You will be asked what type of analysis you need.
Choose between "single wires" and "twisted wires"
