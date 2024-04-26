import random

def get_user_input(function, error):
    while True:
        try:
            user_input = int(input(function))
            if user_input <= 0:
                print(error)
            else:
                return user_input
        except ValueError:
            print(error)

grid = [[0 for _ in range(4)] for _ in range(4)]

def generate_new_tile():
    available_cells = []
    for i in range(4):
        for j in range(4):
            if grid[i][j] == 0:
                available_cells.append((i, j))
    if available_cells:
        x, y = random.choice(available_cells)
        grid[x][y] = random.choice([2, 4])

def print_grid():
    for i in range(4):
        for j in range(4):
            print('{:6d}'.format(grid[i][j]), end='\t')
        print()
    print()

def move(direction):
    if direction.lower() == 'a':
        for i in range(4):
            data = [cell for cell in grid[i] if cell != 0]
            for idx,p in enumerate(data[1:], 1):
                if p == data[idx - 1]:
                    data[idx - 1]= p * 2
                    data[idx]=0
            data = [cell for cell in data if cell != 0]
            data+= [0] * (4 - len(data))
            grid[i] = data
    elif direction.lower() == 'd':
        for i in range(4):
            data = [cell for cell in grid[i] if cell != 0][::-1]
            for idx,p in enumerate(data[1:], 1):
                if p == data[idx - 1]:
                    data[idx - 1]= p * 2
                    data[idx]=0
            data = [cell for cell in data if cell != 0]
            data+= [0] * (4 - len(data))
            grid[i] = data[::-1]
    elif direction.lower() == 'w':
        for j in range(4):
            data = [grid[i][j] for i in range(4) if grid[i][j] != 0]
            for idx,p in enumerate(data[1:], 1):
                if p == data[idx - 1]:
                    data[idx - 1]= p * 2
                    data[idx]=0
            data = [cell for cell in data if cell != 0]
            data+= [0] * (4 - len(data))
            for i in range(4):
                grid[i][j] = data[i]
    elif direction.lower() == 's':
        for j in range(4):
            data = [grid[i][j] for i in range(4) if grid[i][j] != 0][::-1]
            for idx,p in enumerate(data[1:], 1):
                if p == data[idx - 1]:
                    data[idx - 1]= p * 2
                    data[idx]=0
            data = [cell for cell in data if cell != 0]
            data+= [0] * (4 - len(data))
            data=data[::-1]
            for i in range(4):
                grid[i][j] = data[i]

    else:
        raise Exception('ERROR')

def check_win():
    for i in range(4):
        for j in range(4):
            if grid[i][j] == 2048:
                return True
    return False

def check_game_over():
    for i in range(4):
        for j in range(4):
            if grid[i][j] == 0:
                return False
            if i < 3 and grid[i][j] == grid[i + 1][j]:
                return False
            if j < 3 and grid[i][j] == grid[i][j + 1]:
                return False
    return True

def game_main():
    generate_new_tile()
    generate_new_tile()
    print_grid()
    while True:
        try:
            direction = input("Input direction of movement(use WASD): ")
            move(direction)
            generate_new_tile()
            print_grid()
            if check_win():
                print("YOU WIN!")
                break
            if check_game_over():
                print("YOU LOSE.")
                break
        except Exception as e:
            if str(e)=='ERROR':
                print('ERROR, please retype!')
            else:
                raise e
a = 0
while True:
    a = get_user_input("To play 2048 press 1 and to exit press 2:", "ERROR")
    if a == 1:
        game_main()
    if a == 2:
        break
