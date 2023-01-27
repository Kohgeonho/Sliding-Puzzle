import sys
from collections import defaultdict, deque

def input_single(dtype=int):
    return dtype(sys.stdin.readline().strip())

def input_list(dtype=int):
    return [dtype(i) for i in sys.stdin.readline().strip().split()]

B = "".join(["".join(input_list(str)) for _ in range(3)])
A = "123456780"
INF = 10 ** 8

def neighbor(B):
    BX = B.index('0')
    xi, xj = BX // 3, BX % 3
    N = []

    def swap(S, _i, _j):
        y = S[3*_i+_j]
        return S.replace('0', 't').replace(y, '0').replace('t', y)

    if xi > 0:
        N.append(swap(B, xi-1, xj))
    if xj > 0:
        N.append(swap(B, xi, xj-1))
    if xi < 2:
        N.append(swap(B, xi+1, xj))
    if xj < 2:
        N.append(swap(B, xi, xj+1))

    return N

def BFS(B, A):
    V = defaultdict(lambda: INF)
    Q = deque([(B, 0)])

    while Q:
        _B, D = Q.popleft()
        # print(_B, D)
        if _B == A:
            print(D)
            return
        
        for N in neighbor(_B):
            if V[N] > D + 1:
                V[N] = D + 1
                Q.append((N, D+1))

    print(-1)

BFS(B, A)