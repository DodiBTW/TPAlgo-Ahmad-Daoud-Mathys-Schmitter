# Pseudo code algorithme AVL

fonction inserer_AVL(racine, clé):
    si racine est nul:
        retourner nouveau_noeud(clé)
    si clé < racine.clé:
        racine.gauche ← inserer_AVL(racine.gauche, clé)
    sinon si clé > racine.clé:
        racine.droite ← inserer_AVL(racine.droite, clé)
    sinon:
        retourner racine

    mettre à jour la hauteur de racine

    équilibre ← hauteur(racine.gauche) - hauteur(racine.droite)

    si équilibre > 1 et clé < racine.gauche.clé:
        retourner rotation_droite(racine)
    si équilibre < -1 et clé > racine.droite.clé:
        retourner rotation_gauche(racine)
    si équilibre > 1 et clé > racine.gauche.clé:
        racine.gauche ← rotation_gauche(racine.gauche)
        retourner rotation_droite(racine)
    si équilibre < -1 et clé < racine.droite.clé:
        racine.droite ← rotation_droite(racine.droite)
        retourner