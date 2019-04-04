"""Provides a scripting component.
    Inputs:
        curve: input curve
        amplitude: amplitude in sin equation
        curveResolution: TK
        decayBool: decayBool
    Output:
        curve: output curve
"""
__author__ = "tetov"

import math
from clr import StrongBox
from System import Array
import Rhino.Geometry as rg

def decay(z):
    return math.sin(z * z * decayValue)

def main():
    frequency = curveResolution / 4
    #print(frequency)
    points = []

    params = StrongBox[Array[rg.Point3d]]()

    curve.DivideByCount(int(curveResolution), True, params)
    params = list(params.Value)


    for x, y in enumerate(params):
        curvePoint = y
        frame = curve.FrameAt(x)
        zvalue = frame[1].ZAxis
        eq = x / ( len(params)-1 )
        eq *= 2 * math.pi
        eq *= frequency
        #fun
        #eq = math.pow(math.sin(eq), 2.0)

        if decayBool:
             eq *= decay(x)

        eq += phaseShift
        eq = math.sin(eq)
        eq *= amplitude

        if decayBool:
             eq *= decay(x)
             
        points.append(curvePoint + ( zvalue * eq ))
    return points


if amplitude is None: amplitude = 1
if curveResolution is None: curveResolution = 10000
if decayBool is None: decayBool = False
if decayValue is None: decayValue = 1.0
if phaseShift is None: phaseShift = 0.0

outCurve = rg.Curve.CreateInterpolatedCurve(main(), 3)
