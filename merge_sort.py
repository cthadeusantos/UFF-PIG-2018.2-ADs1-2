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
def merge(llist, rlist, ascending=True):
    """
    Merge two lists into an ordered list.
    If ascending == True build a ascending list
    If ascending == False build a descending list
    """
    final = []
    while llist or rlist:
        # This verification is necessary for not try to compare
        # a NoneType with a valid type.
        if len(llist) and len(rlist):
            if llist[0] < rlist[0]:
                final.append(llist.pop(0))
            else:
                final.append(rlist.pop(0))

        # This two conditionals here, is for the case when the two lists
        # have diferent sizes. This save us of an error trying to acess
        # an index out of range.
        if not len(llist):
            if len(rlist):
                final.append(rlist.pop(0))

        if not len(rlist):
            if len(llist):
                final.append(llist.pop(0))
    if ascending == True:
        return final
    else:
        final.reverse()
        return final


def merge_sort(list, ascending=True):
    """
    Sort the list passed by argument with merge.
    """
    if len(list) < 2:
        return list
    mid = int(len(list) / 2)
    return merge(merge_sort(list[:mid]), merge_sort(list[mid:]), ascending)
