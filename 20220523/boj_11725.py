import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(1000000)
N = int(input())
result = [0] * (N + 1)
visited = [False] * (N + 1)
graph = [[] for _ in range(N + 1)]
for i in range(N - 1):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)


def dfs(graph, value, visited):
    visited[value] = True
    for i in graph[value]:
        if not visited[i]:
            result[i] = value
            dfs(graph, i, visited)


dfs(graph, 1, visited)
for i in range(2, N + 1):
    print(result[i])