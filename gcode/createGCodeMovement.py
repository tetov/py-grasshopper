"""Creates GCode movement commands to one or more defined points
    Inputs:
        pts: One or more points to interpolate movement inbetween
        speed: Travel speed
        autohome: Autohome all axis before movement?
    Output:
        gcode: Movements
"""

__author__ = "tetov"
__date__ = "20190430"

import Rhino.Geometry as rg
import Grasshopper.Kernel as gh

w = gh.GH_RuntimeMessageLevel.Warning

ghenv.Component.Name = 'createGcodeMovement'
ghenv.Component.NickName = 'gMovement'
ghenv.Component.Message = __author__ + " " + __date__

ghenv.Component.Params.Input[1].NickName = "pts"
ghenv.Component.Params.Input[1].Name = "Points"

ghenv.Component.Params.Input[2].NickName = "speed"
ghenv.Component.Params.Input[2].Name = "Travel speed"

ghenv.Component.Params.Input[3].NickName = "autohome"
ghenv.Component.Params.Input[3].Name = "Autohome all axis at start?"

ghenv.Component.Params.Output[1].NickName = "gcode"
ghenv.Component.Params.Output[1].Name = "gcode commands"

if not speed:
    speed = 1500
elif speed[0] <= 0:
    raise ValueError('Zero or negative speed values not accepted')
else:
    if len(speed) > 1:
        ghenv.Component.AddRuntimeMessage(
            w, 'Only a single speed value is currently supported.')

    speed = int(speed[0])


def generate_g1(input_pt):
    g1_command = "G1 F%d X%.3f Y%.3f Z%.3f" % (speed, input_pt.X, input_pt.Y,
                                               input_pt.Z)
    return g1_command


def main():
    commands = []

    if autohome:
        commands.append("G28")

    for pt in pts:
        pt = rg.Point3d(pt)
        commands.append(generate_g1(pt))

    return commands


gcode = main()
