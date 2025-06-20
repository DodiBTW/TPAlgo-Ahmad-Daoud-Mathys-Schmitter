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
from Exercice6.avl import AVL

class TestGraphs:
    def __init__ (self, format_print: FmtPrint, unweighted_graph_to_use: dict, weighted_graph_to_use: dict, negative_weighted_graph_to_use: dict, negative_weighted_graph_with_negative_cycle: dict, network_graph: dict, random_array = [], numbers_for_avl = []):
        self.unweighted_graph_to_use = unweighted_graph_to_use
        self.weighted_graph_to_use = weighted_graph_to_use
        self.negative_weighted_graph_to_use = negative_weighted_graph_to_use
        self.negative_weighted_graph_with_negative_cycle = negative_weighted_graph_with_negative_cycle
        self.format_print = format_print
        self.network_graph = network_graph
        self.random_array = random_array
        self.numbers_for_avl = numbers_for_avl

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
        self.format_print.clear_console()
        self.format_print.log("Temps de tri avec QuickSort :", open=True)
        self.format_print.log(f"{end_time_quick_sort - start_time_quick_sort:.6f} secondes", close=True)


    def test_avl_tree(self):
        avl_tree_manager = AVL()
        for number in self.numbers_for_avl:
            avl_tree_manager.insert(number)
        self.format_print.clear_console()
        self.format_print.log("Arbre AVL après insertion des nombres :", open=True)
        self.format_print.log(avl_tree_manager.pretty_print(), close=True)

    def test_avl_tree_rebalancing(self):
        avl_tree_manager = AVL()
        # Cas 1: Rotation simple à droite (insertion)
        self.format_print.log("Test rotation simple à droite (insertion):", open=True)
        for n in [30, 20, 10]:
            avl_tree_manager.insert(n)
        self.format_print.log(avl_tree_manager.pretty_print(), close=True)
        # Cas 2: Rotation simple à gauche (insertion)
        avl_tree_manager = AVL()
        self.format_print.log("Test rotation simple à gauche (insertion):", open=True)
        for n in [10, 20, 30]:
            avl_tree_manager.insert(n)
        self.format_print.log(avl_tree_manager.pretty_print(), close=True)
        # Cas 3: Double rotation gauche-droite (insertion)
        avl_tree_manager = AVL()
        self.format_print.log("Test double rotation gauche-droite (insertion):", open=True)
        for n in [30, 10, 20]:
            avl_tree_manager.insert(n)
        self.format_print.log(avl_tree_manager.pretty_print(), close=True)
        # Cas 4: Double rotation droite-gauche (insertion)
        avl_tree_manager = AVL()
        self.format_print.log("Test double rotation droite-gauche (insertion):", open=True)
        for n in [10, 30, 20]:
            avl_tree_manager.insert(n)
        self.format_print.log(avl_tree_manager.pretty_print(), close=True)
        # Cas 5: Rotation après suppression
        avl_tree_manager = AVL()
        for n in [20, 10, 30, 25, 40, 22]:
            avl_tree_manager.insert(n)
        self.format_print.log("Arbre avant suppression (pour test de rééquilibrage):", open=True)
        self.format_print.log(avl_tree_manager.pretty_print(), close=True)
        avl_tree_manager.delete(40)
        self.format_print.log("Arbre après suppression de 40 (rééquilibrage attendu):", open=True)
        self.format_print.log(avl_tree_manager.pretty_print(), close=True)
        # Cas 6: Suppression provoquant une double rotation
        avl_tree_manager = AVL()
        for n in [50, 30, 70, 20, 40, 60, 80, 65]:
            avl_tree_manager.insert(n)
        self.format_print.log("Arbre avant suppression (double rotation attendue):", open=True)
        self.format_print.log(avl_tree_manager.pretty_print(), close=True)
        avl_tree_manager.delete(80)
        self.format_print.log("Arbre après suppression de 80 (double rotation attendue):", open=True)
        self.format_print.log(avl_tree_manager.pretty_print(), close=True)