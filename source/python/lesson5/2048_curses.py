import curses
import random
a = 1
qwq = '111'
stdscr = curses.initscr()
curses.start_color()
curses.use_default_colors()

curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_CYAN)
curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_YELLOW)
curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_GREEN)
curses.init_pair(5, curses.COLOR_BLACK, curses.COLOR_MAGENTA)
curses.init_pair(6, curses.COLOR_BLACK, curses.COLOR_RED)
curses.init_pair(7, curses.COLOR_BLACK, curses.COLOR_BLUE)

HEIGHT = 4
WIDTH = 4

game_board = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]

KEY_UP = ord('w')
KEY_DOWN = ord('s')
KEY_LEFT = ord('a')
KEY_RIGHT = ord('d')

color_map = {
    0: 0,
    2: 1,
    4: 2,
    8: 3,
    16: 4,
    32: 5,
    64: 6,
    128: 1,
    256: 2,
    512: 3,
    1024: 4,
    2048: 5
}

def draw_game(stdscr, a):
    stdscr.clear()
    for i in range(HEIGHT):
        for j in range(WIDTH):
            value = game_board[i][j]
            color = color_map[value]
            stdscr.addstr(i*4, j * 20, str(value), curses.color_pair(color))
    height, width = stdscr.getmaxyx()

    if a == 0:
        text = "YOU LOSE! Enter r to replay and enter q to exit"
    else:
        text = "w(up) s(down) a(left) d(right) q(quit)"

    x = (width - len(text)) // 2
    y = height - 1

    stdscr.addstr(8*4, 1*20, text)

    stdscr.refresh()

def is_game_over():
    for i in range(HEIGHT):
        for j in range(WIDTH):
            if game_board[i][j] == 0:
                return False                   
    return True

def generate_number():
    if is_game_over():
        a = 0
        return a
    while True:
        row = random.randint(0, HEIGHT - 1)
        col = random.randint(0, WIDTH - 1)
        if game_board[row][col] == 0:
            game_board[row][col] = random.choice([2, 4])
            break
    return 1

def handle_key_event(key):
    if key == KEY_UP:
        move_up()
    elif key == KEY_DOWN:
        move_down()
    elif key == KEY_LEFT:
        move_left()
    elif key == KEY_RIGHT:
        move_right()

def move_up():
    for j in range(WIDTH):
        for i in range(1, HEIGHT):
            if game_board[i][j] != 0:
                k = i
                while k > 0 and game_board[k - 1][j] == 0:
                    game_board[k - 1][j] = game_board[k][j]
                    game_board[k][j] = 0
                    k -= 1
                if k > 0 and game_board[k - 1][j] == game_board[k][j]:
                    game_board[k - 1][j] *= 2
                    game_board[k][j] = 0

def move_down():
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
                    game_board[k][j] = 0

def move_left():
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
                    game_board[i][k] = 0

def move_right():
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
                    game_board[i][k] = 0

def main(stdscr):
    while True:
        generate_number()
        generate_number()
        draw_game(stdscr, 1)
        
        while True:
            key = stdscr.getch()
            if key == ord('q'):
                qwq = 'quit'
                break
            if key == ord('r'):
                for i in range(HEIGHT):
                    for j in range(WIDTH):
                        game_board[i][j] = 0
                qwq = '111'
                break
            if key == ord('w') or key == ord('s') or key == ord('a') or key == ord('d'):
                handle_key_event(key)
                b = generate_number()
                draw_game(stdscr, b)
        if qwq == 'quit':
            return
            
curses.wrapper(main)
