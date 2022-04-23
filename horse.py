
import PIL
import pygame


class Horse:
    def __init__(self, name, color, image):
        self.name = name
        self.color = color
        self.image = PIL.Image.open(image)
        self.width, self.height = self.image.size
        self.image_winscreen =  self.image.resize((int(self.width/5), int(self.height/5)))
        self.load_pygame = pygame.image.load(image)
        self.image_game = pygame.transform.scale(self.load_pygame, (self.load_pygame.get_width() // 4, self.load_pygame.get_height() // 4))

