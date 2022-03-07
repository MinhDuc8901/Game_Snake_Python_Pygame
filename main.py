from tabnanny import check
import pygame
import time
from random import randint

pygame.init()
screen = pygame.display.set_mode((601,660))
pygame.display.set_caption("Trò chơi con rắn")
clock = pygame.time.Clock()
running = True

#color 
GREEN = (0,200,0)
BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)

snakes = [[0,0],[0,1],[0,2],[0,3],[0,4],[0,5]]
direction = 'right'
flie = [randint(0,19),randint(0,19)]
total = 0
count = 0
check = True
checkover = True
# font 
font = pygame.font.SysFont('sans',30)
# sound 
sound = pygame.mixer.Sound('music.mp3')
pygame.mixer.Sound.play(sound)


while running : 
    clock.tick(60)
    screen.fill(BLACK)

    #draw line 
    for i in range(21):
        pygame.draw.line(screen,WHITE,(0,i*30),(600,i*30))
        pygame.draw.line(screen,WHITE,(i*30,0),(i*30,600))
    
    flies = pygame.draw.rect(screen,RED,(flie[0]*30,flie[1]*30,30,30))

    
    for snake in snakes:
        snake_act = pygame.draw.rect(screen,GREEN,(snake[0]*30,snake[1]*30,30,30))
        if snake_act.colliderect(flies):
            flie = [randint(0,19),randint(0,19)]
            if direction == 'right':
                snakes.append([int(snakes[-1][0])+1,int(snakes[-1][1])])
                count+=1
                total+=1
            elif direction == 'left':
                snakes.append([int(snakes[-1][0])-1,int(snakes[-1][1])])
                count+=1
                total+=1
            elif direction == 'up':
                snakes.append([int(snakes[-1][0]),int(snakes[-1][1])-1])
                count+=1
                total+=1
            else: 
                snakes.append([int(snakes[-1][0]),int(snakes[-1][1])+1])
                count+=1
                total+=1
    
    snake_head = pygame.draw.rect(screen,GREEN,(snakes[-1][0]*30,snakes[-1][1]*30,30,30))
    
    for i in range(len(snakes)-2):
        snake_act = pygame.draw.rect(screen,GREEN,(snakes[i][0]*30,snakes[i][1]*30,30,30))
        if snake_act.colliderect(snake_head):
            game_over_txt = font.render('GAME OVER '+str(total),True,RED)
            screen.blit(game_over_txt,(270,270))
            check = False
            pygame.mixer.pause()
            checkover = False

    
    

    total_txt = font.render('Score: '+str(total),True,WHITE)
    screen.blit(total_txt,(30,615))
    

    # run snakes
    if check:
        if direction == 'right':
            snakes.append([int(snakes[-1][0])+1,int(snakes[-1][1])])
            snakes.pop(0)
        elif direction == 'left':
            snakes.append([int(snakes[-1][0])-1,int(snakes[-1][1])])
            snakes.pop(0)
        elif direction == 'up':
            snakes.append([int(snakes[-1][0]),int(snakes[-1][1])-1])
            snakes.pop(0)
        else: 
            snakes.append([int(snakes[-1][0]),int(snakes[-1][1])+1])
            snakes.pop(0)

    time.sleep(0.1)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction!='down':
                direction = 'up'
            if event.key == pygame.K_DOWN and direction!='up':
                direction = 'down'
            if event.key == pygame.K_RIGHT and direction != 'left':
                direction = 'right'
            if event.key == pygame.K_LEFT and direction != 'right':
                direction = 'left'
            if event.key == pygame.K_SPACE:
                if checkover == False:
                    pygame.mixer.Sound.play(sound)
                    snakes = [[0,0],[0,1]]
                    check = True
                    total =0
                    checkover = True
                else:
                    check = False if check else True
                    if check == False : 
                        pygame.mixer.pause()
                    else : pygame.mixer.unpause()


        if event.type == pygame.QUIT:
            running = False
    
    if snakes[-1][0] >= 19: 
        snakes.append([0,int(snakes[-1][1])])
        snakes.pop(0)
    if snakes[-1][1] >= 19 : 
        snakes.append([int(snakes[-1][0]),0])
        snakes.pop(0)
    if snakes[-1][1] == -1 : 
        snakes.append([int(snakes[-1][0]),19])
        snakes.pop(0)
    if snakes[-1][0] == -1 : 
        snakes.append([19,int(snakes[-1][1])])
        snakes.pop(0)
    

    pygame.display.flip()
pygame.quit()

