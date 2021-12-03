import pygame, controls
from gun import Gun
from pygame.sprite import Group
from stats import Stats
from pig import Pig
from scores import Scores
from heart import Heart


def run():
    pygame.init()
    screen = pygame.display.set_mode((1000,600))
    pygame.display.set_caption("Minecraft 2" )
    bg_color = (179, 229, 252)
    gun= Gun(screen)
    bullets = Group()
    pigs = Group()
    controls.create_army (screen, pigs)
    stats = Stats()
    heart = Heart(screen)
    sc = Scores(screen, stats, heart)




    while True:
        controls.events(screen, gun, bullets)
        if stats.run_game:
             gun.update_gun ()
             """Вызов функции,которая обновляет позицию пушки"""
             bullets.update ()
             controls.update(bg_color, screen,stats, sc, gun, pigs,  bullets)
             controls.update_bullets(screen, stats, sc,  pigs, bullets)
             controls.update_pigs(stats, screen, sc, gun, pigs, bullets)







run()