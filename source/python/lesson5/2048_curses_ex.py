#!/usr/bin/env python3
import curses
import random
qwq = '111'
score = 0
stdscr = curses.initscr()
curses.start_color()
curses.use_default_colors()
#curses.init_pair(0, curses.COLOR_BLACK, curses.COLOR_WHITE)
curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_CYAN)
curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_YELLOW)
curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_GREEN)
curses.init_pair(5, curses.COLOR_BLACK, curses.COLOR_MAGENTA)
curses.init_pair(6, curses.COLOR_BLACK, curses.COLOR_RED)
curses.init_pair(7, curses.COLOR_BLACK, curses.COLOR_BLUE)

HEIGHT = 4
WIDTH = 4
HEIGHT_block = 3
WIDTH_block = 8
game_board = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]

color_map = {
    0: 1,
    2: 2,
    4: 3,
    8: 4,
    16: 5,
    32: 6,
    64: 7,
    128: 2,
    256: 3,
    512: 4,
    1024: 5,
    2048: 6
}

def divide_by_two(num):
    if num % 2 == 0:
        result = num / 2
    else:
        result = (num + 1) / 2
    return result

def draw_game(stdscr, a):
    stdscr.clear()
    curses.curs_set(0)
    HEIGHT_block_centre = 1
    WIDTH_block_centre = 4
    for i in range(HEIGHT):
        for j in range(WIDTH):
            value = game_board[i][j]
            color = color_map[value]
            bit = len(str(value)) - 1
            if bit == 2 or bit == 3:
                bit = bit - 1
            for q in range(HEIGHT_block):
                if q == HEIGHT_block_centre:
                        if value == 0:
                            stdscr.addstr(q+i*HEIGHT_block, j*WIDTH_block, '    .'.ljust(int(WIDTH_block)), curses.color_pair(color))
                        else:
                            stdscr.addstr(q+i*HEIGHT_block, j*WIDTH_block, ' '.ljust(int(WIDTH_block_centre-bit)), curses.color_pair(color))
                            stdscr.addstr(q+i*HEIGHT_block, j*WIDTH_block+int(WIDTH_block_centre)-bit, str(int(value)).ljust(int(WIDTH_block_centre+bit)), curses.color_pair(color))
                else:
                    stdscr.addstr(q+i*HEIGHT_block, j*WIDTH_block, ' '.ljust(WIDTH_block), curses.color_pair(color))
                #for c in range(WIDTH_block):
                     
                     #stdscr.addstr(q, c, ' ', curses.color_pair(color))
                     
                    
    height, width = stdscr.getmaxyx()

    if a == 0:
        text = "YOU LOSE! Enter r to replay and enter q to exit"
    if a == 1:
        text = "w(up) s(down) a(left) d(right) q(quit) r(restart)"
    if a == 2:
        text = "YOU WIN! Enter r to replay and enter q to exit"
    x = (width - len(text)) // 2
    y = height - 1

    stdscr.addstr(int(HEIGHT_block*4+2), int(WIDTH_block_centre), text)
    stdscr.addstr(0, int(WIDTH_block*4 + 4), f"Score: {score}")
    stdscr.refresh()

def can_move(board):
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                return True
            if i > 0 and board[i][j] == board[i-1][j]:
                return True
            if i < 3 and board[i][j] == board[i+1][j]:
                return True
            if j > 0 and board[i][j] == board[i][j-1]:
                return True
            if j < 3 and board[i][j] == board[i][j+1]:
                return True
    return False

def can_move_up(board):
    for col in range(len(board)):
        for row in range(1, len(board)):
            if board[row][col] != 0 and (board[row-1][col] == 0 or board[row-1][col] == board[row][col]):
                return True
    return False

def can_move_down(board):
    for col in range(len(board)):
        for row in range(len(board)-2, -1, -1):
            if board[row][col] != 0 and (board[row+1][col] == 0 or board[row+1][col] == board[row][col]):
                return True
    return False

def can_move_left(board):
    for row in range(len(board)):
        for col in range(1, len(board)):
            if board[row][col] != 0 and (board[row][col-1] == 0 or board[row][col-1] == board[row][col]):
                return True
    return False

def can_move_right(board):
    for row in range(len(board)):
        for col in range(len(board)-2, -1, -1):
            if board[row][col] != 0 and (board[row][col+1] == 0 or board[row][col+1] == board[row][col]):
                return True
    return False         

def check_game_over(board):
    for row in board:
        if 0 in row:
            return False

    for i in range(len(board)):
        for j in range(len(board[i])):
            if i < len(board) - 1 and board[i][j] == board[i+1][j]:
                return False
            if j < len(board[i]) - 1 and board[i][j] == board[i][j+1]:
                return False

    return True

def check_win(board):
    for row in board:
        if 2048 in row:
            return True
    return False

def generate_number():
    while True:
        row = random.randint(0, HEIGHT - 1)
        col = random.randint(0, WIDTH - 1)
        if game_board[row][col] == 0:
            game_board[row][col] = random.choice([2, 4])
            break

def handle_key_event(key):
    if key == ord('w'):
        move_up()
    elif key == ord('s'):
        move_down()
    elif key == ord('a'):
        move_left()
    elif key == ord('d'):
        move_right()

def move_up():
    global score
    for j in range(WIDTH):
        for i in range(1, HEIGHT):
            if game_board[i][j] != 0:
                k = i
                while k > 0 and game_board[k - 1][j] == 0:
                    game_board[k - 1][j] = game_board[k][j]
                    game_board[k][j] = 0
                    score += game_board[i][k]
                    k -= 1
                if k > 0 and game_board[k - 1][j] == game_board[k][j]:
                    game_board[k - 1][j] *= 2
                    score += game_board[i][k]
                    game_board[k][j] = 0

def move_down():
    global score
    for j in range(WIDTH):
        for i in range(HEIGHT - 2, -1, -1):
            if game_board[i][j] != 0:
                k = i
                while k < HEIGHT - 1 and game_board[k + 1][j] == 0:
                    game_board[k + 1][j] = game_board[k][j]
                    game_board[k][j] = 0
                    k += 1
                if k < HEIGHT - 1 and game_board[k + 1][j] == game_board[k][j]:
                    game_board[k + 1][j] *= 2
                    score += game_board[i][k]
                    game_board[k][j] = 0

def move_left():
    global score
    for i in range(HEIGHT):
        for j in range(1, WIDTH):
            if game_board[i][j] != 0:
                k = j
                while k > 0 and game_board[i][k - 1] == 0:
                    game_board[i][k - 1] = game_board[i][k]
                    game_board[i][k] = 0
                    k -= 1
                if k > 0 and game_board[i][k - 1] == game_board[i][k]:
                    game_board[i][k - 1] *= 2
                    score += game_board[i][k]
                    game_board[i][k] = 0

def move_right():
    global score
    for i in range(HEIGHT):
        for j in range(WIDTH - 2, -1, -1):
            if game_board[i][j] != 0:
                k = j
                while k < WIDTH - 1 and game_board[i][k + 1] == 0:
                    game_board[i][k + 1] = game_board[i][k]
                    game_board[i][k] = 0
                    k += 1
                if k < WIDTH - 1 and game_board[i][k + 1] == game_board[i][k]:
                    game_board[i][k + 1] *= 2
                    score += game_board[i][k]
                    game_board[i][k] = 0

def main(stdscr):
    global score
    while True:
        generate_number()
        generate_number()
        draw_game(stdscr, 1)
        
        while True:
            a = 1
            if check_game_over(game_board):
                a = 0
                draw_game(stdscr, a)
            if check_win(game_board):
                a = 2
                draw_game(stdscr, a)
            key = stdscr.getch()
            if key == curses.KEY_UP:
                key = ord('w')
            elif key == curses.KEY_DOWN:
                key = ord('s')
            elif key == curses.KEY_LEFT:
                key = ord('a')
            elif key == curses.KEY_RIGHT:
                key = ord('d')
                
            if key == ord('q'):
                qwq = 'quit'
                break
            if key == ord('r'):
                score = 0
                for i in range(HEIGHT):
                    for j in range(WIDTH):
                        game_board[i][j] = 0
                qwq = '111'
                break
            if key == ord('w') or key == ord('s') or key == ord('a') or key == ord('d'):
                if key == ord('w'):
                    #can_move_up(game_board);
                    if not can_move_up(game_board):
                        continue
                if key == ord('s'):
                    #can_move_down(game_board);
                    if not can_move_down(game_board):
                        continue
                if key == ord('a'):
                    #can_move_left(game_board);
                    if not can_move_left(game_board):
                        continue
                if key == ord('d'):
                    if not can_move_right(game_board):
                        continue
                handle_key_event(key)
                generate_number()
                draw_game(stdscr, a)
        if qwq == 'quit':
            return
            
curses.wrapper(main)
