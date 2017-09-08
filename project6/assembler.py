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

# Variables
x = ''
n = 0

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
        
        # remove whitespace and inline comments
        line = cleanLine(line)
        
        # if line is empty 
        if not line:
            continue
        
        # if line isn't empty
        else:
            
            # if line is a label
            if line.startswith('('):
                
                # store label values in symbolDict
                x = storeLabel(line, n)
                
            else:
                n += 1
        
    # reset n
    n = 16
    
    # reset f
    f.seek(0)
    
    # 2nd pass: evaluate all lines, find binary values for each
    for line in f:
        
        # remove whitespace and newline
        line = cleanLine(line)
        
        # if line is empty, a comment, or a label declaration
        if not line \
        or line.startswith('/') \
        or line.startswith('('):
            continue
        
        # if line is an A instruction
        if line.startswith('@'):
            x = findValueA(line, n)
        
        # if line is a C instruction
        else:
            x = findValueC(line)

        # write x to hack file
        h.write(x + '\n')

h.close()
