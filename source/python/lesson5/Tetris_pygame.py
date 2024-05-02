import pygame, sys
import random

all_block = [
    [[0, 0], [0, 1], [0, 2], [0, 3], ],
    [[0, 0], [0, 1], [1, 0], [1, 1], ],
    [[0, 0], [1, 0], [0, 1], [0, 2], ],
    [[0, 0], [0, 1], [0, -1], [0, -2], ],
    [[0, 0], [0, 1], [1, 1], [1, 2], ],  
    [[0, 0], [0, -1], [1, -1], [1, -2], ],
    [[0, 0], [0, 1], [0, -1], [1, 0]],    
]

backgroud = [[0 for column in range(0, 10)] for row in range(0, 23)]
backgroud[0] = [1 for colum in range(0, 10)]

initial_position = [21, 5]
times = 0  
score = [0]

gameover = []

press = False

pygame.init()
screen = pygame.display.set_mode((400, 800))
select_block = list(random.choice(all_block))


def block_down():
    global select_block    
    y, x = initial_position
    y -= 1 
    for row, column in select_block:
        row += y
        column += x
        if backgroud[row][column]:
            break
    else:
        initial_position.clear()       
        initial_position.extend([y, x])
        return
    y, x = initial_position
    for row, column in select_block:
        row += y
        column += x
        backgroud[row][column] = 1 
    complete_row = []

    for row in range(1, 21): 
        if 0 not in backgroud[row]: 
            complete_row.append(row)
    for row in complete_row:
        backgroud.pop(row)  
        backgroud.append(list(0 for _ in range(0, 10))) 
    score[0] += len(complete_row)
    initial_position.clear()  
    select_block = list(random.choice(all_block))
    initial_position.extend(select_block)
    initial_position.clear()
    initial_position.extend([20, 5])
    y, x = initial_position
    for row, column in select_block:
        row += y
        column += x
        if backgroud[row][column] == 1:
            gameover.append(1)

def draw_block():
    y, x = initial_position
    for row, column in select_block:
        row += y
        column += x
        pygame.draw.rect(screen, (255, 165, 0), (column * 40, 800 - row * 40, 38, 38))
    for row in range(1, 21):
        for column in range(0, 10):
            if backgroud[row][column] == 1:
                pygame.draw.rect(screen, (0, 0, 255), (column * 40, 800 - row * 40, 38, 38))


def rotate():
    y, x = initial_position
    rotating_position = [(-colum, row) for row, colum in select_block]
    for row, colum in rotating_position:
        row += y
        colum += x
        if colum < 0 or colum > 9 or backgroud[row][colum]:
            break
    else:
        select_block.clear()
        select_block.extend(rotating_position)


def move(d):
    y, x = initial_position
    # select_block = list(random.choice(all_block))
    x += d
    for row, colum in select_block:
        row += y
        colum += x
        if colum < 0 or colum > 9 or backgroud[row][colum]:
            break
    else:
        initial_position.clear()
        initial_position.extend([y, x])


while True:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                press = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                rotate()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    move(1)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    move(-1)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                times = 60
        if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    sys.exit()

    if times % 60 == 0:
        block_down()
    times += 1
    if gameover:
        sys.exit()
    draw_block()
    pygame.time.Clock().tick(400)
    font = pygame.font.Font(None, 36)
    text = font.render("Score: " + str(score[0]), True, (0, 0, 0))
    text_controls1 = font.render("(up)Rotate, (left/right)Move,", True, (0, 0, 0))
    text_controls2 = font.render("(down)Accelerate, (q)Quit", True, (0, 0, 0))
    screen.blit(text, (10, 10))
    screen.blit(text_controls1, (10, 40))
    screen.blit(text_controls2, (10, 70))
    pygame.display.update()

    pygame.display.flip()
