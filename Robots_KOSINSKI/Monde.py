# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 16:23:11 2022

@author: Stephane
"""

from Robot import Robot
from Jeton import Jeton
from Base import Base
from Recharge import Recharge

from tkinter import * 

import random
import math

class Monde(Frame):

    def __init__(self, parent, dimx, dimy):

        # Données globales59
        self.robots = []            # Les robots
        self.jetons = []            # Les jetons
        self.nbRobots = 10         # Le nombre de robots
        self.nbJetons = 15          # Le nombre de jetons
        self.nbjetonspoisons = 5
        self.base = Base(100, 300)  # La base où ramener les jetons
        self.recharges = []         # Les zones de recharge
        self.nbRecharges = 3        # Le nombre de zones de recharge
        self.dimx = dimx            # La largeur du plateau
        self.dimy = dimy            # La hauteur du plateau
     


        # Indique si les robots ciblent le jeton disponible le plus proche
        # ou non - ne pas toucher
        self.plusproche = False   

        # L'interface graphique
        super().__init__()
        self.initUI()

        # Affic her
        self.update()

    def initUI(self):
        self.master.title("Robots")

        self.boutons = Frame(self.master)
        self.boutons.grid(row=0, column=0)

        # boutons
        self.creation1 = Button(self.boutons, text="Creer Jetons", command=self.creerj)
        self.creation1.grid(row=0, column=0, sticky='w')
        self.creation2 = Button(self.boutons, text="Creer Recharges", command=self.creerrc)
        self.creation2.grid(row=1, column=0, sticky='w')
        self.creation3 = Button(self.boutons, text="Creer Robots", command=self.creer)
        self.creation3.grid(row=0, column=1, sticky='w')
        self.creation4 = Button(self.boutons, text="Creer Robots Aléatoire", command=self.creerAleatoire)
        self.creation4.grid(row=1, column=1, sticky='w')
        self.go = Button(self.boutons, text="Go - aléatoire", command=self.demarrer)
        self.go.grid(row=0, column=2, sticky='w')
        self.goA = Button(self.boutons, text="Go - plus proche", command=self.demarrerA)
        self.goA.grid(row=1, column=2, sticky='w')


        # Affichage
        self.pireslabel = Label(self.boutons)
        self.pireslabel.grid(row=0, column=3, sticky='w')
        self.meilleurslabel = Label(self.boutons)
        self.meilleurslabel.grid(row=1, column=3, sticky='w')

        # plateau
        self.ecran = Frame(self.master)
        self.ecran.grid(row=1, column=0)
        self.canvas = Canvas(self.ecran, width=800, height=600)
        self.canvas.grid(row=0, column=0, sticky="w")
        self.canvas.configure(background="lightblue")

    # Permet de mettre à jour l'a ffichage
    def update(self):
        self.canvas.delete("all")
        self.base.draw(self.canvas)
        for r in self.robots:
            r.draw(self.canvas)
        for j in self.jetons:
            j.draw(self.canvas)
        for rc in self.recharges:
            rc.draw(self.canvas)
        if len(self.robots)>2:
            pires = self.piresRobots()
            meilleurs = self.meilleursRobots()
            sp = "Pires : "
            sm = "Meilleurs : "
            if len(pires) > 0:
                sp = sp + str(pires[0]) + " " + str(pires[1]) + " " + str(pires[2])
            if len(meilleurs) > 0:
                sm = sm + str(meilleurs[0]) + " " + str(meilleurs[1]) + " " + str(meilleurs[2])
            self.pireslabel.configure(text=sp)
            self.meilleurslabel.configure(text=sm)
    # Commande pour creer les bombes 

    # Commande pour créer les jetons
    def creerj(self):
        self.jetons.clear()
        self.creerJetonsAleatoires(self.nbJetons)
        self.update()

    # Commande pour créer les recharges       
    def creerrc(self):
        self.recharges.clear()
        self.creerRecharges(self.nbRecharges)
        self.update()

    # Commande pour créer les robots dans la base       
    def creer(self):
        self.robots.clear()
        self.creerRobots(self.nbRobots)
        self.update()

    # Commande pour créer les robots placés aléatoirement
    def creerAleatoire(self):
        self.robots.clear()
        self.creerRobotsAleatoire(self.nbRobots)
        self.update()

    # Commande pour lancer la simulation
    # Le robot cible un jeton disponible al� �atoire
    def demarrer(self):
        self.plusproche = False
        self.timer()

    # Commande pour lancer la simulation
    # Le robot cible le jeton disponible le plus proche
    def demarrerA(self):
        self.plusproche = True
        self.timer()

    # Timer qui déclenche la routine principale toutes x ms
    def timer(self):
        self.run()
        self.after(100, self.timer)

    # Boucle principale qui réalise le comportement de chaque robot 
    def run(self):
        for r in self.robots:
            self.nextStep(r, self.plusproche)
        self.update()

    # Création de la base
    def creerBase(self):
        self.base = Base(100, 300)

    # Création des robots, tous positionnés dans la base
    def creerRobots(self, nrobots):
        for i in range(0, nrobots):
            self.robots.append(Robot(self.base.x, self.base.y))

    # Création des jetons placés aléatoirement sur le plateau
    def creerJetonsAleatoires(self, njetons):
        offset = 30 
        nbpoison = 0
        for i in range(0, njetons):
            Jeton.poison=False
            x = random.randint(0 + offset, self.dimx - offset)
            y = random.randint(0 + offset, self.dimy - offset)
            if nbpoison != self.nbjetonspoisons :
                nbpoison+=1
                monJeton = Jeton(x, y)
                monJeton.poison=True
            else : 
                x = random.randint(0 + offset, self.dimx - offset)
                y = random.randint(0 + offset, self.dimy - offset)
                monJeton = Jeton(x,y)
            self.jetons.append(monJeton)
            
    def creerRobotsAleatoire(self, nrobots):
        offset = 30
        for i in range(0, nrobots):
            x = random.randint(0 + offset, self.dimx - offset)
            y = random.randint(0 + offset, self.dimy - offset)
            self.robots.append(Robot(x, y))
            
    #--------------- A REALISER - Partie 2 --------------------
    # Création des zones de recharges
    #----------------------------------------------------------               
    def creerRecharges(self, nrecharges ):
        self.recharges.append(Recharge(100, 300))
        self.recharges.append(Recharge(450, 100))
        self.recharges.append(Recharge(450, 500))                     

    #--------------- A REALISER - Partie 1 --------------------
    # Retourne la liste des jetons disponibles
    #----------------------------------------------------------
    def jetonsDisponibles(self):
        disponibles = []
        for jeton in self.jetons :
            if jeton.estDisponible() :
                disponibles.append(jeton)
        return disponibles

    #--------------- A REALISER - Partie 1 --------------------
    # Retourne le jeton disponible le plus proche du robot
    # passé en paramètre avec la liste des jetons disponibles
    #----------------------------------------------------------
    def disponibleLePlusProche(self, robot, jetonsDisponibles):
        jeton = None
        if len(jetonsDisponibles)>0 :
            minimum = robot.distance(jetonsDisponibles[0].x, jetonsDisponibles[0].y)
            jeton=jetonsDisponibles[0]
            for element in jetonsDisponibles:
                if minimum>robot.distance(element.x, element.y):
                    minimum=robot.distance(element.x, element.y)
                    jeton=element
        return jeton

    #--------------- A REALISER - Partie 1 --------------------
    # Retourne aléatoirement un jeton disponible parmi la
    # liste des jetons disponibles
    #----------------------------------------------------------
    def disponibleAleatoire(self, jetonsDisponibles):
        jeton = None
        if len(jetonsDisponibles)>0 :
            jeton = random.choice(jetonsDisponibles)
        return jeton

    #--------------- A REALISER - Partie 2 --------------------
    # Retourne la zone de recharge la plus proche du robot
    # passé en paramètre
    #-------------- --------------------------------------------
    def rechargeLaPlusProche(self, robot):
        recharge = None 
        if len(self.recharges)>0 :
            minimum = robot.distance(self.recharges[0].x, self.recharges[0].y)
            recharge=self.recharges[0]
            for element in self.recharges:
                if minimum>robot.distance(element.x, element.y):
                    minimum=robot.distance(element.x, element.y)
                    recharge=element
        return recharge


    #--------------- A REALISER - Partie 2 --------------------
    # Trie le tableau de robots en fonction de l'ordre
    # croissant des nombres de jetons ramenés par robot
    #----------------------------------------------------------
    def trierRobots(self):
        '''
        tab=[] ; 
        for i in range(0,len(self.robots)) :
            tab.append(self.robots[i].ramenes)
        n = len(tab);
        for i in range(0,n-1):
            for j in range(n-1,i,-1):
                if tab[j-1] >  tab[j]: 
                    #-- Echange les 2 valeurs --#
                    aux =  tab[j-1];
                    tab[j-1] = tab[j];
                    tab[j] = aux; 
        return  tab
        '''
        n = len(self.robots);
        for i in range(0,n-1):
            for j in range(n-1,i,-1):
                if self.robots[j-1].ramenes >  self.robots[j].ramenes: 
                    #-- Echange les 2 valeurs --#
                    aux =  self.robots[j-1];
                    self.robots[j-1] =  self.robots[j];
                    self.robots[j] = aux; 
        return  self.robots 
    
        
    #--------------- A REALISER - Partie 2 --------------------
    # Retourne la liste des trois robots qui ont ramené le
    # moins de jetons                                                             
    #----------------------------------------------------------
    def piresRobots(self):
        pires = []         
        croissant=self.trierRobots() 
        for i in range(0,3) :
            pires.append(croissant[i]) 
        return pires 

    #--------------- A REALISER - Partie 2 --------------------
    # Retourne la liste des trois robots qui ont ramené le
    # plus de jetons
    #------- ---------------------------------------------------
    def meilleursRobots(self):
        meilleurs = []
        croissant=self.trierRobots()  
        for i in range(1,4) :
            meilleurs.append(croissant[-i]) 
        return meilleurs

    #--------------- A REALISER - Partie 1 & 2 --------------------
    # Détermine la prochaine action du robot
    # plusproche = True signifie que le robot cible le jeton
    #                   disponible le plus proche
    # plusproche = False signifie que le robot cible un jeton
    #                   disponible au hasard
    #----------------------------------------------------------
    def nextStep(self, robot, plusproche):
        
        if robot.energie != 0 :
            if robot.porte is not None :
                if robot.porte.poison is True :
                    robot.x=robot.porte.x
                    robot.y=robot.porte.y   
                    robot.vitesse=0
                    robot.energie=100
                    robot.envie=False
                if robot.distance(self.base.x,self.base.y)<=self.base.rayon :
                    robot.porte.aLaMaison=True
                    robot.pose()
                    robot.ramenes+=1
                else :
                    robot.allerVers(self.base.x,self.base.y) 
                
            else :
                if robot.cible is not None : 
                    if not robot.cible.estDisponible() : 
                        robot.cible = None
                if robot.cible is None :
                    jetonsDispo = self.jetonsDisponibles() 
                    if plusproche :
                        robot.cible = self.disponibleLePlusProche(robot,jetonsDispo) 
                    else :
                        robot.cible=self.disponibleAleatoire(jetonsDispo)
                if robot.cible is not None :
                    if robot.distance(robot.cible.x, robot.cible.y)<5 :
                        robot.ramasse(robot.cible)
                    else :
                        robot.allerVers(robot.cible.x,robot.cible.y)
        else :
            robot.pose() 
            #robot.porte.estPortePar = None 
            robot.porte = None 
            robot.allerVers(self.rechargeLaPlusProche(robot).x,self.rechargeLaPlusProche(robot).y)
        if self.rechargeLaPlusProche(robot) is not None :
            if robot.distance(self.rechargeLaPlusProche(robot).x,self.rechargeLaPlusProche(robot).y)<=self.rechargeLaPlusProche(robot).rayon and robot.energie==0:
                robot.energie=100 

        # Déplacer le robot d'un pas   
        robot.deplacer(self.dimx, self.dimy) # A conserver à la fin de la méthode

#--- ------- Programme Principal -----------------------------------------------   

def main():
    root = Tk()
    root.geometry('800x600')
    monde = Monde(root, 800, 600)
    root.mainloop()

if __name__ == '__main__':
    main()
