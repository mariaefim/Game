import pygame.font
#возможность измнения счета
from heart import Heart
from pygame.sprite import Group

class Scores():
    def __init__(self, screen, stats, heart):
        """инициализируем подсчет очков """
        self.screen = screen
        self.heart = heart
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 36)   #выбираем цвет и тип шрифта
        self.image_score()       #вызываем функцию изображения с текущим счетом
        self.image_high_score ()
        self.image_hearts()     #вызываем функцию с изображением жизней

    def image_score(self):
        """преобразование текст счета в графическое изображение"""
        self.score_image = self.font.render(str(self.stats.score), True, self.text_color, (179, 229, 252))
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 40
        self.score_rect.top = 20       #отступаем от краев для размещения изображения

    def  image_high_score(self):
        """преобразует рекорд в графическое изображение"""
        self.high_score_image = self.font.render (str(self.stats.high_score), True, self.text_color, (179, 229, 252))
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.screen_rect.top + 20

    def image_hearts(self):
        """количество жизней"""
        self.hearts= Group()
        for heart_number in range(self.stats.guns_left):    #перебираем количество остав шихся пушек
            heart = Heart(self.screen)
            heart.rect.x = 15 + heart_number * heart.rect.width
            heart.rect.y = 20
            self.hearts.add(heart)

    def show_score(self):
        """вывод счета на экран"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.hearts.draw(self.screen)

