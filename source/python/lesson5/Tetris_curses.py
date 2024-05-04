import curses, time
import random

HEIGHT = 20
WIDTH = 10

SHAPES = [
    [[1, 1, 1, 1]],
    [[1, 1], [1, 1]],
    [[1,1, 0], [0, 1, 1]],
    [[0, 1, 1], [1, 1, 0]],
    [[1, 1, 1], [0, 1, 0]],
    [[1, 1, 1], [1, 0, 0]],
    [[1, 1, 1], [0, 0, 1]]
]
COLORS = [curses.COLOR_BLUE, curses.COLOR_CYAN, curses.COLOR_GREEN,
          curses.COLOR_MAGENTA, curses.COLOR_RED, curses.COLOR_YELLOW,
          curses.COLOR_WHITE]

def create_block():
    shape = random.choice(SHAPES)
    color = random.choice(COLORS)
    return shape, color

def draw_block(window, y, x, shape, color):
    window.attron(curses.color_pair(color))
    for i in range(len(shape)):
        for j in range(len(shape[i])):
            if shape[i][j] == 1:
                window.addstr(y + i, x + j * 2, '  ')
    window.attroff(curses.color_pair(color))


#def check_collision(board, shape, x, y):
def check_collision(board, shape, x, y):
    rows = HEIGHT
    cols = WIDTH

    for i in range(len(shape)):
        for j in range(len(shape[i])):
            if shape[i][j] != 0:
                row = x + i
                col = y + j
                if row < 0 or row >= rows or col < 0 or col >= cols:
                    return True
                if board[row][col] != 0:
                    return True

    return False


def fix_block(field, shape, y, x):
    for i in range(len(shape)):
        for j in range(len(shape[i])):
            if shape[i][j] == 1:
                field[y + i][x + j] = 1

def clear_lines(field):
    lines_cleared = 0
    for i in range(HEIGHT):
        if all(field[i]):
            del field[i]
            field.insert(0, [0 for _ in range(WIDTH)])
            lines_cleared += 1
    return lines_cleared

def main(stdscr):
      
    #window = curses.newwin(HEIGHT + 2, WIDTH * 2 + 2, (curses.LINES - HEIGHT) // 2 - 1, (curses.COLS - WIDTH * 2) // 2 - 1)
    #window.border()

    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(800)
    qwq = 0

    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_BLUE)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_CYAN)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_GREEN)
    curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_MAGENTA)
    curses.init_pair(5, curses.COLOR_BLACK, curses.COLOR_RED)
    curses.init_pair(6, curses.COLOR_BLACK, curses.COLOR_YELLOW)
    curses.init_pair(7, curses.COLOR_BLACK, curses.COLOR_WHITE)

    window = curses.newwin(HEIGHT + 2, WIDTH * 2 + 2, (curses.LINES - HEIGHT) // 2 - 1, (curses.COLS - WIDTH * 2) // 2 - 1)
    window.border()
    
    y, x = (curses.LINES - HEIGHT) // 2 - 1, (curses.COLS - WIDTH * 2) // 2 - 1

    right_height, right_width = 5, 22
    right_y, right_x = y - 5, x
    right_win = curses.newwin(right_height, right_width, right_y, right_x)
    

    field = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]
    shape, color = create_block()
    shape_next, color_next = create_block()
    y, x = 0, WIDTH // 2 - len(shape) // 2

    win_width = right_win.getmaxyx()
    

    while True:
        for i in range(HEIGHT):
            for j in range(WIDTH):
                if field[i][j] == 0:
                    window.addstr(i + 1, j * 2 + 1, '  ')
                else:
                    window.attron(curses.color_pair(field[i][j]))
                    window.addstr(i + 1, j * 2 + 1, '  ')
                    window.attroff(curses.color_pair(field[i][j]))

        draw_block(window, y + 1, x * 2 + 1, shape, color)

        key = stdscr.getch()
        if key == ord('q'):
            break
        if key == curses.KEY_LEFT and not check_collision(field, shape, y, x - 1):
            x -= 1
        elif key == curses.KEY_RIGHT and not check_collision(field, shape, y, x + 1):
            x += 1
        elif key == curses.KEY_DOWN and not check_collision(field, shape, y + 1, x):
            y += 1
        elif key == curses.KEY_UP:
            rotated_shape = list(zip(*reversed(shape)))
            if not check_collision(field, rotated_shape, y, x):
                shape = rotated_shape

        if not check_collision(field, shape, y + 1, x):
            y += 1
        else:
            fix_block(field, shape, y, x)
            lines_cleared = clear_lines(field)
            window.addstr(0, 2, f"Score: {lines_cleared}")
            shape, color = shape_next, color_next
            shape_next, color_next = create_block()
            y, x = 0, WIDTH // 2 - len(shape) // 2
            if check_collision(field, shape, y, x):
                break
        right_win.border()
        right_win.addstr(1, 2, "Next:")
        right_win.addstr(4, 2, "←,↑,→,↓ or q")
        draw_block(right_win,  2, 10, shape_next, color_next)
        
        window.refresh()
        right_win.refresh()
        right_win.clear()
        
    stdscr.addstr(curses.LINES // 2, (curses.COLS - 9) // 2, "Game Over")
    stdscr.refresh()
    stdscr.getch()

if __name__ == "__main__":
    curses.wrapper(main)
