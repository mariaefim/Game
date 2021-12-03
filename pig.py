import  pygame

class Pig(pygame.sprite.Sprite):
    """класс одной свинки """

    def __init__(self,screen):
        """инициализируем и задаем начальную позицию обьекта"""
        super(Pig, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images2.0/майн-свинья.png')
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = round(self.rect.x)
        self.y = round(self.rect.y)

    def draw(self):
        """вывод свинки на экран"""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """перемещение свинок"""
        self.y += 0.04
        self.rect.y = self.y