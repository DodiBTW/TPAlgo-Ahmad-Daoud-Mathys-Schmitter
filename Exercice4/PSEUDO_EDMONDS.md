# Pseudo code algorithme d'Edmonds-Karp

fonction edmonds_karp(graphe, source, puits):
    flot_max ← 0

    tant qu'il existe un chemin de source à puits dans le graphe résiduel (trouvé par BFS):
        flot_chemin ← capacité minimale sur ce chemin
        pour chaque arête du chemin:
            diminuer la capacité de l'arête de flot_chemin
            augmenter la capacité de l'arête inverse de flot_chemin
        flot_max ← flot_max + flot_chemin