# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 11:50:01 2022

@author: Stephane
"""

class Recharge:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rayon = 20
        
    def draw(self, canvas):
        x0 = self.x - self.rayon    # top left
        y0 = self.y - self.rayon
        x1 = self.x + self.rayon    # bottom right
        y1 = self.y + self.rayon
        canvas.create_oval(x0, y0, x1, y1, outline="red", fill="", width=2)