import random
import pygame
from pygame.math import Vector2
import core
import asteroid
import interface


class Vaisseau:

    def __init__(self,largeur=400,hauteur=400):
        self.position = Vector2(400,400)
        self.taille = 15
        self.couleur = (255,0,0)
        self.masse = 10
        self.vel = Vector2(0,0)
        self.maxAcc = 300
        self.maxVel = 440
        self.score= 0


    def deplacement(self, destination):
        if destination is not None:
            #bilan des force

            self.vel=destination -self.position
            self.vel = self.vel.normalize()
        else:
            self.vel= Vector2(0,0)

        #limiter la vitesse si trop grande
        if self.vel.length() > self.maxVel:
            self.vel.scale_to_length(self.maxVel)

        #ajouter vitesse a position
        self.position += self.vel

    def eat(self,asteroid):
        if asteroid.position.distance_to(self.position) < asteroid.taille + self.taille:
            self.score += 10
            core.memory("resultat",self.score)
            asteroid.RAZ()


    def show(self, screen):
        a = 0 - self.vel.angle_to(Vector2(0, 1))

        p1 = self.position + Vector2(-10, 0).rotate(a)
        p2 = self.position + Vector2(0, 30).rotate(a)
        p3 = self.position + Vector2(10, 0).rotate(a)

        core.Draw.polygon((255, 0, 0), ((p1), (p2), (p3)))

    def bord(self, screen):

        if self.position[0] > core.WINDOW_SIZE[0]:
            self.position[0] = 0
        elif self.position[0] < 0:
            self.position[0] = core.WINDOW_SIZE[0]
        elif self.position[1] > core.WINDOW_SIZE[1]:
            self.position[1] = 0
        elif self.position[1] < 0:
            self.position[1] = core.WINDOW_SIZE[1]
