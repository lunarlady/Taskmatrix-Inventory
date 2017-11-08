#jshtalenkova, edited
#10/17

#in--> inventory, bom, number of builds
#out--> new inventory

import bom_parser as b
import utilities as u
import time as t
 

def inventory(in_file, bom_file, n):
	#complete message and bom name strings
	s = "Your inventory has been updated..."
	s_bom = bom_file.partition(".")[0]

	#create new file
	name = "InventoryMaster" + t.strftime("%m_%d_%Y") + ".txt"
	out_file = open(name, "w")	

	#create (item, quantity) dictionary from bom file
	bom_lines = u.reader(bom_file)
	d_bom = b.d_maker(bom_lines)

	#extract bom title

	#read inv master
	inv = u.reader(in_file)
		
	#edit inv lines and write to new file
	for i in range(0, 899):
		#print("*******LINE " + str(i))
		#parse line
		x = u.parse_t(inv[i])
		
		#edit line
        	#erase old 
        	del x[49] 
        	#change header 
        	if i == 0: 
                	x[51] = s_bom + "_" + n   
                	x.append( t.strftime("B%y%m%d_%H%M") )     
        	#change other lines  
        	else: 
			#find part in bom and write quantity
                	part = x[0][1:-1] 
                	q_part = b.part_finder(d_bom, part)
			x[51] = q_part

			#subtract from inventory
			#if quantity missing, set to zero
			if x[50] == "":
				x[50] = "0"

			#if deficit, print alert and append same
			elif x[50][0] == "(":
				if part in d_bom: 
					print("You do not have enough {0} to build".format(part))
				x.append(x[50])
			else:
				x.append( str(int(x[50]) - int(q_part)*int(n)) )

		#join line
		y = u.join_t(x)
		
		#write to new inv file
		out_file.write(y + "\n")
	return s 
