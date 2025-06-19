from utils.fmt_print import FmtPrint
from Exercice1.dfs import DFS
from Exercice1.bfs import BFS
from Exercice2.dijkstra import Dijkstra
from Exercice3.bellman_ford import BellmanFord

class TestGraphs:
    def __init__ (self, format_print: FmtPrint, unweighted_graph_to_use: dict, weighted_graph_to_use: dict, negative_weighted_graph_to_use: dict, negative_weighted_graph_with_negative_cycle: dict):
        self.unweighted_graph_to_use = unweighted_graph_to_use
        self.weighted_graph_to_use = weighted_graph_to_use
        self.negative_weighted_graph_to_use = negative_weighted_graph_to_use
        self.negative_weighted_graph_with_negative_cycle = negative_weighted_graph_with_negative_cycle
        self.format_print = format_print


    def test_bfs(self):
        bfs_manager = BFS(self.unweighted_graph_to_use)
        noeud = None
        while noeud not in self.unweighted_graph_to_use:
            self.format_print.clear_console()
            self.format_print.log("Veuillez entrer le noeud de départ pour l'algorithme BFS :", open=True, close=True)
            noeud = input("Noeud de départ : ")
        graph = bfs_manager.bfs(noeud)
        self.format_print.clear_console()
        self.format_print.log(f"Résultat de l'algorithme BFS à partir du noeud {noeud} :", open=True)
        self.format_print.log(str(graph), close=True)

    def test_dfs(self):
        dfs_manager = DFS(self.unweighted_graph_to_use)
        noeud = None
        while noeud not in self.unweighted_graph_to_use:
            self.format_print.clear_console()
            self.format_print.log("Veuillez entrer le noeud de départ pour l'algorithme DFS :", open=True, close=True)
            noeud = input("Noeud de départ : ")
        graph = dfs_manager.dfs(noeud)
        self.format_print.log(f"Résultat de l'algorithme DFS à partir du noeud {noeud} :", open=True)
        self.format_print.clear_console()
        self.format_print.log(str(graph), close=True)

    def test_dijkstra(self):
        dijkstra_manager = Dijkstra(self.weighted_graph_to_use)
        noeud = None
        while noeud not in self.weighted_graph_to_use:
            self.format_print.clear_console()
            self.format_print.log("Veuillez entrer le noeud de départ pour l'algorithme Dijkstra :", open=True, close=True)
            noeud = input("Noeud de départ : ")
        graph = dijkstra_manager.dijkstra(noeud)
        self.format_print.clear_console()
        self.format_print.log(f"Résultat de l'algorithme Dijkstra à partir du noeud {noeud} :", open=True)
        self.format_print.log(str(graph), close=True)
    def test_bellman_ford(self):
        bellman_ford_manager = BellmanFord(self.negative_weighted_graph_to_use)
        noeud = None
        while noeud not in self.negative_weighted_graph_to_use:
            self.format_print.clear_console()
            self.format_print.log("Veuillez entrer le noeud de départ pour l'algorithme Bellman-Ford :", open=True, close=True)
            noeud = input("Noeud de départ : ")
        graph = bellman_ford_manager.bellman_ford(noeud)
        self.format_print.clear_console()
        self.format_print.log(f"Résultat de l'algorithme Bellman-Ford à partir du noeud {noeud} :", open=True)
        self.format_print.log(str(graph), close=True)
    def test_bellman_ford_with_negative_cycle(self):
        bellman_ford_manager = BellmanFord(self.negative_weighted_graph_with_negative_cycle)
        noeud = None
        while noeud not in self.negative_weighted_graph_with_negative_cycle:
            self.format_print.clear_console()
            self.format_print.log("Veuillez entrer le noeud de départ pour l'algorithme Bellman-Ford avec cycle négatif :", open=True, close=True)
            noeud = input("Noeud de départ : ")
            try:
                graph = bellman_ford_manager.bellman_ford(noeud)
                self.format_print.clear_console()
                self.format_print.log(f"Résultat de l'algorithme Bellman-Ford avec cycle négatif à partir du noeud {noeud} :", open=True)
                self.format_print.log(str(graph), close=True)
            except ValueError as e:
                self.format_print.log(str(e), open=True, close=True)
    def test_ford_fulkerson(self):
        self.format_print.log("L'algorithme Ford-Fulkerson n'est pas encore implémenté.", open=True, close=True)
    def test_edmonds_karp(self):
        self.format_print.log("L'algorithme Edmonds-Karp n'est pas encore implémenté.", open=True, close=True)