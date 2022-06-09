from tkinter import Canvas
from case_taquin import CaseTaquin
import random
from time import sleep


class Plateau(Canvas):
    decx = 5
    decy = 5

    def __init__(self, master, largeur=4):
        super().__init__(master, width=largeur * CaseTaquin.largeur + Plateau.decx,
                         height=largeur * CaseTaquin.hauteur + Plateau.decy)
        self.largeur = largeur
        self.plateau: list[CaseTaquin] = []
        self.initialisation()
        self.bind("<Button-1>", self.click)

    def initialisation(self):
        for i in range(self.largeur ** 2 - 1):
            self.plateau.append(
                CaseTaquin(self, i + 1, Plateau.decx + i % self.largeur * CaseTaquin.largeur,
                           Plateau.decy + i // self.largeur * CaseTaquin.hauteur))
        self.draw()
        for i in range(random.randint(5, 10)):
            for ct in self.plateau:
                self.deplace(ct)

    def draw(self):
        self.create_rectangle(Plateau.decx, Plateau.decy, Plateau.decx + self.largeur * CaseTaquin.largeur,
                              Plateau.decy + self.largeur * CaseTaquin.hauteur)
        for ct in self.plateau:
            ct.draw()

    def click(self, event):
        item = self.find_closest(event.x, event.y)
        ct = self.item_to_case_taquin(item)
        self.deplace(ct)
        if self.resolu():
            print("vous avez gagné")

    def deplace(self, ct: CaseTaquin):
        if ct is not None:
            if not self.pos_exist(ct.x - CaseTaquin.largeur, ct.y):
                ct.deplace_gauche()
            elif not self.pos_exist(ct.x + CaseTaquin.largeur, ct.y):
                ct.deplace_droite()
            elif not self.pos_exist(ct.x, ct.y + CaseTaquin.hauteur):
                ct.deplace_bas()
            elif not self.pos_exist(ct.x, ct.y - CaseTaquin.hauteur):
                ct.deplace_haut()

    def item_to_case_taquin(self, item):
        for ct in self.plateau:
            if ct.id == item[0]:
                return ct
        return None

    def resolu(self) -> bool:
        """return True si le taquin est résolu
        et False dans le cas contraire"""
        for i in range(len(self.plateau)):
            if (self.plateau[i].x, self.plateau[i].y) != (Plateau.decx + i % self.largeur * CaseTaquin.largeur,
                                                          Plateau.decy + i // self.largeur * CaseTaquin.hauteur):
                return False
        return True

    def pos_exist(self, x, y):
        if Plateau.decx <= x < Plateau.decx + self.largeur * CaseTaquin.largeur and Plateau.decy <= y < Plateau.decy + self.largeur * CaseTaquin.hauteur:
            for ct in self.plateau:
                if (ct.x, ct.y) == (x, y):
                    return True
            return False
        return True
