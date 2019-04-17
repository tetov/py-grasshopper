"""Offsets curves inwards until offset is no longer valid
    Inputs:
        C: Curves to offset inwards
        D: Offset distance
        S: Simplify curves?
    Output:
        O: Offset curves
"""

__author__ = "tetov"

ghenv.Component.Name = "Offset inwards completely"
ghenv.Component.NickName = 'offsetInwardsCompletely'

import Rhino.RhinoDoc
import Rhino.Geometry as rg

# setup of internal vars
curves = C
step_size = D
simplify_bool = S

tolerance = Rhino.RhinoDoc.ActiveDoc.ModelAbsoluteTolerance
angle_tolerance = Rhino.RhinoDoc.ActiveDoc.ModelAngleToleranceRadians

offset_curves = []

# sanity checks on external inputs
if curves is None: raise ValueError("Missing input curves")
elif not curves.IsClosed: raise ValueError("Curves needs to be closed")
elif not curves.IsPlanar(tolerance): raise ValueError("Curves needs to be planar")

if simplify_bool is None: simplify_bool = True

if step_size is None: raise ValueError("Specify step size")
step_size = abs(step_size) * -1 # take positive input for better UX

# reduces runtime and prevents some bugs
if simplify_bool:
    curves = curves.Simplify(rg.CurveSimplifyOptions.All, tolerance * 100, angle_tolerance)

offset_curves.append(curves.ToNurbsCurve()) # cast curves to NURBS

def offsetInwards(input_curve):
    return input_curve.Offset(rg.Plane.WorldXY, step_size, tolerance, rg.CurveOffsetCornerStyle.Sharp)

while True:
    if offsetInwards(offset_curves[-1]) is not None:
        new_offset = offsetInwards(offset_curves[-1])[0]
    else:
        raise ValueError("Break: None error")

    if rg.AreaMassProperties.Compute(new_offset).Area > rg.AreaMassProperties.Compute(offset_curves[-1]).Area:
        print("Break: New offset's area larger than previous")
        break
    elif rg.Intersect.Intersection.CurveSelf(new_offset, tolerance).Count > 0:
        print("Break: Self intersecting offset")
        break
    elif rg.Intersect.Intersection.CurveCurve(new_offset, offset_curves[-1], tolerance, tolerance).Count > 0:
        print("Break: New offset intersects with previous")
        break
    else:
        offset_curves.append(new_offset)

O = offset_curves
