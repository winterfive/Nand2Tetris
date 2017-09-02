# create dict symbolTable
symbolTable = {'SP': 0, 'R0': 0, 'LCL': 1, 'R1': 1, 'ARG': 2, 'R2': 2,
	'THIS': 3, 'R3': 3, 'THAT': 4, 'R4': 4, 'R5': 5, 'R6': 6, 'R7': 7,
	'R8': 8, 'R9': 9, 'R10': 10, 'R11': 11, 'R12': 12, 'R13': 13,
	'R14': 14, 'R15': 15, 'SCREEN': 16384, 'KBD': 24576}
	
def findValueA(value):
	# A instruction
	# Purpose: return 16bit binary value of the arguement
	# Stub: string -> int
	
	# remove @ from string
	value = value.strip('@\n')
	
	# change value to an int
	value = int(value)

	# find value in binary
	value = format(value, 'b')

	# if value(len) < 16:
	value = value.zfill(16)
		
	# return value
	return value

def findValueC(value):
	# C Instruction
	# Purpose: return 16bit binary value of the arguement
	# Stub: string -> int
	
	# parse the dest, comp, and jump pieces  TODO
	# find values for each
	# concatenate parts and store value
	# return value
	
	return value
	
