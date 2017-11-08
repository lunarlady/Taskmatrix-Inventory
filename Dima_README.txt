Inventory Editor 
Jane Shtalenkova
October 2017

inv_user.py	::	user interface, prompts for inventory file, bom file, and number of builds	

in_process.py	::	main inventory editor
bom_parse.py	::	bom manipulator
utilities.py	::	file readers, parsers

@USER:

PYTHON PATH SET ON WINDOWS MACHINE
On Windows machine, with Python path C:\Python34 must add path to python.exe
1. Right click <My Computer> and choose <Properties>
2. Go to <Advanced> tab and click <Environment Variables> button 
3. Find variable <PATH> in the top menu and click edit
4. Add the following line to the end of the string
	;C:\Python34
5. Click ok and restart Command Prompt

EXECUTING INVENTORY SCRIPT
1. Go to Inventory directory containing all scripts
2. In Command Prompt type
	python inv_user.py
3. Program will prompt user input for three parameters
	a) Enter include file name (no extension, i.e. InventoryMaster)
	b)Enter bom file name (no extension, i.e. EagleBO)
	c)Enter number of builds
4. New file will be called the same name as original include, followed by date and time generated. It will be generated in the same folder the script is run. 

Enjoy :)


