import pygame.font

class Scoreboard():
    def __init__(self, settings, screen, stats):
        self.screen =screen
        self.screen_rect = screen.get_rect()
        self.settings = settings
        self.stats = stats.score
        if self.settings.startBlanka == True:
            self.background_color = self.settings.blanka_color
        else:
            self.background_color = self.settings.bg_color

        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None, 20)


    def show_score(self, score, best_score, startBlanka):
        if startBlanka == True:
            score_str = 'score: ' + str(score) + '            best score: ' + str(best_score)
        else:
            score_str = str(score)
        self.score_image = self.font.render(score_str, True, self.text_color, self.background_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20
        self.screen.blit(self.score_image, self.score_rect)