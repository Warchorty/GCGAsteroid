import random
import pygame
from pygame.math import Vector2
import core


class Interface:
    def __init__(self,largeur=400,hauteur=400):
        self.position = Vector2(400,400)
        self.taille = 10
        self.couleur = (255,0,0)

    def show(self,screen):
        print(core.memory("resultat"))
