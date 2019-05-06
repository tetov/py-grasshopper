"""Sorts curves from endpoint to endpoint sequentially and flips curves
    so start is closest to end.
    Inputs:
        crvs: Curves to sort
        start_index: Which curve to start sorting from. Default is 0.
    Outputs:
        sorted_crvs: Curves sorted in order of sequential proximity
        indicies: The original list's indicies sorted in order of sequential
            proximity
"""

__author__ = "tetov"
__date__ = "20190506"

from Rhino import Geometry as rg
from ghpythonlib import components as ghcomp

ghenv.Component.Name = 'Sort curves sequentially'
ghenv.Component.NickName = 'seqSortCurves'
ghenv.Component.Message = __author__ + " " + __date__

ghenv.Component.Params.Input[1].NickName = "crvs"
ghenv.Component.Params.Input[1].Name = "Curves to sort"
ghenv.Component.Params.Input[1].Description = "Curves to sort"

ghenv.Component.Params.Input[2].NickName = "start_index"
ghenv.Component.Params.Input[2].Name = "Index of curve to start sorting from"
ghenv.Component.Params.Input[
    2].Description = "Index of curve to start sorting from"

ghenv.Component.Params.Output[1].NickName = "sorted_crvs"
ghenv.Component.Params.Output[1].Name = "Sorted curves"
ghenv.Component.Params.Output[1].Description = "The sequentially sorted curves"

ghenv.Component.Params.Output[2].NickName = "indices"
ghenv.Component.Params.Output[2].Name = "Indices"
ghenv.Component.Params.Output[
    2].Description = "The parallel sorted list of indices"

if start_index is None:
    start_index = 0


def find_closest_endpoint(search_pt, curve_endpoints):
    """Calculates distances from point to both endpoints for every curve.
        Returns closest point with metadata.
        TODO: Run distance calculations async?
    """
    dist_calc = []
    for crv in curve_endpoints:
        for kind in crv:
            if kind != 'index':
                dist_calc.append({
                    'index': crv['index'],
                    'endpt_kind': kind,
                    'pt_obj': crv[kind],
                    'dist': search_pt.DistanceTo(crv[kind])
                })

    return sorted(dist_calc, key=lambda x: x['dist'])[0]


# start loop
def main(l_crvs, l_start_index):
    """Setup and loop
    """
    l_indices = []
    curve_endpoints = []
    found_pt = {}
    found_pt['index'] = l_start_index

    for i, crv in enumerate(l_crvs):
        curve_endpoints.append({
            'index': i,
            'startpt': crv.PointAtStart,
            'endpt': crv.PointAtEnd
        })
    l_sorted_crvs = [l_crvs[l_start_index]]

    while len(curve_endpoints) > 1:

        # search from end of curve
        search_pt = next((c for c in curve_endpoints
                          if c['index'] == found_pt['index']))['endpt']

        # remove both endpoints on curve from searchlist
        curve_endpoints = [
            c for c in curve_endpoints if not (c['index'] == found_pt['index'])
        ]

        found_pt = (find_closest_endpoint(search_pt, curve_endpoints))

        l_indices.append(found_pt['index'])

        found_curve = l_crvs[found_pt['index']]

        if found_pt['endpt_kind'] == 'endpt':
            # Flip curve
            found_curve, _ = ghcomp.FlipCurve(found_curve)
            # Flip start and end pt in endpt list
            cross_ref = next((i for i, _ in enumerate(curve_endpoints)
                              if _['index'] == found_pt['index']), None)
            curve_endpoints[cross_ref]['startpt'], curve_endpoints[cross_ref][
                'endpt'] = curve_endpoints[cross_ref][
                    'endpt'], curve_endpoints[cross_ref]['startpt']

        l_sorted_crvs.append(found_curve)

    return l_sorted_crvs, l_indices


sorted_crvs, indices = main(crvs, start_index)
