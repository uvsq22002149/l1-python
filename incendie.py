####################### Informations liées au groupe #################################
#Auteurs:
#LEFEBVRE Elora
#GAY Arnaud
#GIAMMONA Leandre
#Nicolas Mimaud
#REBATI Rayan
#PEREZ Martin
#
#Groupe 2
#MPCI TD2
#dépot Github:
#https://github.com/uvsq22001055/Projet_1_groupe2_TD2.git

####################### Import des libraries #################################

import tkinter as tk


####################### Definition des constantes #################################

HEIGHT, WIDTH = 500, 750
COTE = 10
COULEUR_QUADR = 'grey30'

####################### Definition des vraiables globales #################################

####################### Definition des fonctions #################################

def quadrillage():
    """Affiche un quadrillage constitué de carrés de côté COTE"""
    y = 0
    while y <= HEIGHT:
        canvas.create_line((0, y), (WIDTH, y), fill=COULEUR_QUADR)
        y += COTE
    x = 0
    while x <= WIDTH:
        canvas.create_line((x, 0), (x, HEIGHT), fill=COULEUR_QUADR)
        x += COTE


def mofiCase():
    pass

def fire():
    pass


def stop():
    pass


def generation():
    pass


def sauvgarderFich():
    pass


def chargeTerrain():
    pass


def avancement():
    pass


def comptage():
    pass


def vitesse():
    pass


####################### Programme  #################################

racine = tk.Tk()
racine.title("Simulation Incendie")
canvas = tk.Canvas(racine, height = HEIGHT, width = WIDTH, bg= '#7CB9E8')

canvas.grid(column = 0, row=0)

quadrillage()

####################### boutton #################

bouton_terrain_quelconque = tk.Button(racine, text = "terrain au hasard")
bouton_sauvegrde_terrain = tk.Button(racine, text = "sauvegarder le terrain")
bouton_charger_terrain = tk.Button(racine, text = "ouvrir un terrain")
bouton_start = tk.Button(racine, text = "start")
bouton_stop = tk.Button(racine, text = "stop")

bouton_terrain_quelconque.grid(column = 0, row = 0)
bouton_sauvegrde_terrain.grid(column = 0, row = 1)
bouton_charger_terrain.grid(column = 0, row = 2)
bouton_start.grid(column = 0, row = 3)
bouton_stop.grid(column = 0, row = 4)
canvas.grid(column = 1, row = 0, rowspan = 5)


racine.mainloop()