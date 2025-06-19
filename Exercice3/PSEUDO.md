# Pseudo code algorithme de Bellman-Ford

fonction bellman_ford(graphe, source):
    pour chaque sommet dans graphe:
        distance[sommet] ← infini
    distance[source] ← 0

    pour i de 1 à nombre_de_sommets - 1:
        pour chaque sommet u dans graphe:
            pour chaque voisin v de u:
                si distance[u] + poids(u, v) < distance[v]:
                    distance[v] ← distance[u] + poids(u, v)

    pour chaque sommet u dans graphe:
        pour chaque voisin v de u:
            si distance[u] + poids(u, v) < distance[v]:
                retourner "Cycle de poids négatif détecté"

    retourner distance