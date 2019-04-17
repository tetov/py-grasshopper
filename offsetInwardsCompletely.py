"""Provides a scripting component.
    Inputs:
        x: The x script variable
        y: The y script variable
    Output:
        a: The a output variable"""

__author__ = "tetov"
__version__ = "2019.04.16"

import Rhino.RhinoDoc
import Rhino.Geometry as rg
from ghpythonlib import components as ghcomp

offset_curves = []
tolerance = Rhino.RhinoDoc.ActiveDoc.ModelAbsoluteTolerance
angle_tolerance = Rhino.RhinoDoc.ActiveDoc.ModelAngleToleranceRadians

i = 0

if simplify_bool:
    curves = curves.Simplify(rg.CurveSimplifyOptions.All, tolerance * 100, angle_tolerance)

def offsetInwards(input_curve):
    return input_curve.Offset(rg.Plane.WorldXY, step_size * -1 * i, tolerance, rg.CurveOffsetCornerStyle.Sharp)

while i < 100:
    i += 1
    if offsetInwards(curves) is not None:
        new_offset = offsetInwards(curves)[0]
    else:
        break
    if rg.Intersect.Intersection.CurveSelf(new_offset, tolerance).Count > 0:
        break
    else:
        intersect_list = list(offset_curves)
        intersect_list.append(new_offset)
        if ghcomp.MultipleCurves(intersect_list)[0] is not None:
            break

    offset_curves.append(new_offset)
