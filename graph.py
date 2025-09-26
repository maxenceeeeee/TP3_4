from utils import  display_graph_from_dict

def ajouter_noeud(d, noeudad) :
    flag = False
    for noeud in d :
        if noeud == noeudad :
            flag = True
    if flag == False :
        d[noeudad] =[]
        

def ajouter_arete(d, noeud1, noeud2):
    if (noeud1 in d) and (noeud2 in d) :
        if noeud2 not in d[noeud1] : 
            d[noeud1] = [noeud2]
        
def parcours_en_profondeur(g, deb):
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
    