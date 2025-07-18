class FordFulkerson:
    def __init__(self, graph: dict):
        self.graph = graph

    def ford_fulkerson(self, source: str, sink: str):
        parent = {vertex: None for vertex in self.graph}
        max_flow = 0

        def bfs(source, sink):
            visited = set()
            queue = [source]
            while queue:
                u = queue.pop(0)
                for v in self.graph[u]:
                    if v not in visited and self.graph[u][v] > 0:
                        queue.append(v)
                        visited.add(v)
                        parent[v] = u
                        if v == sink:
                            return True
            return False

        # On s'assure que pour chaque arête u->v, il existe aussi l'arête v->u
        for u in self.graph:
            for v in self.graph[u]:
                if v not in self.graph:
                    self.graph[v] = {}
                if u not in self.graph[v]:
                    self.graph[v][u] = 0

        while bfs(source, sink):
            path_flow = float('Inf')
            s = sink
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]
            max_flow += path_flow
            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]
        return max_flow