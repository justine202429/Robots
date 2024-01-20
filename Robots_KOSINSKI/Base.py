# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 16:26:02 2022

@author: Stephane
"""

class Base:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rayon = 30
        
    def draw(self, canvas):
        x0 = self.x - self.rayon      #top left
        y0 = self.y - self.rayon
        x1 = self.x + self.rayon    #bottom right
        y1 = self.y + self.rayon
        canvas.create_oval(x0, y0, x1, y1, outline="black", fill="", width=2)