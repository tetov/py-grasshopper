"""Provides a scripting component.
    Inputs:
        x: The x script variable
        y: The y script variable
    Output:
        a: The a output variable"""

__author__ = "a"
__version__ = "2019.04.02"

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
