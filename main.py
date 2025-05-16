from utils.fmt_print import FmtPrint
from unweighted_graph import UnweightedGraph

unweighted_graph_to_use = {
                "A": ["B","C"],
                "B": ["A", "D", "E"],
                "C": ["A", "F"],
                "D": ["B"],
                "E": ["B", "F"],
                "F": ["C", "E"]
            }

weighted_graph_to_use = {
        "A": {"B": 1, "C": 2},
        "B": {"A": 1, "D": 3, "E": 4},
        "C": {"A": 2, "F": 5},
        "D": {"B": 3},
        "E": {"B": 4, "F": 6},
        "F": {"C": 5, "E": 6}
    }

negative_weighted_graph_to_use = {
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
    format_print.clear_console()
    format_print.log("Bienvenue au testeur d'algorithmes de graphes", open=True)
    format_print.log("Veuillez modifier le graphe dans le fichier graph.py afin de tester les algorithmes")
    format_print.log("Graphe non pondéré actuel :", close=True)
    graph_manager.ascii_graph()
    format_print.log("Graphe pondéré actuel :", open=True,close=True)
    print(weighted_graph_to_use)
    format_print.log("Graphe pondéré avec poids négatifs actuel :", open=True,close=True)
    print(negative_weighted_graph_to_use)