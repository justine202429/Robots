# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 15:46:48 2022

@author: Stephane
"""

class Jeton:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.estPortePar = None
        self.aLaMaison = False
        self.rayon = 4
        self.poison = False
        
    def __str__(self):
        s = "[<(" + str(self.x) + "," + str(self.y) + "," + str(self.poison) + ")>"
        return s
    
    def draw(self, canvas):
        x0 = self.x - self.rayon      #top left
        y0 = self.y - self.rayon
        x1 = self.x + self.rayon    #bottom right
        y1 = self.y + self.rayon
        if self.poison == False : 
            canvas.create_oval(x0, y0, x1, y1, outline="black", fill="white", width=1)
        else : 
            canvas.create_oval(x0, y0, x1, y1, outline="black", fill="green", width=1)
        
    def estDisponible(self):
        if (self.estPortePar == None) and (self.aLaMaison == False) :
            return True
        else :
            return False
    
    
        

        