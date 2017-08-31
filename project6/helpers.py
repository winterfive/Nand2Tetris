def findValueA(value):
	# Purpose: return 16bit binary value of the arguement
	# Stub: string -> string
	
	# remove @ from string
	newValue = value.strip('@\n')
	
	# change value to an int
	newValue = int(newValue)

	# find value in binary
	newValue = format(newValue, 'b')

	# if newValue(len) < 16:
	newValue = newValue.zfill(16)
		
	# return value
	return newValue

# def findValueC(): TODO
