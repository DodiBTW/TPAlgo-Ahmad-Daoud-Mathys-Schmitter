from collections import deque, defaultdict

class UnweightedGraph:
    def __init__(self, graph=None):
        if graph is not None:
            self.graph = graph
        else:
            self.graph = {
                "A": ["B","C"],
                "B": ["A", "D", "E"],
                "C": ["A", "F"],
                "D": ["B"],
                "E": ["B", "F"],
                "F": ["C", "E"]
            }

    def build_layers(self, start="A"):
        visited = set()
        layers = defaultdict(list)
        level = {start: 0}
        queue = deque([start])
        visited.add(start)

        while queue:
            node = queue.popleft()
            curr_level = level[node]
            layers[curr_level].append(node)

            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    level[neighbor] = curr_level + 1
                    queue.append(neighbor)

        return layers, level

    def ascii_graph(self, root="A"):
        layers, levels = self.build_layers(root)
        max_nodes = max(len(nodes) for nodes in layers.values())
        node_width = 1  # Each node is a single character
        gap_size = 3    # Minimum gap between nodes

        max_width = max_nodes * (node_width + gap_size)
        height = (max(layers.keys()) + 1) * 2

        canvas = [[" " for _ in range(max_width)] for _ in range(height)]

        positions = {}
        for lvl, nodes in layers.items():
            y = lvl * 2
            total_nodes = len(nodes)
            # Calculate the starting x to center the nodes
            layer_width = (total_nodes - 1) * (node_width + gap_size)
            start_x = (max_width - layer_width - node_width) // 2
            for i, node in enumerate(nodes):
                x = start_x + i * (node_width + gap_size)
                canvas[y][x] = node
                positions[node] = (x, y)

        drawn = set()

        for node in self.graph:
            x1, y1 = positions[node]
            for neighbor in self.graph[node]:
                edge_key = tuple(sorted([node, neighbor]))
                if edge_key in drawn:
                    continue
                drawn.add(edge_key)
                x2, y2 = positions[neighbor]
                self.draw_line(canvas, x1, y1, x2, y2)

        for row in canvas:
            print("".join(row).rstrip())

    @staticmethod
    def draw_line(canvas, x1, y1, x2, y2):
        dx = x2 - x1
        dy = y2 - y1
        steps = max(abs(dx), abs(dy))
        for i in range(1, steps):
            x = x1 + i * dx // steps
            y = y1 + i * dy // steps
            if canvas[y][x] == " ":
                if dx == 0:
                    canvas[y][x] = "|"
                elif dy == 0:
                    canvas[y][x] = "-"
                elif (dx > 0 and dy > 0) or (dx < 0 and dy < 0):
                    canvas[y][x] = "\\"
                else:
                    canvas[y][x] = "/"

if __name__ == "__main__":
    g = Graph()
    g.ascii_graph()
