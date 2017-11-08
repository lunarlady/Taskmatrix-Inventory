#jshtalenkova, edited
#10/17

#in--> file.readlines()
#out--> dictionary: (part number, quantity)


def d_maker(lines):
	d = {'part number' : 'quantity'}
	for i in range(14, len(lines)):
		x = lines[i].split()
		d[x[3]] = x[1]
	return d


#lookup part in build dictionary
#in--> part
#out--> quantity used in build
def part_finder(d, part):
	s = "0"
	if part in d:
        	return d[part]
	else:
		return s		
		

