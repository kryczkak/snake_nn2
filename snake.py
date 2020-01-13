import pygame


class Snake(object):
    long_body = [[0, 0], [1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0], [10, 0], [11, 0],
                 [12, 0], [13, 0], [14, 0], [15, 0], [16, 0], [17, 0], [18, 0], [19, 0],
                 [19, 1], [18, 1], [17, 1], [16, 1], [15, 1], [14, 1], [13, 1], [12, 1], [11, 1], [10, 1], [9, 1],
                 [8, 1], [7, 1], [6, 1], [5, 1], [4, 1], [3, 1], [2, 1], [1, 1], [0, 1],
                 [19, 2], [18, 2], [17, 2], [16, 2], [15, 2], [14, 2], [13, 2], [12, 2], [11, 2], [10, 2], [9, 2],
                 [8, 2], [7, 2], [6, 2], [5, 2], [4, 2], [3, 2], [2, 2], [1, 2], [0, 2],
                 [0, 3]]
    short_body = [[0, 0], [1, 0]]
    body_color = [0,0,0]
    direction = [1,0]

    body = short_body

    def __init__(self, body, body_color, direction):
        self.body = body
        self.body_color = body_color
        self.direction = direction


    def move(self, keys, blanka_dir_x = -5, blanka_dir_y = -5):


        if blanka_dir_x != - 5:
            self.direction[0] = blanka_dir_x
            self.direction[1] = blanka_dir_y
        else:
            for key in keys:
                if keys[pygame.K_LEFT]:
                    if not (self.direction[0] == 1 and self.direction[1] == 0):
                        self.direction[0] = -1
                        self.direction[1] = 0

                if keys[pygame.K_RIGHT]:
                    if not (self.direction[0] == -1 and self.direction[1] == 0):
                        self.direction[0] = 1
                        self.direction[1] = 0

                if keys[pygame.K_UP]:
                    if not (self.direction[0] == 0 and self.direction[1] == 1):
                        self.direction[0] = 0
                        self.direction[1] = -1

                if keys[pygame.K_DOWN]:
                    if not (self.direction[0] == 0 and self.direction[1] == -1):
                        self.direction[0] = 0
                        self.direction[1] = 1


        head = self.body[-1]

        self.body.append([head [0] + self.direction [0], head [1] + self.direction [1]])
        self.body.pop(0)


    def check_snak_eaten(self, pos_x, pos_y):
        head = self.body[-1]
        eaten = False
        if head[0] == pos_x and head[1] == pos_y:
            eaten = True

        return eaten



    def grow_snake(self, pos_x, pos_y):
        self.body.append([pos_x, pos_y])



    def check_colisions(self, row_num):
        head = self.body[-1]
        clash = False

        if head[0] <0 or head[0] > row_num -1:
            clash = True

        if head[1] <0 or head[1] > row_num -1:
            clash = True

        for cube in self.body[0:-2]:
            if cube[0] == head[0] and cube[1] == head[1]:
                clash = True

        return clash



    def reset_life(self):
        long_body = [[0,0],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[9,0],[10,0],[11,0],[12,0],[13,0],[14,0],[15,0],[16,0],[17,0],[18,0],[19,0],
                     [19,1],[18,1],[17,1],[16,1],[15,1],[14,1],[13,1],[12,1],[11,1],[10,1],[9,1],[8,1],[7,1],[6,1],[5,1],[4,1],[3,1],[2,1],[1,1],[0,1],
                     [19,2],[18,2],[17,2],[16,2],[15,2],[14,2],[13,2],[12,2],[11,2],[10,2],[9,2],[8,2],[7,2],[6,2],[5,2],[4,2],[3,2],[2,2],[1,2],[0,2],
                     [0,3]]
        short_body = [[0,0],[1,0]]
        self.body =  short_body
        self.direction = [1,0]
