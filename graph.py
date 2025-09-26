from utils import  display_graph_from_dict

def ajouter_noeud(d, noeudad) :
    """Ajoute un noeud au graphe

    Args:
        d (dict): graphe
        noeudad (str): noeud lettre à ajouter 
    """
    flag = False
    for noeud in d :
        if noeud == noeudad :
            flag = True
    if flag == False :
        d[noeudad] =[]
        

def ajouter_arete(d, noeud1, noeud2):
    """Ajouter une arrete

    Args:
        d (dict): graphe
        noeud1 (str): noeud lettre pour liaison
        noeud2 (str): noeud lettre pour liaison 
    """
    if (noeud1 in d) and (noeud2 in d) :
        if noeud2 not in d[noeud1] : 
            d[noeud1] = [noeud2]
        
def parcours_en_profondeur(g, deb):
    """Parcourt en profondeur le graphe

    Args:
        g (_type_): graphe
        deb (str): noeud à partir du quel on parcourt
    """
    a_explorer  = [deb]
    deja_visites = []
    while len(a_explorer) != 0 :
        n = a_explorer[-1]
        a_explorer.remove(n)
        if n not in deja_visites :
            deja_visites.append(n)
            for i in g[n]:
                if i not in deja_visites :
                    a_explorer.append(i)
                    
    print(deja_visites)

        
def parcours_en_largeur(g, deb):
    """Parcourt en largeur le graphe

    Args:
        g (_type_): graphe
        deb (str): noeud à partir du quel on parcourt
    """
    a_explorer = [deb]
    deja_visites = []
    while len(a_explorer) != 0 :
        n = a_explorer[0]
        a_explorer.remove(n)
        if n not in deja_visites :
            deja_visites.append(n)
            for i in g[n]:
                if i not in deja_visites :
                    a_explorer.append(i)
    print(deja_visites)
    