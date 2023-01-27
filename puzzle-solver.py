import sys
from utils import show
from collections import defaultdict, deque

monitor = False

def input_single(dtype=int):
    return dtype(sys.stdin.readline().strip())

def input_list(dtype=int):
    return [dtype(i) for i in sys.stdin.readline().strip().split()]

print("Initial State")
B = "".join(["".join(input_list(str)) for _ in range(3)])
print("Target State")
A = "".join(["".join(input_list(str)) for _ in range(3)])
INF = 10 ** 8

def neighbor(B):
    BX = B.index('0')
    xi, xj = BX // 3, BX % 3
    N = []

    def swap(S, x, y):
        lst = list(S)
        lst[x], lst[y] = lst[y], lst[x]
        return ''.join(lst)

    if xi > 0:
        NX = 3*(xi-1)+xj
        N.append((swap(B, BX, NX), NX))
    if xj > 0:
        NX = 3*(xi)+xj-1
        N.append((swap(B, BX, NX), NX))
    if xi < 2:
        NX = 3*(xi+1)+xj
        N.append((swap(B, BX, NX), NX))
    if xj < 2:
        NX = 3*(xi)+xj+1
        N.append((swap(B, BX, NX), NX))

    return N

def show_puzzle(B, *args, **kwargs):
    board = [
        [B[3*i + j] for j in range(3)]
        for i in range(3)
    ]
    show(board, *args, **kwargs)

def BFS(B, A):
    V = defaultdict(lambda: INF)
    Q = deque([(B, '')])

    while Q:
        _B, D = Q.popleft()
        if _B == A:
            print(D)
            return
        
        for N, s in neighbor(_B):
            if V[N] > len(D) + 1:
                V[N] = len(D) + 1
                Q.append((N, D+str(s+1)))

    print(-1)

BFS(B, A)