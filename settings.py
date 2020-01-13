class Settings():

    def __init__(self):
        self.startBlanka = True


        if self.startBlanka == True:
            self.game_speed = 0.0001
        else:
            self.game_speed = 0.09

        self.rows = 20
        self.row_width = 20

        if self.startBlanka == True:
            self.blanka_screen_width = self.rows * self.row_width
        else:
            self.blanka_screen_width = 0
        self.blanka_color = (210, 210, 210)

        self.screen_width = self.rows * self.row_width + self.blanka_screen_width
        self.screen_height = self.rows * self.row_width
        self.bg_color = (230, 230, 230)

        self.button_color = (0, 0, 0)
        self.button_text_color = (255,255,255)

