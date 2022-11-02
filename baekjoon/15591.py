import sys
from collections import deque
import copy
read = sys.stdin.readline

def bfs(UTUBE, min_k, now_node):
    is_visited = [False for i in range(len(UTUBE.keys())+1)]
    is_visited[now_node] = True
    can_go_list = copy.deepcopy(UTUBE[now_node])
    result = set()
    while can_go_list:
        now_node = can_go_list.popleft()
        if now_node[1] >= min_k:
            result.add(now_node)
            is_visited[now_node[0]] = True
            tmp_deque = UTUBE[now_node[0]]
            for tmp_node in tmp_deque:
                if(is_visited[tmp_node[0]] == False):
                    can_go_list.append((tmp_node[0], min(tmp_node[1], now_node[1])))
    return list(result)
if __name__ == '__main__':
    N, Q = map(int, read().split())
    UTUBE = dict()
    for i in range(N-1):
        p,q,r = map(int, read().split())
        if(p in UTUBE):
            tmp_list = UTUBE[p]
            tmp_list.append((q,r))
            UTUBE[p] = tmp_list
        else:
            tmp_list = deque()
            tmp_list.append((q,r))
            UTUBE[p] = tmp_list
        if(q in UTUBE):
            tmp_list = UTUBE[q]
            tmp_list.append((p,r))
            UTUBE[q] = tmp_list
        else:
            tmp_list = deque()
            tmp_list.append((p,r))
            UTUBE[q] = tmp_list
    for i in range(Q):
        k, v = map(int, read().split())
        print(len(bfs(UTUBE,k,v)))