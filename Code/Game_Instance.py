# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 15:08:05 2022

@author: Thibaud
"""


#%%

class Game_Instance:
    
    nb_j = 4 à 8 
    joueurs = tableau 8 object joueur
    plateau = {
        "pioche"   : object deck,
        "defausse" : object carte,
        "zones"    : object tableau 8 object zone, (zone : matrice 4 * 3 object carte)
        "points"   : [0,0,0,0,0,0,0,0]
        }
    
    
    def __init__(self):
        pass
    
    def manche:
        # Préparation d'une manche
        deck = self.plateau["pioche"]
        zones = self.plateau["zones"]
        
        deck.reset()
        deck.distribuer(nombre_de_joueur = nb_j,zones)
        defausse = deck.tirer()
        
        joueurs = self.joueurs
        
        # Début d'une manche
        for joueur in joueurs:
            joueur.retourne_2()
        
        j_actif = zones.plus_grand() #si égalité faire un top juste pour compter pour moi
        
        # Déroulemet d'une manche
        while not joueurs[j_actif].fin() : # Fin d'une manche
            self.jouer(j_actif)
            j_actif = (j_actif + 1) % nb_j
        
        # Décompte des points
        for joueur in joueurs:
            joueur.retourne_tout()
        j_petit = zones.plus_petit() #si égalité perdu
        
        
   
        
        
        pass
    
    def partie:
        pass
    


#%%
