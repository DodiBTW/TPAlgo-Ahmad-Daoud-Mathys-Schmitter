from utils.fmt_print import FmtPrint
from unweighted_graph import UnweightedGraph
from test_graphs import TestGraphs
from Exercice1.dfs import DFS
from Exercice1.bfs import BFS
from Exercice2.dijkstra import Dijkstra
from menu import menu, parse_choice

unweighted_graph_to_use = {
    "A": ["B","C"],
    "B": ["A", "D"],
    "C": ["A", "E"],
    "D": ["B", "F"],
    "E": ["C"],
    "F": ["D"]
}

weighted_graph_to_use = {
    "A": {"B": 4, "C": 2},
    "B": {"A": 4, "D": 5},
    "C": {"A": 2, "E": 3},
    "D": {"B": 5, "F": 6},
    "E": {"C": 3},
    "F": {"D": 6}
}



# SANS CYCLE NEGATIF 
#    6        2        1        -4
# A---->B---->D---->E------->F
# |     |                ^
# |     |                |
# |     v                |
# |    C---->F<----------+
# |     \      3
# |      \-------------->
# |             5
# +--------------------->C
# Chatgpt a généré ça, donc il est pas très correct mais bon.
negative_weighted_graph_to_use = {
    "A": {"B": 6, "C": 5},
    "B": {"C": -2, "D": 2},
    "C": {"F": 3},
    "D": {"E": 1},
    "E": {"F": -4},
    "F": {}
}
negative_weighted_graph_with_negative_cycle = {
    "A": {"B": 1, "C": 2},
    "B": {"A": 1, "D": -3, "E": 4},
    "C": {"A": 2, "F": 5},
    "D": {"B": -3},
    "E": {"B": 4, "F": 6},
    "F": {"C": 5, "E": 6}
}

if __name__ == "__main__":
    graph_manager = UnweightedGraph(unweighted_graph_to_use)
    format_print = FmtPrint()
    test_graphs = TestGraphs(format_print, unweighted_graph_to_use, weighted_graph_to_use, negative_weighted_graph_to_use, negative_weighted_graph_with_negative_cycle)
    format_print.clear_console()
    format_print.log("Bienvenue au testeur d'algorithmes de graphes", open=True)
    format_print.log("Graphe non pondéré actuel :", close=True)
    graph_manager.ascii_graph()
    while True:
        choice = menu(format_print)
        choice = choice.strip()
        format_print.clear_console()
        if choice == "0":
            break
        else:
            parse_choice(choice, format_print, test_graphs)
