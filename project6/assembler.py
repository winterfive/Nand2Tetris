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

x = ''
n = 1

# get name for new file
title = sys.argv[1]

# split name from file type
title = title.split('.')
title = title[0]

# concatenate title with ".hack"
title = title + '.hack'

# create hack file to write to
h = open(title, 'w')

# open file.asm to be translated
with open(sys.argv[1], 'r') as f:
    
    # 1st pass: find and store all symbol values in symbolTable
    for line in f:
        
        # if line is empty or a comment, skip it
        if not line or line.startswith('/'):
            continue
        
        line = cleanLine(line)
        
        if line.startswith('('):
            x = storeSymbol(line, n)
            n += 1
            print(line)
        else:
            print("not a symbol")
            continue
        
    # reset f
    f.seek(0, 0)
    
    # set n to 16 (1st available register is R16)
    n = 16
    
    # 2nd pass: evaluate all lines, find binary values for each
    for line in f:
        
        # remove whitespace and newline char
        line = cleanLine(line)
        
        # if line is empty or a comment
        if not line or line.startswith('/'):
            n += 1
            continue
        
        print(line)
        
        # if line is an A instruction
        if '@' in line:
            x = findValueA(line, n)
            
        # if line is a symbol
        if line.startswith('('):
            x = findSymbol(line)
        
        # if line is a C instruction
        else:
            x = findValueC(line)

        # write x to hack file
        h.write(x + '\n')
        
        n += 1

h.close()
