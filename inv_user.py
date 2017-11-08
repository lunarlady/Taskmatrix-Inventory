#jshtalenkova, edited
#10/17

#in--> user-defined (inventory file, bom file, number of builds)
#out--> new inventory file

import in_process as i

print("***************************************************************************************\n")
print("***************************************************************************************\n\n\n")
print("Welcome to your inventory editor, Dima!")
print("Last Update: October 2017\n\n")
print("***************************************************************************************\n\n\n")
inv = raw_input("Inventory file name: ")
bom = raw_input("Build of materials file name: ")
num = raw_input("Number of builds: ")
print("***************************************************************************************\n\n\n")
i.inventory(inv, bom, num)

