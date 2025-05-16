from collections import deque

def construire_graphe_non_oriente_pondere(edges):
    """Construit un graphe non orienté et pondéré."""
    graph = {}
    for u, v, weight in edges:
        if u not in graph:
            graph[u] = {}
        if v not in graph:
            graph[v] = {}
        graph[u][v] = weight
        graph[v][u] = weight  # Ajout pour l'aspect non orienté
    return graph

def dfs_non_oriente_pondere(graph, start_node):
    """Implémentation DFS pour un graphe non orienté pondéré (ignore les poids pour le parcours)."""
    visited = set()
    stack = [start_node]
    traversal = []
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            traversal.append(node)
            # Ajouter les voisins en ordre inverse
            for neighbor in reversed(graph.get(node, {})):
                if neighbor not in visited:
                    stack.append(neighbor)
    return traversal

def bfs_non_oriente_pondere(graph, start_node):
    """Implémentation BFS pour un graphe non orienté pondéré (ignore les poids pour le parcours)."""
    visited = set()
    queue = deque([start_node])
    visited.add(start_node)
    traversal = []
    while queue:
        node = queue.popleft()
        traversal.append(node)
        for neighbor in graph.get(node, {}):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return traversal

# Exemple de graphe de la Figure 1 avec des poids (non orienté)
edges_non_orientes_ponderees = [('A', 'B', 1), ('C', 'D', 2), ('E', 'F', 3)]
graphe_figure1_non_oriente_pondere = construire_graphe_non_oriente_pondere(edges_non_orientes_ponderees)

start_nodes = ['A', 'C', 'E']

print("\nParcours DFS (graphe non orienté et pondéré):")
for start_node in start_nodes:
    result_dfs = dfs_non_oriente_pondere(graphe_figure1_non_oriente_pondere, start_node)
    print(f"  À partir de {start_node}: {result_dfs}")

print("\nParcours BFS (graphe non orienté et pondéré):")
for start_node in start_nodes:
    result_bfs = bfs_non_oriente_pondere(graphe_figure1_non_oriente_pondere, start_node)
    print(f"  À partir de {start_node}: {result_bfs}")