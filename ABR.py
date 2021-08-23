from arbre_fini import arbre,noeud


class ABR:
    """ Une classe arbre binaire de recherche basique"""
    def __init__(self, tab):
        """noeud->arbre
            Crée un arbre de racine r"""
        self.__racine = noeud(tab.pop(0))
        while len(tab)>0 :
            r = self.__racine
            cherche = True
            n = noeud(tab.pop(0))
            while cherche :
                if n.Lire_valeur() < r.Lire_valeur() :
                    if r.Lire_fg() == None :
                        r.Attr_fg(n)
                        n.Attr_pere(r)
                        cherche = False
                    else :
                        r = r.Lire_fg()
                else:
                    if r.Lire_fd() == None :
                        r.Attr_fd(n)
                        n.Attr_pere(r)
                        cherche = False
                    else :
                        r = r.Lire_fd()

    def __repr__(self):
        """None->String
            Retourne la chaîne servant pour l'affichage de l'arbre"""
        if self.__racine.Lire_fd()==None and self.__racine.Lire_fg()==None :
            return str(self.__racine.Lire_valeur())
        elif self.__racine.Lire_fd()==None :
            return "("+str(self.sous_arbre(self.__racine.Lire_fg()))+")<-"+str(self.__racine.Lire_valeur())
        elif self.__racine.Lire_fg()==None : 
            return str(self.__racine.Lire_valeur())+"->("+str(self.sous_arbre(self.__racine.Lire_fd()))+")"
        else :
            return "("+str(self.sous_arbre(self.__racine.Lire_fg()))+")<-"+str(self.__racine.Lire_valeur())+"->("+str(self.sous_arbre(self.__racine.Lire_fd()))+")"

    def ajouter(self, valeur):
        """noeud*noeud*String->None
            Ajoute le noeud n à l'arbre appelant en fils du noeud pere. Si position est "g" c'est un fils
            gauche, sinon un fils droit. Par défaut c'est un fils gauche."""
        r = self.__racine
        cherche = True
        n = noeud(valeur)
        while cherche :
            if n.Lire_valeur() < r.Lire_valeur() :
                if r.Lire_fg() == None :
                    r.Attr_fg(n)
                    n.Attr_pere(r)
                    cherche = False
                else :
                    r = r.Lire_fg()
            else:
                if r.Lire_fd() == None :
                    r.Attr_fd(n)
                    n.Attr_pere(r)
                    cherche = False
                else :
                    r = r.Lire_fd()

    def sous_arbre(self, r):
        return arbre(r)

    def Lire_racine(self):
        return self.__racine
     

    def infixe(self):
        """None->String
            Renvoie la chaîne correspndant au parcours infixe de l'arbre appelant"""
        if self.__racine.Lire_fd()==None and self.__racine.Lire_fg()==None :
            return str(self.__racine.Lire_valeur())
        elif self.__racine.Lire_fd()==None :
            return self.sous_arbre(self.__racine.Lire_fg()).infixe() + " " + str(self.__racine.Lire_valeur())
        elif self.__racine.Lire_fg()==None : 
            return str(self.__racine.Lire_valeur()) + " " + self.sous_arbre(self.__racine.Lire_fd()).infixe()
        else :
            return self.sous_arbre(self.__racine.Lire_fg()).infixe() + " " + str(self.__racine.Lire_valeur()) + " " + self.sous_arbre(self.__racine.Lire_fd()).infixe()

    def tri(self):
        """None->String
            trie les données de l'ABR"""
        return self.infixe()

    def min(self):
        r = self.__racine
        while r.Lire_fg() != None :
            r = r.Lire_fg()
        return r.Lire_valeur()

    def max(self):
        r = self.__racine
        while r.Lire_fd() != None :
            r = r.Lire_fd()
        return r.Lire_valeur()

if __name__ == "__main__":
    print([10,2,5,12,15,20,1,3,7,25])
    a = ABR([10,2,5,12,15,20,1,3,7,25])
    print(a)
    print(a.tri())
    print(a.min())
    print(a.max())
    a.ajouter(16)
    print(a)
