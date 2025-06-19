from utils.fmt_print import FmtPrint
import time
from random import randint
from Exercice1.dfs import DFS
from Exercice1.bfs import BFS
from Exercice2.dijkstra import Dijkstra
from Exercice3.bellman_ford import BellmanFord
from Exercice4.ford_fulkerson import FordFulkerson
from Exercice4.edmonds_karp import EdmondsKarp
from Exercice5.random_quick_sort import RandomQuickSort
from Exercice5.quick_sort import QuickSort


class TestGraphs:
    def __init__ (self, format_print: FmtPrint, unweighted_graph_to_use: dict, weighted_graph_to_use: dict, negative_weighted_graph_to_use: dict, negative_weighted_graph_with_negative_cycle: dict, network_graph: dict, random_array = []):
        self.unweighted_graph_to_use = unweighted_graph_to_use
        self.weighted_graph_to_use = weighted_graph_to_use
        self.negative_weighted_graph_to_use = negative_weighted_graph_to_use
        self.negative_weighted_graph_with_negative_cycle = negative_weighted_graph_with_negative_cycle
        self.format_print = format_print
        self.network_graph = network_graph
        self.random_array = random_array



    def test_bfs(self):
        bfs_manager = BFS(self.unweighted_graph_to_use)
        noeud = ""
        while noeud not in self.unweighted_graph_to_use:
            self.format_print.clear_console()
            self.format_print.log("Veuillez entrer le noeud de départ pour l'algorithme BFS :", open=True, close=True)
            noeud = input("Noeud de départ : ").upper()
        graph = bfs_manager.bfs(noeud)
        self.format_print.clear_console()
        self.format_print.log(f"Résultat de l'algorithme BFS à partir du noeud {noeud} :", open=True)
        self.format_print.log(str(graph), close=True)

    def test_dfs(self):
        dfs_manager = DFS(self.unweighted_graph_to_use)
        noeud = ""
        while noeud not in self.unweighted_graph_to_use:
            self.format_print.clear_console()
            self.format_print.log("Veuillez entrer le noeud de départ pour l'algorithme DFS :", open=True, close=True)
            noeud = input("Noeud de départ : ").upper()
        graph = dfs_manager.dfs(noeud)
        self.format_print.log(f"Résultat de l'algorithme DFS à partir du noeud {noeud} :", open=True)
        self.format_print.clear_console()
        self.format_print.log(str(graph), close=True)

    def test_dijkstra(self):
        dijkstra_manager = Dijkstra(self.weighted_graph_to_use)
        noeud = ""
        while noeud not in self.weighted_graph_to_use:
            self.format_print.clear_console()
            self.format_print.log("Veuillez entrer le noeud de départ pour l'algorithme Dijkstra :", open=True, close=True)
            noeud = input("Noeud de départ : ").upper()
        graph = dijkstra_manager.dijkstra(noeud)
        self.format_print.clear_console()
        self.format_print.log(f"Résultat de l'algorithme Dijkstra à partir du noeud {noeud} :", open=True)
        self.format_print.log(str(graph), close=True)
    def test_bellman_ford(self):
        bellman_ford_manager = BellmanFord(self.negative_weighted_graph_to_use)
        noeud = ""
        while noeud not in self.negative_weighted_graph_to_use:
            self.format_print.clear_console()
            self.format_print.log("Veuillez entrer le noeud de départ pour l'algorithme Bellman-Ford :", open=True, close=True)
            noeud = input("Noeud de départ : ").upper()
        graph = bellman_ford_manager.bellman_ford(noeud)
        self.format_print.clear_console()
        self.format_print.log(f"Résultat de l'algorithme Bellman-Ford à partir du noeud {noeud} :", open=True)
        self.format_print.log(str(graph), close=True)
    def test_bellman_ford_with_negative_cycle(self):
        bellman_ford_manager = BellmanFord(self.negative_weighted_graph_with_negative_cycle)
        noeud = ""
        while noeud not in self.negative_weighted_graph_with_negative_cycle:
            self.format_print.clear_console()
            self.format_print.log("Veuillez entrer le noeud de départ pour l'algorithme Bellman-Ford avec cycle négatif :", open=True, close=True)
            noeud = input("Noeud de départ : ").upper()
            try:
                graph = bellman_ford_manager.bellman_ford(noeud)
                self.format_print.clear_console()
                self.format_print.log(f"Résultat de l'algorithme Bellman-Ford avec cycle négatif à partir du noeud {noeud} :", open=True)
                self.format_print.log(str(graph), close=True)
            except ValueError as e:
                self.format_print.log(str(e), open=True, close=True)
    def test_ford_fulkerson(self):
        ford_fulkerson_manager = FordFulkerson(self.network_graph)
        source = ""
        sink = ""
        while source not in self.network_graph:
            self.format_print.clear_console()
            self.format_print.log("Veuillez entrer le noeud source pour l'algorithme Ford-Fulkerson :", open=True, close=True)
            source = input("Noeud source : ").upper()
        while sink not in self.network_graph:
            self.format_print.clear_console()
            self.format_print.log("Veuillez entrer le sink pour l'algorithme Ford-Fulkerson :", open=True, close=True)
            sink = input("Sink : ").upper()
        max_flow = ford_fulkerson_manager.ford_fulkerson(source, sink)
        self.format_print.clear_console()
        self.format_print.log(f"Résultat de l'algorithme Ford-Fulkerson entre {source} et {sink} :", open=True)
        self.format_print.log(f"Flux maximum : {max_flow}", close=True)

    def test_edmonds_karp(self):
        edmonds_karp_manager = EdmondsKarp(self.network_graph)
        source = ""
        sink = ""
        while source not in self.network_graph:
            self.format_print.clear_console()
            self.format_print.log("Veuillez entrer le noeud source pour l'algorithme Edmonds-Karp :", open=True, close=True)
            source = input("Noeud source : ").upper()
        while sink not in self.network_graph:
            self.format_print.clear_console()
            self.format_print.log("Veuillez entrer le sink pour l'algorithme Edmonds-Karp :", open=True, close=True)
            sink = input("Sink : ").upper()
        max_flow = edmonds_karp_manager.edmonds_karp(source, sink)
        self.format_print.clear_console()
        self.format_print.log(f"Résultat de l'algorithme Edmonds-Karp entre {source} et {sink} :", open=True)
        self.format_print.log(f"Flux maximum : {max_flow}", close=True)

    def test_random_quick_sort(self):
        random_quick_sort_manager = RandomQuickSort(self.random_array)
        self.format_print.clear_console()
        self.format_print.log("Tableau avant le tri :", open=True)
        self.format_print.log(str(self.random_array), close=True)
        random_quick_sort_manager.sort()
        self.format_print.clear_console()
        self.format_print.log("Tableau après le tri :", open=True)
        self.format_print.log(str(random_quick_sort_manager.array), close=True)

    def compare_quick_sort(self):
        random_array = [randint(1, 10000) for _ in range(1000000)]
        start_time_quick_sort = time.perf_counter()
        quick_sort_manager = QuickSort(random_array.copy())
        sorted_array = quick_sort_manager.sort()
        end_time_quick_sort = time.perf_counter()
        start_time_random_quick_sort = time.perf_counter()
        quick_sort_manager_random = RandomQuickSort(random_array.copy())
        sorted_array_random = quick_sort_manager_random.sort()
        end_time_random_quick_sort = time.perf_counter()
        self.format_print.clear_console()
        self.format_print.log("Comparaison des algorithmes de tri rapide pour un tableau de 1000000 elements :", open=True, separate=True)
        self.format_print.log(f"Tri rapide standard - temps : {end_time_quick_sort - start_time_quick_sort:.6f} secondes", separate=True)
        self.format_print.log(f"Tri rapide randomisé - temps : {end_time_random_quick_sort - start_time_random_quick_sort:.6f} secondes", close=True)
