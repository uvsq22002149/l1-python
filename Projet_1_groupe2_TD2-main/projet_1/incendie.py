####################### Informations liées au groupe #############################
# Auteurs:
# LEFEBVRE Elora
# GAY Arnaud
# GIAMMONA Leandre
# Nicolas Mimaud
# REBATI Rayan
# PEREZ Martin
#
# Groupe 2
# MPCI TD2
# dépot Github:
# https://github.com/uvsq22001055/Projet_1_groupe2_TD2.git

####################### Import des libraries ###################################

import tkinter as tk
from random import randrange

####################### Definition des constantes ###############################

HEIGHT, WIDTH = 500, 750
ROW, COL = 50, 75
COTE = 10
COULEUR_QUADR = 'grey30'
C_WATER= '#7FFFD4'
C_FOREST = '#228B22'
C_FIRE= '#FF0000'
C_SHIRE = '#EEEB2C'
C_HOT_ASHES = '#8B0000'
C_COLD_ASHES ='#332D21'
water = 0
shire  = 1
forest = 2
fire = 3
hot_ashes = 4
cold_ashes = 5


####################### Definition des vraiables globales ########################

case = [[0 for row in range(ROW)] for col in range(COL)]
etat = [[water for row in range(ROW)] for col in range(COL)]

####################### Definition des fonctions #################################
def LandGrid():
    """Affiche un quadrillage constitué de carrés de côté COTE."""
    y = 0
    while y <= HEIGHT:
        canvas.create_line((0, y), (WIDTH, y), fill=COULEUR_QUADR)
        y += COTE
    x = 0
    while x <= WIDTH:
        canvas.create_line((x, 0), (x, HEIGHT), fill=COULEUR_QUADR)
        x += COTE


def ModifieCase():
    """Fixe le type de la case de coordonnées x,y."""
    pass

def Fire():
    """Modifie le type de la case cliquer en "feu"."""
    pass


def Stop():
    """Interrompt le programme.""" 
    pass


def Generate():
    """Fonction du boutton qui permet de générer un nouveau environnement. """
    for y in range(ROW):
        for x in range(COL):
            case[x][y] = canvas.create_rectangle((x*COTE, y*COTE,
 (x+1)*COTE, (y+1)*COTE), outline= COULEUR_QUADR, fill=C_WATER)
    for i in range(ROW * COL // 4):
        etat[randrange(COL)][randrange(ROW)] = shire
    for i in range(ROW * COL // 4):
        etat[randrange(COL)][randrange(ROW)] = forest
    for y in range(HEIGHT//10):
        for x in range(WIDTH//10):
            if etat[x][y]==0:
                coul = C_WATER
                canvas.itemconfig(case[x][y], fill=coul)
            elif etat[x][y] == 1:
                coul = C_SHIRE
                canvas.itemconfig(case[x][y], fill=coul)
            elif etat[x][y]==2 :
                coul= C_FOREST
                canvas.itemconfig(case[x][y], fill= coul)
    


def SaveFich():
    """Sauvgarde dans un ficher l'environement créer."""
    pass


def LoadLand():
    """Charge un fichier d'un environement"""
    pass


def Advancement():
    pass


def Counting():
    """Compte le nombre de case en feu et le nombre d'étape de la simulation"""
    pass


def Speed():
    """Permet de modifier la vitesse de la simulation"""
    pass


####################### Programme principal ###############################
racine = tk.Tk()
canvas = tk.Canvas(racine, height = HEIGHT, width = WIDTH, bg= 'white')

canvas.grid(column = 0, row=0)

LandGrid()
Generate()
###################### boutton #################

bouton_terrain_quelconque = tk.Button(racine, text = "Terrain au hasard")
bouton_sauvegrde_terrain = tk.Button(racine, text = "Sauvegarder le terrain")
bouton_charger_terrain = tk.Button(racine, text = "Ouvrir un terrain")
bouton_start = tk.Button(racine, text = "START")
bouton_stop = tk.Button(racine, text = "STOP")

bouton_terrain_quelconque.grid(column = 0, row = 0)
bouton_sauvegrde_terrain.grid(column =  0, row  =  1)
bouton_charger_terrain.grid(column =  0, row  =  2)
bouton_start.grid(column = 0, row = 3)
bouton_stop.grid(column = 0, row = 4)
canvas.grid(column = 1, row = 0, rowspan = 5)

canvas.bind('<1>', Fire)
canvas.bind('v', Speed)

racine.mainloop()