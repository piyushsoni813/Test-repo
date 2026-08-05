from typing import List

class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(n)]
        for u, v in invocations:
            graph[u].append(v)
        visited = [False] * n
        stack = [k]
        while stack:
            u = stack.pop()
            if visited[u]:
                continue
            visited[u] = True
            for v in graph[u]:
                if not visited[v]:
                    stack.append(v)
        for u, v in invocations:
            if not visited[u] and visited[v]:
                return list(range(n))
        return [u for u in range(n) if not visited[u]]