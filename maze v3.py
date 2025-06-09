import random

Num = 15  # should be odd

    
pointer = [1, 1]
mode = "kill"
direction = {
    "north": [0, -2],
    "east": [2, 0],
    "south": [0, 2],
    "west": [-2, 0]
}

# Each cell: [x, y, wall(True/False), n, e, s, w, border, visited]
CELLS = [[x, y, True, False, False, False, False, False, False] for y in range(Num) for x in range(Num)]

def conv(x, y):
    return x + y * Num

def screen(save_to_file=False, filename="maze.txt"):
    WALL_CHAR = "█"
    maze_str = ""

    for cell in CELLS:
        if cell[2]:  # Wall
            maze_str += WALL_CHAR
        else:
            maze_str += " "

        if cell[0] == Num - 1:
            maze_str += "\n"

    if save_to_file:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(maze_str)
        print(f"Maze saved to {filename}")
    else:
        print(maze_str)


def init():
    for cell in CELLS:
        x, y = cell[0], cell[1]
        if x == 0 or y == 0 or x == Num - 1 or y == Num - 1:
            cell[7] = True  # border
            cell[8] = True  # visited (prevents expansion into walls)

def update_cells(prev, curr):
    x, y = curr
    cx = conv(x, y)
    CELLS[cx][2] = False      # Mark current cell as path
    CELLS[cx][8] = True       # Visited

    # Also remove wall between prev and curr
    if prev:
        mx = (x + prev[0]) // 2
        my = (y + prev[1]) // 2
        CELLS[conv(mx, my)][2] = False  # Break wall

def available_dirs(x, y):
    dirs = []
    for d in direction:
        dx, dy = direction[d]
        nx, ny = x + dx, y + dy
        wx, wy = x + dx // 2, y + dy // 2  # wall cell

        if 0 <= nx < Num and 0 <= ny < Num:
            if not CELLS[conv(nx, ny)][8] and CELLS[conv(wx, wy)][2]:
                dirs.append(d)
    return dirs

def Maze_gen_kill():
    global mode, pointer
    update_cells(None, pointer)  # First time, no previous cell

    dirs = available_dirs(pointer[0], pointer[1])
    if not dirs:
        mode = "hunt"
        return

    d = random.choice(dirs)
    dx, dy = direction[d]

    mid = [pointer[0] + dx // 2, pointer[1] + dy // 2]
    nxt = [pointer[0] + dx, pointer[1] + dy]

    update_cells(pointer, mid)
    update_cells(mid, nxt)
    pointer = nxt

def Maze_gen_hunt():
    global pointer, mode

    for cell in CELLS:
        x, y = cell[0], cell[1]

        if x % 2 == 1 and y % 2 == 1 and not cell[8]:  # unvisited path cell
            for d in direction:
                dx, dy = direction[d]
                nx, ny = x + dx, y + dy

                if 0 <= nx < Num and 0 <= ny < Num and CELLS[conv(nx, ny)][8]:
                    # break wall between them
                    mx, my = (x + nx) // 2, (y + ny) // 2
                    CELLS[conv(mx, my)][2] = False

                    # mark hunted cell as visited and carve
                    pointer = [x, y]
                    CELLS[conv(x, y)][2] = False
                    CELLS[conv(x, y)][8] = True
                    mode = "kill"
                    return

    screen()
    screen(save_to_file=True)
    input("Maze generation completed")
    exit()


init()

while True:
    if mode == "kill":
        Maze_gen_kill()
    else:
        Maze_gen_hunt()

    
    

