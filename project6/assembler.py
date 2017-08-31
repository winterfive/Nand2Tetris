# Author: Lee Gainer
# Date: Aug 2017
# Course: NandtoTetris, final project
# Function: Translate any .asm file to binary (.hack)

#!/usr/bin/python

import sys
from helpers import *

# create empty symbol table, dict
# add pre-defined symbols

# 1st Pass - scan program
# 		   - add labels and their values to table

# 2nd Pass - scan program for each instruction
#		   - find binary value for each instruction and place in output file

# create dict symbolTable
symbolTable = {'SP': 0, 'R0': 0, 'LCL': 1, 'R1': 1, 'ARG': 2, 'R2': 2,
	'THIS': 3, 'R3': 3, 'THAT': 4, 'R4': 4, 'R5': 5, 'R6': 6, 'R7': 7,
	'R8': 8, 'R9': 9, 'R10': 10, 'R11': 11, 'R12': 12, 'R13': 13,
	'R14': 14, 'R15': 15, 'SCREEN': 16384, 'KBD': 24576}
	
x = ''

# get name for new file
title = sys.argv[1][0:3]

# concatenate title with ".hack"
title = title + '.hack'

# create hack file to write to
h = open(title, 'w')

# open file.asm to be translated
with open(sys.argv[1], 'r') as f:
    for line in f:
    	
    	# if line is a comment
    	if '//' in line:
    		continue
    	
    	# if line begins with a space
    	if not line:
    		continue
    	
    	# if line is an A instruction
    	if '@' in line:
    		x = findValueA(line)
		
    	# if line is a C instruction
    	# if 'A' or 'D' or 'M' in line:
    		# x = findValueC()

    	# write x to hack file
    	h.write(x)
    	h.write('\n')

h.close()
