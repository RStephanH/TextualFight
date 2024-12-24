import random 
"""
Creation des classes
"""
class Joueur:
    nombreJoueur=0
    def __init__(self, nom,pv=250):
        self.nom=nom
        self.pv=pv
        print("Un joueur vient d'être crée, son nom est {}".format(self.nom))
        Joueur.nombreJoueur+=1
    def attaquer(self,other):
        if not isinstance(other, Joueur):
            raise ValueError("Les combatants doivent être des joueurs")
        print("{} attaque!".format(self.nom))
        self.chanceAttaque=bool(random.randint(0,1))
        if self.chanceAttaque:
            self.domageAttaque=int(random.randint(0,100))
            other.pv-=self.domageAttaque
            print("{} a pris {} de degât \n Pv restant de {} = {}".format(other.nom,self.domageAttaque,other.nom,other.pv))
        elif not self.chanceAttaque:
            print("{} rate son attaque!".format(self.nom))
    @classmethod
    def combattre(cls,j1,j2):
        if not isinstance(j1,cls) or not isinstance(j2,cls):
            raise ValueError("Les combatants ne sont pas tous des joueurs")
        while j1.pv>0 and j2.pv>0:
            j1.attaquer(j2)
            if j2.pv<=0 :
                print("{} est K.O \n Le gagnant est {} avec {} de PV\nLe perdant est {} avec {} de PV".format(j2.nom,j1.nom,j1.pv,j2.nom,j2.pv))
                break
            j2.attaquer(j1)
            if j1.pv<=0 :
                print("{} est K.O \nLe gagnant est {} avec {} de Pv\nLe perdant est {} avec {} de Pv".format(j1.nom,j2.nom,j2.pv,j1.nom,j1.pv))
                break
"""
Creation des fonctions
"""
def creerJoueur():
    nomJ=str(input("Quel est votre nom jeune combatant(e):"))
    return nomJ




p1=Joueur(creerJoueur())