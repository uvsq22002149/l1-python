####################### Informations liées au groupe #############################
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

####################### Import des libraries ###################################

import tkinter as tk


####################### Definition des constantes ###############################

HEIGHT, WIDTH = 500, 750
COTE = 10
COULEUR_QUADR = 'grey30'
C_WATER= '#7FFFD4'
C_FOREST = '#228B22'
C_FIRE= '#FF0000'
C_MEADOW = '#9ACD32'
C_HOT_ASHES = '#8B0000'
C_COLD_ASHES ='#332D21'

####################### Definition des vraiables globales ########################

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
    pass


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

canvas.grid(column = 1, row=0, rowspan = 5)

LandGrid()

###################### boutton #################

bouton_terrain_quelconque  =  tk . Button ( racine , text  =  "terrain au hasard" )
bouton_sauvegrde_terrain  =  tk . Button ( racine , text  =  "sauvegarder le terrain" )
bouton_charger_terrain  =  tk . Button ( racine , text  =  "ouvrir un terrain" )
bouton_start  =  tk . Button ( racine , text  =  "start" )
bouton_stop  =  tk . Button ( racine , text  =  "stop" )

bouton_terrain_quelconque . grid ( column  =  0 , row  =  0 )
bouton_sauvegrde_terrain . grid ( column  =  0 , row  =  1 )
bouton_charger_terrain . grid ( column  =  0 , row  =  2 )
bouton_start . grid ( column  =  0 , row  =  3 )
bouton_stop . grid ( column  =  0 , row  =  4 )


racine.mainloop()