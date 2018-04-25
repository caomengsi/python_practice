#!/usr/bin/env python
# -*- coding: utf-8 -*-
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#皇后问题 https://blog.csdn.net/ap1005834/article/details/50975076
def conflict(state , nextX):
    nextY = len(state)
    for i in range(nextY):
        if abs(state[i] - nextX) in (0 , nextY - i ):
            return True
    return False


def queens(num = 8 , state = ()):
    for pos in range(num):
        if not conflict(state , pos):
            if len(state) == num -1:
                yield (pos,)
            else:
                for result in queens(num , state + (pos,)):
                    yield (pos, ) + result
print len(list(queens(8)))