class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = {i: [] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = [False] * n
        def dfs(node):
            if node == destination:
                return True
            visited[node] = True
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    if dfs(neighbor):
                        return True
            return False
        return dfs(source)
