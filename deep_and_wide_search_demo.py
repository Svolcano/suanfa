from copy import deepcopy
from collections import deque

map = {
    'a':['b', 'c'],
    'b':['c', 'd', 'e'],
    'c':['w'],
    'd':['e'],
    'e':['f'],
    'w':[],
    'f':['eof'],
}


def deep_first_find_route(start, map, route, dog):
    if start == 'f':
        return True
    else:
        for next in map[start]:
            route.append(next)
            status = deep_first_find_route(next, map, deepcopy(route), dog)
            if status:
                if len(route) < dog['len']:
                    dog['len'] = len(route)
                    dog['best'] = route
            else:
                route.pop(-1)
        return False

def wide_first_find_route(map):
    queue = deque()
    stop = 'f'
    start = 'a'
    search = [('', start)]
    queue += [(start, i) for i in map[start]]
    while queue:
        pre, next = queue.popleft()
        print(pre, search)
        if (pre, next) not in search:
            search.append((pre, next))
        if next in search:
            continue
        if next == stop:
            break  
        queue += [(next, i) for i in map[next]]
        
    
    path = [stop]
    print(search)
    while search:
        print(path)
        for i in range(len(search)):
            pre, next = search[i]
            if stop in map[next]:
                path.append(next)
                path.append(pre)
                stop = pre
                break
        search = search[:i]
    print(path)



route = ['a']
wide_first_find_route(map)

