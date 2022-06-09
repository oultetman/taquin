from tkinter import Tk, Canvas
from case_taquin import CaseTaquin
from plateau import Plateau

fenetre = Tk()
fenetre.title("Taquin")
fenetre.geometry("480x480")
p = Plateau(fenetre,3)
p.pack()



fenetre.mainloop()
