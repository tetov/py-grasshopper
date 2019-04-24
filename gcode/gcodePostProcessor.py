"""Component for post processing gcode in various ways
    Inputs:
        gcode: gcode for post processing
        command: gcode commands to insert
        index: Index for position of insertion 
    Output:
        out_gcode: Processed gcode
"""

__author__ = "tetov"

from itertools import groupby

ghenv.Component.Params.Input[1].NickName = "gcode"
ghenv.Component.Params.Input[1].Name = "GCode to be processed."

ghenv.Component.Params.Input[2].NickName = "command"
ghenv.Component.Params.Input[2].Name = "Command to add at index."

ghenv.Component.Params.Input[3].NickName = "index"
ghenv.Component.Params.Input[3].Name = "Index to insert command"

ghenv.Component.Params.Output[1].NickName = "out_gcode"
ghenv.Component.Params.Output[1].Name = "Processed gcode"

out_gcode = []

def insert_command(input):
    out_gcode[index:index] = input

# remove duplicate lines
for (key,_) in groupby(gcode):
    out_gcode.append(key)

if index is None: index = 0
if command is not None: insert_command(command)
