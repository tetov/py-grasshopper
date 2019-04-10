__author__ = "tetov"

import Rhino.Geometry as rg
import Rhino.RhinoDoc
from System.Collections.Generic import List

def projectToMesh():
    print("start")
    tolerance = Rhino.RhinoDoc.ActiveDoc.ModelAbsoluteTolerance
    curve_list = List[rg.Curve]()

    outCurves = []
    print len(inCurves)
    for x in inCurves:
        outCurves.append(rg.Curve.ProjectToMesh(x, inMesh, direction, tolerance)[0])
    print(len(outCurves))
    print(type(outCurves))
    print("end")
    outCurves.

    return outCurves
    #outCurves.append(rg.Curve.ProjectToMesh(curveList, meshList, direction, tolerance))

if inCurves is not None or inMesh is not None or not direction.IsValid():
    outCurves = projectToMesh()
    print(outCurves)
