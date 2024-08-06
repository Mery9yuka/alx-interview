#!/usr/bin/python3
'''Module that return pascal triangle'''


def pascal_triangle(n):
    '''
    Pascal's triangle function
    '''
    List = []
    if n == 0:
        return List
    for k in range(n):
        List.append([])
        List[k].append(1)
        if (k > 0):
            for m in range(1, k):
                lists[k].append(lists[k - 1][m - 1] + lists[k - 1][m])
            lists[k].append(1)
    return List
