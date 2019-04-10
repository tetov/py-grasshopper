"""Provides a scripting component.
    Inputs:
        axisStart:
        axisDirection:
        helixStart:
        pitch:
        turnCount:
        radius1:
        radius2:
    Output:
        a: Output spiral
"""

__author__ = "tetov"

import Rhino.Geometry as rg

if axisStart is None: axisStart = rg.Point3d(0,0,0)
if axisDirection is None: axisDirection = rg.Vector3d(0,0,1)
if helixStart is None: helixStart = rg.Point3d(0,10,10)
if pitch is None: pitch = 5.0
if turnCount is None: turnCount = 10.0
if radius1 is None: radius1 = 5.0
if radius2 is None: radius1 = radius2

radius2 /= 2


a=rg.NurbsCurve.CreateSpiral(axisStart, axisDirection, helixStart, pitch, turnCount, radius1, radius2)
