import pygame
import time
import random

pygame.init()

win_len =1200
win_h = 600
add_caption = pygame.display.set_mode((win_len,win_h),pygame.FULLSCREEN)

box_len = 1000
box_h = 500

pygame.display.set_caption("SNAKE")

timer = pygame.time.Clock()

snake_block = 10
snake_speed = 10

display_style = pygame.font.SysFont("arial",30,"bold")
score_font = pygame.font.SysFont("arial",45,"bold")

def final_score(score):
    value = score_font.render("Enjoy the game --- Score: "+str(score),True,"yellow")
    add_caption.blit(value,[370,20])

def make_snake(snake_block,list_snake):
    for x in list_snake:
        pygame.draw.rect(add_caption,"white",[x[0],x[1],15,15])

def display_msg1(msg,color):
    mssg = display_style.render(msg,True,color)
    add_caption.blit(mssg,[500,200])

def display_msg2(msg,color):
    mssg = display_style.render(msg,True,color)
    add_caption.blit(mssg,[500,300])

def display_msg3(msg,color):
    mssg = display_style.render(msg,True,color)
    add_caption.blit(mssg,[500,400])

def display_msg4(msg,color):
    mssg = display_style.render(msg,True,color)
    add_caption.blit(mssg,[980,550])

def start_game():
    game_over = False
    game_close = False

    x1 = 600
    y1 = 300 

    new_x1 = 0
    new_y1 = 0

    list_snake = []
    snake_len = 1

    foodx_pos = round(random.randrange(200,box_len-15)/10.0)*10.0
    foody_pos = round(random.randrange(100,box_h-15)/10.0)*10.0

    while not game_over:
        
        while game_close == True:
            add_caption.fill("black")
            display_msg1("YOU LOST","red")
            display_msg2("Press C to play again","white")
            display_msg3("Press ESC to exit","white")
            display_msg4("Created by rbnshj","yellow")
            final_score(snake_len-1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        start_game()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    new_x1 = -snake_block
                    new_y1 = 0
                elif event.key == pygame.K_RIGHT:
                    new_x1 = snake_block
                    new_y1 = 0
                elif event.key == pygame.K_UP:
                    new_y1 = -snake_block
                    new_x1 = 0
                elif event.key == pygame.K_DOWN:
                    new_y1 = snake_block
                    new_x1 = 0

        
        if x1>box_len-15 or x1<200 or y1>box_h-15 or y1<100:
            game_close = True

        x1 += new_x1
        y1 += new_y1
        
        add_caption.fill("black")
        pygame.draw.rect(add_caption,"green",[200,100,800,400])
        pygame.draw.rect(add_caption,"red",[foodx_pos,foody_pos,15,15],border_radius=500)
        name = score_font.render("--- Press any arrow key to START ---",True,"yellow")
        add_caption.blit(name,[310,520])
        
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)

        list_snake.append(snake_head)
        if len(list_snake)>snake_len:
            del list_snake[0]
        for x in list_snake[:-1]:
            if x == snake_head:
                game_close = True

        
        make_snake(snake_block,list_snake)
        final_score(snake_len-1)

        pygame.display.update()

        if x1 == foodx_pos and y1 == foody_pos:
            foodx_pos = round(random.randrange(200,box_len-15)/10.0)*10.0
            foody_pos = round(random.randrange(100,box_h-15)/10.0)*10.0
            snake_len += 1

        timer.tick(snake_speed)

    pygame.quit()

start_game() 