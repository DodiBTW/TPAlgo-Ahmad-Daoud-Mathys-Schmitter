# Pseudo code algorithme de Dijkstra

fonction dijkstra(graphe, source):
    pour chaque sommet dans graphe:
        distance[sommet] ← infini
    distance[source] ← 0
    file_priorite ← tous les sommets du graphe

    tant que file_priorite n'est pas vide:
        u ← sommet avec la plus petite distance dans file_priorite
        retirer u de file_priorite

        pour chaque voisin de u:
            alt ← distance[u] + poids(u, voisin)
            si alt < distance[voisin]:
                distance[voisin] ← alt
                mettre à jour la priorité de voisin dans file_priorite

    retourner distance