# -*- coding: utf-8 -*-
"""
Created on Sat Feb  5 11:47:00 2022

@author: DELL
"""
#1
'''
a = int(input())
q = []
def read_each():
    line = input().split(" ")
    s = input()
    return (line, s)

def solve(tup):
    T, s = tup
    N, K = int(T[0]), int(T[1])
    ans = 0
    for i in range(N // 2):
        if s[i] == s[N - i - 1]:
            ans += 1
    return abs(ans - K)

for i in range(a):
    tup = read_each()
    print('Case #{}: {}'.format(i+1,solve(tup)))
'''

#3
'''
import collections
import heapq

num = int(input())
matrix, heap = {}, []
r, c = 0, 0
def read_each():
    line = input().split(" ")
    global r, c, matrix
    r, c = int(line[0]), int(line[1])
    matrix = collections.defaultdict(dict)
    for i in range(r):
        col = input().split(" ")
        matrix[i] = collections.defaultdict(int)
        for j in range(c):
            matrix[i][j] = int(col[j])
            heapq.heappush(heap, [-matrix[i][j], i, j])
    return
dirc = [-1, 0, 1, 0, -1]
def solution():
    visited = [[0 for j in range(c)] for i in range(r)]
    ans = 0
    while heap:
        val, i, j = heapq.heappop(heap)
        for v in range(4):
            x, y = i + dirc[v], j + dirc[v + 1]
            if x >= 0 and x < r and y >= 0 and y < c and visited[x][y] == 0 and matrix[i][j] > matrix[x][y] - 1:
                ans += max(-val - matrix[x][y] - 1, 0)
                matrix[x][y] = max(-val - 1, matrix[x][y])
                visited[x][y] = 1
                heapq.heappush(heap, [-matrix[x][y], x, y])
    return ans

            
        

for i in range(num):
    matrix, maxs = {}, []
    r, c = 0, 0
    read_each()
    print('Case #{}: {}'.format(i+1,solution()))

'''

#4 not passed
import collections
import heapq
count = int(input())
row, col = collections.defaultdict(dict), collections.defaultdict(dict)
#cost = collections.defaultdict(dict)
heap = []
visited = collections.defaultdict(dict)
def read_each():
    num = int(input())
    global visited
    #visited = [[0 for j in range(num)] for i in range(num)]
    for i in range(num):
        line = input().split(" ")
        for j in range(num):
            if line[j] == str(-1):
                row[i][j] = 1
                col[j][i] = 1
        if row.get(i) and len(row.get(i)) <= 1:
            row.pop(i)
        if i == num - 1 and col.get(j) and len(col[j]) <= 1:
            col.pop(j)
    '''
    for j in range(num):
        if col.get(j) and len(col[j]) <= 1:
            col.pop(j)
    '''
    #print(visited)
    for i in range(num):
        line = input().split(" ")
        for j in range(num):
            if line[j] != "0":
                visited[i][j] = 0
                heapq.heappush(heap, (int(line[j]), i, j))
    input()
    input()
    return

def solution():
    def find(x, y):
        if visited[x][y]:
            return
        visited[x][y] = 1
        row[x].pop(y)
        if len(row[x]) == 1:
            newy = list(row[x].keys())[0]
            find(x, newy)
        if len(row[x]) == 0:
            row.pop(x)
        col[y].pop(x)
        if len(col[y]) == 1:
            newx = list(col[y].keys())[0]
            find(newx, y)
        if len(col[y]) == 0:
            col.pop(y)
        return
            
    if len(col) == 0 and len(row) == 0:
        return 0
    '''
    heap = []
    for k, v in row.items():
        for m, n in v.items():
            heapq.heappush(heap, (cost[k][m], k, m))
    '''
    ans = 0
    while heap:
        val, x, y = heapq.heappop(heap)
        if visited[x][y]:
            continue
        find(x, y)
        ans += val
            
    return ans
        
for i in range(count):
    row, col = collections.defaultdict(dict), collections.defaultdict(dict)
    #cost = collections.defaultdict(dict)
    visited = collections.defaultdict(dict)
    read_each()
    print('Case #{}: {}'.format(i+1,solution()))






























    