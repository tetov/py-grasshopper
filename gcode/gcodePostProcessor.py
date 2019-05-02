"""Component for post processing gcode in various ways
    Inputs:
        gcode: gcode for post processing
        remove_dups_bool: Remove duplicate gcode commands (e.g G92 E0 x 2 from Silkworm)
        command: gcode commands to insert
        index: Index for position of insertion
    Output:
        out_gcode: Processed gcode
"""

__author__ = "tetov"
__date__ = "20190502"

from os import path
from itertools import groupby
from datetime import datetime
from ghpythonlib import treehelpers as th

# Component setup

ghenv.Component.Name = "gcode Post Processor"
ghenv.Component.NickName = 'gcodePostProcessor'
ghenv.Component.Message = __author__ + " " + __date__

ghenv.Component.Params.Input[1].NickName = "gcode"
ghenv.Component.Params.Input[1].Name = "GCode to be processed."

ghenv.Component.Params.Input[2].NickName = "remove_dups_bool"
ghenv.Component.Params.Input[2].Name = "Remove duplicate commands?"

ghenv.Component.Params.Input[3].NickName = "commands"
ghenv.Component.Params.Input[3].Name = "Command to add at index."

ghenv.Component.Params.Input[4].NickName = "index"
ghenv.Component.Params.Input[4].Name = "Index to insert command"

ghenv.Component.Params.Input[5].NickName = "flow"
ghenv.Component.Params.Input[5].Name = "Flowrate"

ghenv.Component.Params.Input[6].NickName = "speed"
ghenv.Component.Params.Input[6].Name = "Feedrate"

ghenv.Component.Params.Output[1].NickName = "out_gcode"
ghenv.Component.Params.Output[1].Name = "Processed gcode"

if index is None:
    index = 0

def insert_commands(gcode, new_commands, index):
    gcode[index:index] = new_commands
    return gcode


def remove_dups(input):
    output = []
    for (key, _) in groupby(input):
        output.append(key)
    return output


def bounds(list_w_nums):

    if not list_w_nums.DataCount:
        return "None specified"
    else:
        list_w_nums = th.tree_to_list(list_w_nums)

    if len(list_w_nums) > 1:
        return min(list_w_nums), max(list_w_nums)
    else:
        return list_w_nums[0]


def main():

    new_gcode = gcode

    gcode_comments = [
        ";Filename: " + path.basename(ghdoc.Path),
        ";Created: " + str(datetime.now()),
        ";Flow rate: " + str(bounds(flow)),
        ";Feed rate: " + str(bounds(speed)),
    ]
    new_gcode = insert_commands(new_gcode, gcode_comments, 0)

    if commands is not None:
        new_gcode = insert_commands(new_gcode, commands, index)

    if remove_dups_bool:
        new_gcode = remove_dups(new_gcode)

    return new_gcode


out_gcode = main()
