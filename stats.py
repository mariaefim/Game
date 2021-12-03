class Stats():
    """отслеживание статистики"""

    def __init__(self):
        """инициализируем статистику"""
        self.reset_stats()
        self.run_game = True
        with open ('highscore.txt','r')  as f:
        #в каждой новой игре открывает записи прошлых результатови читает их
           self.high_score = int(f.readline())
    def reset_stats(self):
            """статистика изменяющаяся во время игры"""
            self.guns_left = 3
            self.score = 0