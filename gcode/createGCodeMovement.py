"""Creates GCode movement commands to one or more defined points
    Inputs:
        pts: One or more points to interpolate movement inbetween
        speed: Travel speed
        autohome: Autohome all axis before movement?
    Output:
        gcode: Movements
"""

__author__ = "tetov"

import Rhino.Geometry as rg
import Grasshopper.Kernel as gh

w = gh.GH_RuntimeMessageLevel.Warning

ghenv.Component.Name = "Offset inwards completely"
ghenv.Component.NickName = 'offsetInwardsCompletely'


ghenv.Component.Params.Input[1].NickName = "pts"
ghenv.Component.Params.Input[1].Name = "Points"

ghenv.Component.Params.Input[2].NickName = "speed"
ghenv.Component.Params.Input[2].Name = "Travel speed"

ghenv.Component.Params.Input[3].NickName = "autohome"
ghenv.Component.Params.Input[3].Name = "Autohome all axis at start?"


ghenv.Component.Params.Output[1].NickName = "gcode"
ghenv.Component.Params.Output[1].Name = "gcode commands"

gcode = []

def generate_g1(input_pt):
    g1_command = "G1 F%d X%.3f Y%.3f Z%.3f" % (speed, input_pt.X, input_pt.Y, input_pt.Z)
    return g1_command

if not speed: speed = 1500
elif speed[0] <= 0: raise ValueError('Zero or negative speed values not accepted')
else:
    if len(speed) > 1:
        ghenv.Component.AddRuntimeMessage(w, 'Only a single speed value is currently supported.')

    speed = int(speed[0])

if autohome: gcode.append("G28")

for pt in pts:
    pt = rg.Point3d(pt)
    gcode.append(generate_g1(pt))

