import sys
import pygame
from numpy import sign
from time import sleep
from random import randint
from button import Button

from settings import Settings
from snake import Snake
from scoreboard import Scoreboard
from stats import Stats

from blanka import Blanka


def draw_snake(surface, color, body, row_width):
    for cube in body:
        pygame.draw.rect(surface, color, (cube[0]*row_width, cube[1]*row_width,row_width,row_width))

def draw_snak(surface, color, pos_x, pos_y, row_width):
    pygame.draw.rect(surface, color, (pos_x * row_width, pos_y * row_width, row_width, row_width))

def draw_blanka_stats(surface, color, pos_x, pos_y, width, height):
    pygame.draw.rect(surface, color, (pos_x, pos_y, width, height))

def draw_outside_ring(surface, color, pos_x, pos_y, width, height):
    pygame.draw.rect(surface, color, (pos_x, pos_y, width, height))

def draw_blanka_neurons(surface, activations, node_size, node_inc_x, node_inc_y, screen_x):
    pos_x = screen_x
    for x in activations.values(): #layer
        pos_x = pos_x + node_inc_x
        pos_y = 10
        for y in x:                #
            for j in y:            #node
                pos_y = pos_y + node_inc_y
                color = min(int(j * 225), 225)
                pygame.draw.rect(surface,(0,color,0),(pos_x,pos_y,node_size,node_size))
                #pygame.draw.circle(surface,(0,color,0),(pos_x, pos_y),node_size)

def draw_blanka_weights(surface, weights, node_size, node_inc_x, node_inc_y, screen_x):
    x = screen_x + node_size + 1
    for layer in weights:
        x = x + node_inc_x
        y = 10 + round(node_size /2,0)
        for node_in in layer:
            y = y + node_inc_y
            pos_start = (x,y)
            y_node_out = 10 + round(node_size /2,0)
            for node_out in node_in:
                y_node_out = y_node_out + node_inc_y
                pos_end = (x + node_inc_x - node_size -2, y_node_out)
                node_out_abs = min(abs(node_out)*250,250)
                if node_out > 0:
                    color = (0,0,node_out_abs)
                else:
                    color = (node_out_abs,0,0)
                pygame.draw.line(surface, color, pos_start, pos_end,1)




def randomize_snak_position(body, max_range):
    finished = False
    while not finished:
        pos_x = randint(0,max_range-1)
        pos_y = randint(0,max_range-1)

        body_colisions = 0
        for cube in body:
            if cube[0] == pos_x and cube[1] == pos_y:
                body_colisions += 1
        if body_colisions == 0:
            finished = True

    return pos_x, pos_y


def check_play_button(play_button, mouse_x, mouse_y):
    game_state = False
    if play_button.rect.collidepoint(mouse_x, mouse_y):
        game_state = True

    return game_state


def run_game():
    pygame.init()
    snake = Snake
    snake_settings = Settings()
    startBlanka = snake_settings.startBlanka

    if startBlanka:
        blanka = Blanka()
        blanka.create_model()

    screen = pygame.display.set_mode((snake_settings.screen_width, snake_settings.screen_height))

    play_button = Button(snake_settings, screen, "Pause")
    pygame.display.set_caption ("Snake")
    pos_x, pos_y = randomize_snak_position(snake.body,snake_settings.rows)

    old_dir_x, old_dir_y = snake.direction[0], snake.direction[1]
    stats = Stats(pos_x,pos_y,
                  1, 0,
                  snake.direction[0], snake.direction[1],
                  snake.body, snake_settings.rows,
                  'r'
                  )
    scoreboard = Scoreboard(snake_settings, screen, stats)

    game_state_active = False
    pygame.mouse.set_visible(True)


    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                blanka.clear_model()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                game_state_active = check_play_button(play_button, mouse_x, mouse_y)

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if game_state_active:
                        game_state_active = False
                    else:
                        game_state_active = True


        screen.fill(snake_settings.bg_color)

        if game_state_active:
            pygame.mouse.set_visible(False)
            keys = pygame.key.get_pressed()

            if startBlanka:
                head = snake.body[-1]
                tail = snake.body[0]
                new_x, new_y= blanka.chose_dir(
                    [
                    sign(pos_x - head[0])
                    ,sign(pos_y - head[1])
                    ,stats.count_distanses(snake.body,snake_settings.rows,'r')
                    ,stats.count_distanses(snake.body, snake_settings.rows, 'l')
                    ,stats.count_distanses(snake.body,snake_settings.rows,'u')
                    ,stats.count_distanses(snake.body, snake_settings.rows, 'd')
                    #,(tail[0] - head[0]) / snake_settings.rows
                    #,(tail[1] - head[1]) / snake_settings.rows
                    ]
                )
            else:
                 new_x, new_y = -5, -5
            head = snake.body[-1]
            stats.set_stats(pos_x, pos_y, head[0], head[1], snake.body, snake_settings.rows)
            snake.move(snake, keys,new_x, new_y)
            stats.set_dir(snake.direction[0], snake.direction[1])

            #draw_outside_ring(screen,(200,200,200)
             #                 ,snake_settings.row_width
             #                 ,snake_settings.row_width
             #                 ,(snake_settings.rows - 2) * snake_settings.row_width
             #                 ,(snake_settings.rows - 2) * snake_settings.row_width)

            draw_snake(screen, snake.body_color, snake.body, snake_settings.row_width)
            draw_snak(screen,snake.body_color,pos_x, pos_y,snake_settings.row_width)
            if startBlanka == True:
                draw_blanka_stats(screen,snake_settings.blanka_color, snake_settings.rows*snake_settings.row_width,0
                                  ,snake_settings.blanka_screen_width,snake_settings.rows*snake_settings.row_width)
                draw_blanka_neurons(screen, blanka.neurons_ativations, 18, 53, 40, snake_settings.blanka_screen_width)
                draw_blanka_weights(screen, blanka.weights, 18, 53, 40, snake_settings.blanka_screen_width)

            if snake.check_snak_eaten(snake, pos_x, pos_y):
                snake.grow_snake(snake,pos_x,pos_y)
                pos_x, pos_y = randomize_snak_position(snake.body, snake_settings.rows)
                stats.increase_score()

            scoreboard.show_score(stats.score, stats.best_score, startBlanka)

            if snake.check_colisions(snake, snake_settings.rows):
                snake.reset_life(snake)
                stats.reset_score()
                pos_x, pos_y = randomize_snak_position(snake.body, snake_settings.rows)
                game_state_active = False




            if not startBlanka:
                stats.save_stats_to_file('statsJ.csv')


            old_dir_x = snake.direction[0]
            old_dir_y = snake.direction[1]
        else:
            play_button.draw_button()
            pygame.mouse.set_visible(True)
            if startBlanka == True:
                stats.save_stats_to_file('blanka_game_recoeds.csv')
                game_state_active =  True

        pygame.display.flip()
        sleep(snake_settings.game_speed/2)

run_game()