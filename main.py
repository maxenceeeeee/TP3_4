from utils import  *
from graph import * 
def main() : 
    dictionnaire = {
        "A" : ["B"],
        "B" : [],
        "C" : ["A", "B"],
        "D" : ["C"],
        "E" : ["C", "D"]
    
    }
    
    arbre = {
        0: ('exp', [1]),
        1: ('+', [2, 3]),
        2: ('2', []),
        3: ('y', [])
    }
    
    display_graph_from_dict(dictionnaire)
    ajouter_noeud(dictionnaire, "F")
    print(dictionnaire)
    display_graph_from_dict(dictionnaire)
    ajouter_arete(dictionnaire, "F", "E")
    print(dictionnaire)
    display_graph_from_dict(dictionnaire)
    
    parcours_en_profondeur(dictionnaire, "E")
    parcours_en_largeur(dictionnaire, "E")
    display_expression_tree_from_dictv2(arbre)

main()
