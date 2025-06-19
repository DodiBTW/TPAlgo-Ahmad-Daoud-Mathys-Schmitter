from utils.fmt_print import FmtPrint
from test_graphs import TestGraphs

def menu(format_print: FmtPrint):
    format_print.log("1. Tester l'algorithme BFS", open=True , separate=True)
    format_print.log("2. Tester l'algorithme DFS", separate=True)
    format_print.log("3. Tester l'algorithme Dijkstra", separate=True)
    format_print.log("4. Tester l'algorithme Bellman-Ford", separate=True)
    format_print.log("5. Tester l'algorithme Bellman-Ford avec le graphe à cycle négatif", separate=True)
    format_print.log("6. Tester l'algorithme Ford Fulkerson", separate=True)
    format_print.log("7. Tester l'algorithme Edmonds Karp", separate=True)
    format_print.log("8. Tester l'algorithme de tri rapide randomisé", separate=True)
    format_print.log("0. Quitter", close=True)
    choice = input("Choisissez une option : ")

    return choice

def parse_choice(choice: str, format_print: FmtPrint, test_graphs: TestGraphs):
    if choice == "1":
        test_graphs.test_bfs()
    elif choice == "2":
        test_graphs.test_dfs()
    elif choice == "3":
        test_graphs.test_dijkstra()
    elif choice == "4":
        test_graphs.test_bellman_ford()
    elif choice == "5":
        test_graphs.test_bellman_ford_with_negative_cycle()
    elif choice == "6":
        test_graphs.test_ford_fulkerson()
    elif choice == "7":
        test_graphs.test_edmonds_karp()
    elif choice == "8":
        test_graphs.test_random_quick_sort()
    elif choice == "9":
        test_graphs.compare_quick_sort()
    else:
        format_print.log("Choix invalide, veuillez réessayer.", open=True, close=True)
        return