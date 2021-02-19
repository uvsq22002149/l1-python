####################### Informations liées au groupe #################################
#Auteurs:
#LEFEBVRE Elora
#GAY Arnaud
#PEREZ CENIT Martin
#
#
#Groupe 2
#MPCI TD2
#dépot Github:
#https://github.com/uvsq22001055/Projet_1_groupe2_TD2.git


import tkinter as tk

COTE = 10
HAUTEUR = 600
LARGEUR = 1000
COULEUR_QUADR = "white"

def quadrillage():
    """Affiche un quadrillage constitué de carrés de côté COTE"""
    y = 0
    while y <= HAUTEUR:
        canvas.create_line((0, y), (LARGEUR, y), fill=COULEUR_QUADR)
        y += COTE
    x = 0
    while x <= LARGEUR:
        canvas.create_line((x, 0), (x, HAUTEUR), fill=COULEUR_QUADR)
        x += COTE
    

racine = tk.Tk()
racine.title("incendie")

canvas = tk.Canvas(racine, height = HAUTEUR, width = LARGEUR, bg = "blue")
canvas.grid()

quadrillage()

racine.mainloop()
