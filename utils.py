import sys
from time import sleep

sys.setrecursionlimit(10**8)

def str_color(s, color="yellow"):
    if color == "red":
        return f"\033[31m{s}\033[0m"
    elif color == "green":
        return f"\033[32m{s}\033[0m"
    elif color == "yellow":
        return f"\033[33m{s}\033[0m"
    elif color == "blue":
        return f"\033[34m{s}\033[0m"
    elif color == "magenta":
        return f"\033[35m{s}\033[0m"
    elif color == "cyan":
        return f"\033[36m{s}\033[0m"

ARROW = ["\u2190", "\u2191", "\u2192", "\u2193", "\u2196", "\u2197", "\u2198", "\u2199"]
def show(board, t=1, opt="", vemph=[0], idxemph=[], axis=None):
    string = opt + "\n"
    N = len(board)
    M = len(board[0])

    if axis:
        Iaxis, Jaxis = axis
        board = [["   "] + [x for x in Jaxis]] + [[y] + board[i] for i, y in enumerate(Iaxis)]
        N, M = N+1, M+1

    for i in range(N):
        for j in range(M):
            if board[i][j] == vemph:
                string += str_color(f"{board[i][j]:2} ")
            elif (i, j) in idxemph:
                string += str_color(f"{board[i][j]:2} ")
            elif board[i][j] == -1:
                string += ".  "
            else:
                string += f"{board[i][j]:2} "
        string += "\n"
    string += "\n"
    print(string)
    sleep(t)

def binary_search(arr, x):
    left, right = 0, len(arr) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] <= x:
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    return result
