# create dict symbolTable
symbolTable = {'SP': '0', 'R0': '0', 'LCL': '1', 'R1': '1', 'ARG': '2', 'R2': '2',
	'THIS': '3', 'R3': '3', 'THAT': '4', 'R4': '4', 'R5': '5', 'R6': '6', 'R7': '7',
	'R8': '8', 'R9': '9', 'R10': '10', 'R11': '11', 'R12': '12', 'R13': '13',
	'R14': '14', 'R15': '15', 'SCREEN': '16384', 'KBD': '24576'}
	
destTable = {'null': '000', 'M': '001', 'D': '010', 'MD': '011', 'A': '100',
	'AM': '101', 'AD': '110', 'AMD': '111'}
	
compTable = {'0': '101010', '1': '111111', '-1': '111010', 'D': '001100', 'A': '110000',
	'!D': '001101', '!A': '110001', '-D': '001111', '-A': '110011', 'D+1': '011111',
	'A+1': '110111', 'D+1': '001110', 'A-1': '110010', 'D+A': '000010', 'D-A': '010011',
	'A-D': '000111', 'D&A': '000000', 'D|A': '010101', 'M': '110000', '!M': '110001',
	'-M': '110011', 'M+1': '110111', 'M-1': '110010', 'D+M': '000010', 'D-M': '010011',
	'M-D': '000111', 'D&M': '000000', 'D|M': '010101'}
	
jumpTable = {'null': '000', 'JGT': '001', 'JEQ': '010', 'JGE': '011', 'JLT': '100',
	'JNE': '101', 'JLE': '110', 'JMP': '111'}
		
def findValueA(value):
	# A instruction
	# Purpose: return 16bit binary value of the arguement
	# Stub: string -> string

	# remove @ from string
	value = value.strip('@')

	# change value to an int
	value = int(value)

	# find value in binary
	value = format(value, 'b')

	# if value(len) < 16:
	value = value.zfill(16)

	# return value
	return value

def findValueC(value):
	# C Instruction or Jump
	# Purpose: return 16bit binary value of the arguement
	# Stub: string -> string
	
	# if value is a jump
	if ';' in value and '=' not in value:
		# parse the comp and dest data
		value = value.split(';')
		comp = value[0]
		jump = value[1]
		
		# find value of a
		a = findAValue(comp)
		
		# find values for comp, jump, dest
		comp = compTable[comp]
		jump = jumpTable[jump]
		dest = '000'
		
	# value isn't a jump
	else:
		# parse the dest, comp, and jump data
		value = value.split('=')
		dest = value[0]
		comp = value[1]
		
		# split comp into comp and jump
		comp = comp.split(';')
		comp = comp[0]
		jump = 'null'	# Remove later
		# jump = comp[1]	# Use with more complicated files
		
		# find values for each
		dest = destTable[dest]
		comp = compTable[comp]
		jump = jumpTable[jump]
	
	# concatenate parts and store value
	value = ('111' + a + comp + dest + jump)
	
	# return value
	return value
	
def findAValue(comp):
	# A Value in a C Instruction
	# Purpose: Find 1bit value for a
	#Stub: string -> string
	
	# find value for a
	if 'M' in comp:
		a = '1'
	else:
		a = '0'
		
	return  a
