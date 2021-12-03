import pygame, sys
from bullet import  Bullet
from pig import Pig
import time
from heart import Heart


def events(screen, gun,bullets):
    """обработка событий"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                """при нажатии стрелки двигается вправо"""
                gun.moveright = True
            elif event.key == pygame.K_LEFT:
                gun.moveleft = True
            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                gun.moveright = False
                """при отжатии клавиши движения не происходит"""
            elif event.key == pygame.K_LEFT:
                gun.moveleft = False
def update (bg_color, screen,stats, sc,  gun, pigs,  bullets):
    """обновление экрана"""
    screen.fill(bg_color)
    sc.show_score()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    gun.output()
    pigs.draw(screen)
    pygame.display.flip()

def update_bullets(screen, stats, sc,  pigs, bullets):
    """обновление позиций пуль"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collisions = pygame.sprite.groupcollide(bullets, pigs, True, True)
    if collisions:
        stats.score += 1    #увеличиваем счет на единицу
        sc.image_score()
    #столкневение пули с объектом
        check_high_score(stats, sc)
        sc.image_hearts()
    if len(pigs) == 0:
        """рассматриваем случай когда мы полностью уничтожили свинок"""
        bullets.empty()
        create_army(screen, pigs)

def gun_kill(stats, screen, gun, pigs, bullets):
    """столконовение пушки и свинок"""
    if stats.guns_left > 0:
        stats.guns_left -= 1
        pigs.empty()
        bullets.empty()
        create_army(screen, pigs)
        gun.create_gun()
        time.sleep(0.5)
    else:
        stats.run_game = False
        sys.exit()

def update_pigs(stats, screen, sc, gun, pigs, bullets):
    """обновление позиций свинок"""
    pigs.update()
    if pygame.sprite.spritecollideany(gun, pigs):
        # момент столкновения объекта с пушкой
        gun_kill(stats, screen , gun, pigs, bullets)
    pigs_check(stats, screen, sc, gun, pigs, bullets)


def pigs_check (stats, screen, sc, gun, pigs, bullets):
    """проверка добрались ли свинки до конца карты"""
    screen_rect = screen.get_rect()
    for pig in pigs.sprites():
        if pig.rect.bottom >= screen_rect.bottom:
            gun_kill(stats, screen  , gun, pigs, bullets)
            break





def create_army(screen, pigs):
    """создание армии свинок"""
    pig = Pig(screen)
    pig_width = pig.rect.width
    number_pig_x = int((1000- 2*pig_width)/pig_width)
    pig_height = pig.rect.height
    number_pig_y = 3

    for row_number in range(number_pig_y):
         for pig_number in range (number_pig_x):
            pig = Pig(screen)
            pig.x = pig_width +  (pig_width*2.4) * pig_number
            pig.y = pig_height + pig_height *(2 * row_number)
            pig.rect.x=pig.x
            pig.rect.y = pig.rect.height + 2 * pig.rect.height * row_number
            pigs.add(pig)

def check_high_score (stats, sc):
    """проверка новых рекордов"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sc.image_high_score()
        with open ('highscore.txt', 'w') as f:
            #открываем файл в режиме записи
            f.write(str(stats.high_score))


















