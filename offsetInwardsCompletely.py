"""Provides a scripting component.
    Inputs:
        x: The x script variable
        y: The y script variable
    Output:
        a: The a output variable"""

__author__ = "tetov"
__version__ = "2019.04.16"

import Rhino.Geometry as rg

offset_curves = []

area = min_area + 1.0

area_not_exceeded = True

while area_not_exceeded:

   new_offset = curves.Offset(rg.Plane.WorldXY(), steps, steps/10, rg.CurveOffsetCornerStyle.Sharp())

   area = rg.AreaMassProperties.Compute(new_offset)

   if area > min_area:
      offset_curves.append(new_offset)
   else
      area_not_exceeded = False
