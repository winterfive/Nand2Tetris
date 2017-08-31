def findValueA(value):
	# Purpose: return 16bit binary value of the arguement
	# Stub: string -> int
	
	# remove @ from string
	value.strip('@')
	
	# remove /n from string
	value.strip()
	
	# check if string is a number or letters using isdigit()
	value.isnumeric()

	# change value to an int
	int(value)

	# find value in binary
	format(value, 'b')

	# change to string
	str(value)

	if value(len) < 16:
		value.zfill(16)
		
	# return value
	return value

# def findValueC():  # TODO
