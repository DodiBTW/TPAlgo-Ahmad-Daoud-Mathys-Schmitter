class DFS:
    def __init__(self, graph):
        self.graph = graph

    def dfs(self, current, visited=None, order=None):
        """
            ATTENTIONNN : LA VARIABLE ORDER A  ÉTÉ AJOUTÉE CAR LA STRUCTURE DE DONNÉES SET NE PRESERVE PAS L'ORDRE D'INSERTION.
        """
        if visited is None:
            visited = set()
        if order is None:
            order = []
        if current in visited:
            return order
        visited.add(current)
        order.append(current)
        for neighbor in self.graph.get(current, []):
            self.dfs(neighbor, visited, order)
        return order