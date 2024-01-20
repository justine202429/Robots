# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 16:26:02 2022

@author: Stephane
"""
import math

class Robot:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dx = 1.0
        self.dy = 0.0
        self.rayon = 10
        self.vitesse = 10
        self.porte = None
        self.cible = None
        self.ramenes = 0
        self.energie = 100
        self.envie = True

    def __str__(self):
        s = "[(" + "{:3.2f}".format(self.x) + "," + "{:3.2f}".format(self.y) + ") " + str(self.ramenes) + "]"
        return s

    def draw(self, canvas):
        x0 = self.x - self.rayon      #top left
        y0 = self.y - self.rayon
        x1 = self.x + self.rayon    #bottom right
        y1 = self.y + self.rayon
        if self.envie == True :
            canvas.create_oval(x0, y0, x1, y1, outline="black", fill="lightgray", width=1)
            canvas.create_text((x0+x1)//2, (y0+y1)//2, text=str(self.ramenes))
        else : 
            canvas.create_oval(x0, y0, x1, y1, outline="black", fill="green", width=1)
            canvas.create_text((x0+x1)//2, (y0+y1)//2, text=str(self.ramenes))

    def distance(self, x, y):
        d = math.sqrt((x - self.x)**2 + (y-self.y)**2)
        return d

    def ramasse(self, jeton):
        self.cible = None
        jeton.estPortePar = self
        self.porte = jeton

    #--------------- A REALISER - Partie 1 --------------------
  # Pose le jeton que porte le robot
    #----------------------------------------------------------   
    def pose(self):
        if self.porte is not None :
            self.porte.estPortePar = None
            self.porte = None
        """if self.porte is not None :
            self.porte.x=self.x
            self.porte.y=self.y
            self.porte.estPortePar = None
            self.porte=None """
            
    def normaliserDirection(self):
         n = math.sqrt(self.dx**2 + self.dy**2)
         if n != 0:
             self.dx = self.dx / n
             self.dy = self.dy / n
         else:
             self.dx = 0
             self.dy = 0
             
    def allerVers(self, x, y):
         self.dx = x - self.x
         self.dy = y - self.y
         self.normaliserDirection()
         
    #---------- ----- A REALISER - Partie 1 --------------------
    # Déplace (une et une seule fois) le robot
    # maxx et maxy indiquent respectivement la largeur et
    # la hauteur du plateau. Le robot ne doit pas en sortir.
    #----------------------------------------------------------     
    def deplacer(self, maxx, maxy):
        self.normaliserDirection()
        new_x = self.x + self.dx*self.vitesse
        new_y = self.y + self.dy*self.vitesse
        if new_x>=0 and new_x<maxx and new_y>=0 and new_y<maxy :
            self.x=  new_x
            self.y= new_y
            if self.porte is not None :
                self.energie=self.energie-1
                self.porte.x=self.x
                self.porte.y=self.y
                self.porte.estPortePar = self
                