"""Component for post processing gcode in various ways
    Inputs:
        gcode: gcode for post processing
        remove_dups_bool: Remove duplicate gcode commands (e.g G92 E0 x 2 from Silkworm)
        command: gcode commands to add at specified index
        index: Index for position of insertion
        flow: Flow rates. If more than one value is specified the bounds of the flow values will be printed in the gcode.
        spede: Feed rates. If more than one value is specified the bounds of the values will be printed in the gcode.
    Output:
        out_gcode: Processed gcode
"""

__author__ = "tetov"
__date__ = "20190510"

from os import path
from itertools import groupby
from datetime import datetime
from ghpythonlib import treehelpers as th

# Component setup

ghenv.Component.NickName = 'gcodePostProcessor'

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
        list_w_nums.Flatten()
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
        ";Flow rate (min and max): " + str(bounds(flow)),
        ";Feed rate (min and max): " + str(bounds(speed)),
    ]
    new_gcode = insert_commands(new_gcode, gcode_comments, 0)

    if commands is not None:
        new_gcode = insert_commands(new_gcode, commands, index)

    if remove_dups_bool:
        new_gcode = remove_dups(new_gcode)

    return new_gcode


out_gcode = main()
