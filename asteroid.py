import pygame
from pygame.math import Vector2
import random
import core


class Asteroid:
    def __init__(self, largeur=400, hauteur=400):
        self.position = Vector2(random.randint(0, largeur), random.randint(0, hauteur))
        self.taille = 7
        self.couleur = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.vel = Vector2(random.randint(0, largeur), random.randint(0, hauteur))
        self.maxAcc = 300
        self.maxVel = 400

    def deplacement(self):

        # bilan des force
        self.vel = self.vel.normalize()

        # limiter la vitesse si trop grande
        if self.vel.length() > self.maxVel:
            self.vel.scale_to_length(self.maxVel)

        # ajouter vitesse a position
        self.position += self.vel


    def show(self, screen):
        pygame.draw.circle(screen, self.couleur, self.position, self.taille)


    def RAZ (self, largeur=400, hauteur=400):
        self.position = Vector2(random.randint(0, largeur), random.randint(0, hauteur))
        self.couleur = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


    def bord (self,screen):

        if self.position[0] > core.WINDOW_SIZE[0]:
            self.position[0] = 0
        elif self.position[0] < 0:
            self.position[0] = core.WINDOW_SIZE[0]
        elif self.position[1] > core.WINDOW_SIZE[1]:
            self.position[1] = 0
        elif self.position[1] < 0:
            self.position[1] = core.WINDOW_SIZE[1]
