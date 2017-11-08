#jshtalenkova, edited
#10/17

#utilities

#parse file into lines
def reader(file):
        f = open(file, "r")
        lines = f.readlines()
        return lines

#parse tab-delimited into list
def parse_t(x):
	y = x.split('\t')
	return y

#convert list into tab-delimited
def join_t(y):
	x = "\t".join(y)
	return x
