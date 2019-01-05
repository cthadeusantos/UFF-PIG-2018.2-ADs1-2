#!/usr/bin/env python
# codding: UTF-8
#
## @package Ranking Class
#
#  @brief This class generate a ranking from inputs
#  @note calculate footrule and kemeny distance
#  @author Carlos Thadeu Santos - ID: 17113050228
#  @date 31-Aug-2018
#  @version 0.0.1 alpha
#

def binarySearch(alist, item):
    first = 0
    last = len(alist)-1
    found = False

    while first<=last and not found:
        midpoint = (first + last)//2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint-1
            else:
                first = midpoint+1
    return midpoint
