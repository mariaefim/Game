import pygame
from pygame.sprite import Sprite
class Gun(Sprite):

    def __init__(self,screen):
        """инициализация пушки"""
        super(Gun, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images2.0/дуло 2.0.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.centerx= self.screen_rect.centerx
        self.center = round(self.rect.centerx)
        """округление значения сдвига"""
        self.rect.bottom = self.screen_rect.bottom
        """bottom-координата у"""
        self.moveright =False
        self.moveleft = False

    def output(self):
        """рисование пушки"""
        self.screen.blit(self.image, self.rect)
        """blit-отрисовывает пушку"""
    def update_gun (self):
        """обновление позиции пушки"""
        if self.moveright == True and self.rect.right < self.screen_rect.right:
            self.center += 1.5
            """1,5-сглаживание сдвига"""
        if self.moveleft == True and self.rect.left > self.screen_rect.left:
            self.center -= 1.5

        self.rect.centerx = self.center

    def create_gun(self):
        self.center = self.screen_rect.centerx
        #создание новой пушки в середине после смерти

