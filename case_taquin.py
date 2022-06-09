from tkinter import Canvas


class CaseTaquin:
    largeur = 80
    hauteur = 80
    fill = "grey"
    activefill = "green"
    font = ('Helvetica', '16')

    def __init__(self, canevas: Canvas, numero: int, x: int, y: int):
        self.x = x
        self.y = y
        self.numero = numero
        self.canevas = canevas
        self.id = None

    def draw(self):
        self.id = self.canevas.create_rectangle(self.x, self.y, self.x + CaseTaquin.largeur,
                                                self.y + CaseTaquin.hauteur, fill=CaseTaquin.fill,
                                                activefill=CaseTaquin.activefill)
        self.canevas.create_text(self.x + CaseTaquin.largeur // 2, self.y + CaseTaquin.hauteur // 2,
                                 text=str(self.numero), font=CaseTaquin.font)

    def deplace_droite(self):
        self.x = self.x + CaseTaquin.largeur
        self.canevas.move(self.id, CaseTaquin.largeur, 0)
        self.canevas.move(self.id + 1, CaseTaquin.largeur, 0)

    def deplace_gauche(self):
        self.x = self.x - CaseTaquin.largeur
        self.canevas.move(self.id, -CaseTaquin.largeur, 0)
        self.canevas.move(self.id + 1, -CaseTaquin.largeur, 0)

    def deplace_haut(self):
        self.y = self.y - CaseTaquin.hauteur
        self.canevas.move(self.id, 0, -CaseTaquin.hauteur)
        self.canevas.move(self.id + 1, 0, -CaseTaquin.hauteur)

    def deplace_bas(self):
        self.y = self.y + CaseTaquin.hauteur
        self.canevas.move(self.id, 0, CaseTaquin.hauteur)
        self.canevas.move(self.id + 1, 0, CaseTaquin.hauteur)

    def __str__(self):
        return f"({self.x},{self.y})"
