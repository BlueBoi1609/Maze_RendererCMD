import sys
from wall_coords import *
from colorama import init

def Screen():
    global screen_rows
    for cells in CELLS :
        for wall_set, wall_enabled in RENDER_LAYERS:
            if wall_enabled and cells in wall_set:
                screen_rows[cells[1]][cells[0]] = BLOCK
                break
    temp_var=0
    temp_var_1=0
    for index_y,y in enumerate(maze_grid):
        screen_rows[temp_var+90].append("                ")
        screen_rows[temp_var+91].append("                ")
        for index_x,x in enumerate(y):
            if (player[0],player[1]) == (index_x,index_y):
                if player[2] == "N":
                    screen_rows[temp_var+90].append("^^")
                    screen_rows[temp_var+91].append("||")
                if player[2] == "E":
                    screen_rows[temp_var+90].append("->")
                    screen_rows[temp_var+91].append("->")
                if player[2] == "S":
                    screen_rows[temp_var+90].append("||")
                    screen_rows[temp_var+91].append("VV")
                if player[2] == "W":
                    screen_rows[temp_var+90].append("<-")
                    screen_rows[temp_var+91].append("<-")
                
            else:
                screen_rows[temp_var+90].append(x*2)
                screen_rows[temp_var+91].append(x*2)
            temp_var_1+=2
        temp_var+=2

    for row in screen_rows:
        screen_buffer.append("".join(row))  # Convert row to a string

            # Turn it into a single string with newlines
    screen_string = "\n".join(screen_buffer)

    sys.stdout.write(screen_string)
    sys.stdout.flush()

def walls_not_visible():
    global left_wall_1_,left_wall_2_,left_wall_3_,left_wall_4_,left_wall_5_,left_wall_6_,left_wall_7_,left_wall_8_,right_wall_1_,right_wall_2_,right_wall_3_,right_wall_4_,right_wall_5_,right_wall_6_,right_wall_7_,right_wall_8_,left_face_1_,left_face_2_,left_face_3_,left_face_4_,left_face_5_,left_face_6_,left_face_7_,left_face_8_ ,right_face_1_,right_face_2_,right_face_3_,right_face_4_,right_face_5_,right_face_6_,right_face_7_,right_face_8_,front_block_1_,front_block_2_,front_block_3_,front_block_4_,front_block_5_,front_block_6_,front_block_7_,front_block_8_,front_block_9_

    left_face_1_ = not left_wall_1_
    left_face_2_ = not left_wall_2_
    left_face_3_ = not left_wall_3_
    left_face_4_ = not left_wall_4_
    left_face_5_ = not left_wall_5_
    left_face_6_ = not left_wall_6_
    left_face_7_ = not left_wall_7_
    left_face_8_ = not left_wall_8_

    right_face_1_ = not right_wall_1_
    right_face_2_ = not right_wall_2_
    right_face_3_ = not right_wall_3_
    right_face_4_ = not right_wall_4_
    right_face_5_ = not right_wall_5_
    right_face_6_ = not right_wall_6_
    right_face_7_ = not right_wall_7_
    right_face_8_ = not right_wall_8_    
    
      
    if front_block_1_ :
        left_wall_1_ = left_wall_2_ = left_wall_3_ = left_wall_4_ = left_wall_5_ = left_wall_6_ = left_wall_7_ = left_wall_8_ = False
        right_wall_1_ = right_wall_2_ = right_wall_3_ = right_wall_4_ = right_wall_5_ = right_wall_6_ = right_wall_7_ = right_wall_8_ = False
        left_face_1_ = left_face_2_ = left_face_3_ = left_face_4_ = left_face_5_ = left_face_6_ = left_face_7_ = left_face_8_ = False
        right_face_1_ = right_face_2_ = right_face_3_ = right_face_4_ = right_face_5_ = right_face_6_ = right_face_7_ = right_face_8_ = False
        front_block_2_ = front_block_3_ = front_block_4_ = front_block_5_ = front_block_6_ = front_block_7_ = front_block_8_ =  front_block_9_ = False
    
    elif front_block_2_ :
        left_wall_2_ = left_wall_3_ = left_wall_4_ = left_wall_5_ = left_wall_6_ = left_wall_7_ = left_wall_8_ = False
        right_wall_2_ = right_wall_3_ = right_wall_4_ = right_wall_5_ = right_wall_6_ = right_wall_7_ = right_wall_8_ = False
        left_face_2_ = left_face_3_ = left_face_4_ = left_face_5_ = left_face_6_ = left_face_7_ = left_face_8_ = False
        right_face_2_ = right_face_3_ = right_face_4_ = right_face_5_ = right_face_6_ = right_face_7_ = right_face_8_ = False
        front_block_3_ = front_block_4_ = front_block_5_ = front_block_6_ = front_block_7_ = front_block_8_ = front_block_9_ = False
    
    elif front_block_3_ :
        left_wall_3_ = left_wall_4_ = left_wall_5_ = left_wall_6_ = left_wall_7_ = left_wall_8_ = False
        right_wall_3_ = right_wall_4_ = right_wall_5_ = right_wall_6_ = right_wall_7_ = right_wall_8_ = False
        left_face_3_ = left_face_4_ = left_face_5_ = left_face_6_ = left_face_7_ = left_face_8_ = False
        right_face_3_ = right_face_4_ = right_face_5_ = right_face_6_ = right_face_7_ = right_face_8_ = False
        front_block_4_ = front_block_5_ = front_block_6_ = front_block_7_ = front_block_8_ = front_block_9_ = False
    
    elif front_block_4_ :
        left_wall_4_ = left_wall_5_ = left_wall_6_ = left_wall_7_ = left_wall_8_ = False
        right_wall_4_ = right_wall_5_ = right_wall_6_ = right_wall_7_ = right_wall_8_ = False
        left_face_4_ = left_face_5_ = left_face_6_ = left_face_7_ = left_face_8_ = False
        right_face_4_ = right_face_5_ = right_face_6_ = right_face_7_ = right_face_8_ = False
        front_block_5_ = front_block_6_ = front_block_7_ = front_block_8_ = front_block_9_ = False

    elif front_block_5_ :
        left_wall_5_ = left_wall_6_ = left_wall_7_ = left_wall_8_ = False
        right_wall_5_ = right_wall_6_ = right_wall_7_ = right_wall_8_ = False
        left_face_5_ = left_face_6_ = left_face_7_ = left_face_8_ = False
        right_face_5_ = right_face_6_ = right_face_7_ = right_face_8_ = False
        front_block_6_ = front_block_7_ = front_block_8_ = front_block_9_ = False

    elif front_block_6_ :
        left_wall_6_ = left_wall_7_ = left_wall_8_ = False
        right_wall_6_ = right_wall_7_ = right_wall_8_ = False
        left_face_6_ = left_face_7_ = left_face_8_ = False
        right_face_6_ = right_face_7_ = right_face_8_ = False
        front_block_7_ = front_block_8_ = front_block_9_ = False

    elif front_block_7_ :
        left_wall_7_ = left_wall_8_ = False
        right_wall_7_ = right_wall_8_ = False
        left_face_7_ = left_face_8_ = False
        right_face_7_ = right_face_8_ = False
        front_block_8_ = front_block_9_ = False

    elif front_block_8_ :
        left_wall_8_ = False
        right_wall_8_ = False
        left_face_8_ = False
        right_face_8_ = False
        front_block_9_ = False

def maze_mapping():
    global left_wall_1_,left_wall_2_,left_wall_3_,left_wall_4_,left_wall_5_,left_wall_6_,left_wall_7_,left_wall_8_,right_wall_1_,right_wall_2_,right_wall_3_,right_wall_4_,right_wall_5_,right_wall_6_,right_wall_7_,right_wall_8_,left_face_1_,left_face_2_,left_face_3_,left_face_4_,left_face_5_,left_face_6_,left_face_7_,left_face_8_ ,right_face_1_,right_face_2_,right_face_3_,right_face_4_,right_face_5_,right_face_6_,right_face_7_,right_face_8_,front_block_1_,front_block_2_,front_block_3_,front_block_4_,front_block_5_,front_block_6_,front_block_7_,front_block_8_,front_block_9_
    
    left_wall_1_ = blocks[8][0]
    left_wall_2_ = blocks[7][0]
    left_wall_3_ = blocks[6][0]
    left_wall_4_ = blocks[5][0]
    left_wall_5_ = blocks[4][0]
    left_wall_6_ = blocks[3][0]
    left_wall_7_ = blocks[2][0]
    left_wall_8_ = blocks[1][0]
    right_wall_1_ = blocks[8][2]
    right_wall_2_ = blocks[7][2]
    right_wall_3_ = blocks[6][2]
    right_wall_4_ = blocks[5][2]
    right_wall_5_ = blocks[4][2]
    right_wall_6_ = blocks[3][2]
    right_wall_7_ = blocks[2][2]
    right_wall_8_ = blocks[1][2]
    front_block_1_ = blocks[8][1]
    front_block_2_ = blocks[7][1]
    front_block_3_ = blocks[6][1]
    front_block_4_ = blocks[5][1]
    front_block_5_ = blocks[4][1]
    front_block_6_ = blocks[3][1]
    front_block_7_ = blocks[2][1]
    front_block_8_ = blocks[1][1]
    front_block_9_ = blocks[0][0]

def block_input():
    if player[2] == "N":
        for x_index,x in enumerate([-1,0,1]):
            for y_index,y in enumerate([-8,-7,-6,-5,-4,-3,-2,-1,0]):
                if 0 <= player[1]+y <= len(maze_grid)-1 and 0 <= player[0]+x <= len(maze_grid)-1:
                    if maze_grid[player[1]+y][player[0]+x] == "█":
                        blocks[y_index][x_index]=True
                    else:
                        blocks[y_index][x_index]=False

    if player[2] == "E":
        for y_index,y in enumerate([-1,0,1]):   
            for x_index,x in enumerate([8,7,6,5,4,3,2,1,0]):
                if 0 <= player[1]+y <= len(maze_grid)-1 and 0 <= player[0]+x <= len(maze_grid)-1:
                    if maze_grid[player[1]+y][player[0]+x] == "█":
                        blocks[x_index][y_index]=True
                    else:
                        blocks[x_index][y_index]=False

    if player[2] == "S":
        for x_index,x in enumerate([1,0,-1]):
            for y_index,y in enumerate([8,7,6,5,4,3,2,1,0]):
                if 0 <= player[1]+y <= len(maze_grid)-1 and 0 <= player[0]+x <= len(maze_grid)-1:
                    if maze_grid[player[1]+y][player[0]+x] == "█":
                        blocks[y_index][x_index]=True
                    else:
                        blocks[y_index][x_index]=False

    if player[2] == "W":
        for y_index,y in enumerate([1,0,-1]):   
            for x_index,x in enumerate([-8,-7,-6,-5,-4,-3,-2,-1,0]):
                if 0 <= player[1]+y <= len(maze_grid)-1 and 0 <= player[0]+x <= len(maze_grid)-1:
                    if maze_grid[player[1]+y][player[0]+x] == "█":
                        blocks[x_index][y_index]=True
                    else:
                        blocks[x_index][y_index]=False




left_wall_1=set(left_wall_1)
left_wall_2=set(left_wall_2)
left_wall_3=set(left_wall_3)
left_wall_4=set(left_wall_4)
left_wall_5=set(left_wall_5)
left_wall_6=set(left_wall_6)
left_wall_7=set(left_wall_7)
left_wall_8=set(left_wall_8)

left_face_1=set(left_face_1)
left_face_2=set(left_face_2)
left_face_3=set(left_face_3)
left_face_4=set(left_face_4)
left_face_5=set(left_face_5)
left_face_6=set(left_face_6)
left_face_7=set(left_face_7)
left_face_8=set(left_face_8)

right_wall_1=set(right_wall_1)
right_wall_2=set(right_wall_2)
right_wall_3=set(right_wall_3)
right_wall_4=set(right_wall_4)
right_wall_5=set(right_wall_5)
right_wall_6=set(right_wall_6)
right_wall_7=set(right_wall_7)
right_wall_8=set(right_wall_8)

right_face_1=set(right_face_1)
right_face_2=set(right_face_2)
right_face_3=set(right_face_3)
right_face_4=set(right_face_4)
right_face_5=set(right_face_5)
right_face_6=set(right_face_6)
right_face_7=set(right_face_7)
right_face_8=set(right_face_8)

front_block_1=set(front_block_1)
front_block_2=set(front_block_2)
front_block_3=set(front_block_3)
front_block_4=set(front_block_4)
front_block_5=set(front_block_5)
front_block_6=set(front_block_6)
front_block_7=set(front_block_7)
front_block_8=set(front_block_8)
front_block_9=set(front_block_9)

# Walls
left_wall_1_ = left_wall_2_ = left_wall_3_ = left_wall_4_ = left_wall_5_ = left_wall_6_ = left_wall_7_ = left_wall_8_ = True
right_wall_1_ = right_wall_2_ = right_wall_3_ = right_wall_4_ = right_wall_5_ = right_wall_6_ = right_wall_7_ = right_wall_8_ = True

# Front blocks
front_block_1_ = front_block_2_ = front_block_3_ = front_block_4_ = front_block_5_ = front_block_6_ = front_block_7_ = front_block_8_ = front_block_9_ = False

left_face_1_ = None
left_face_2_ = None
left_face_3_ = None
left_face_4_ = None
left_face_5_ = None
left_face_6_ = None
left_face_7_ = None
left_face_8_ = None

right_face_1_ = None
right_face_2_ = None
right_face_3_ = None
right_face_4_ = None
right_face_5_ = None
right_face_6_ = None
right_face_7_ = None
right_face_8_ = None

CELLS=[ (x,y) for y in range(141) for x in range(281) ]

screen_buffer=[]

BLOCK = "#"

player=[1,1,"S"]

blocks=[[True,True,True],
            [True,True,True],
            [True,True,True],
            [True,True,True],
            [True,True,True],
            [True,True,True],
            [True,True,True],
            [True,True,True],
            [True,False,True],]

maze_grid = []

init()

with open("C:/Users/User/Desktop/Python projects/Maze/Main/maze.txt", "r", encoding="utf-8-sig") as f:
    for line in f:
        maze_grid.append(list(line.rstrip("\n")))



while True:   
    
    screen_rows = [["`" for _ in range(281)] for _ in range(141)]

    block_input()

    maze_mapping()

    walls_not_visible()

    RENDER_LAYERS=[(left_wall_1,left_wall_1_),
               (left_wall_2,left_wall_2_),
               (left_wall_3,left_wall_3_),
               (left_wall_4,left_wall_4_),
               (left_wall_5,left_wall_5_),
               (left_wall_6,left_wall_6_),
               (left_wall_7,left_wall_7_),
               (left_wall_8,left_wall_8_),
               
               (left_face_1,left_face_1_),
               (left_face_2,left_face_2_),
               (left_face_3,left_face_3_),
               (left_face_4,left_face_4_),
               (left_face_5,left_face_5_),
               (left_face_6,left_face_6_),
               (left_face_7,left_face_7_),
               (left_face_8,left_face_8_),
               
               (right_wall_1,right_wall_1_),
               (right_wall_2,right_wall_2_),
               (right_wall_3,right_wall_3_),
               (right_wall_4,right_wall_4_),
               (right_wall_5,right_wall_5_),
               (right_wall_6,right_wall_6_),
               (right_wall_7,right_wall_7_),
               (right_wall_8,right_wall_8_),
               
               (right_face_1,right_face_1_),
               (right_face_2,right_face_2_),
               (right_face_3,right_face_3_),
               (right_face_4,right_face_4_),
               (right_face_5,right_face_5_),
               (right_face_6,right_face_6_),
               (right_face_7,right_face_7_),
               (right_face_8,right_face_8_),
               
               (front_block_1,front_block_1_),
               (front_block_2,front_block_2_),
               (front_block_3,front_block_3_),
               (front_block_4,front_block_4_),
               (front_block_5,front_block_5_),
               (front_block_6,front_block_6_),
               (front_block_7,front_block_7_),
               (front_block_8,front_block_8_),
               (front_block_9,front_block_9_)]
    
    #sys.stdout.write('\x1b[H')       
    '''bg = [["`" for _ in range(281)] for _ in range(141)]
    bg_buffer=[]

    for row in bg:
        bg_buffer.append("".join(row))  


    screen_string = "\n".join(bg_buffer)

    sys.stdout.write(screen_string)
    sys.stdout.flush()'''
    
    Screen()

    movement=input("\x1b[2K")

    if movement == "a":
            if player[2] == "N":
                player[2]="W"
            elif player[2] == "E":
                player[2]="N"
            elif player[2] == "S":
                player[2]="E"
            elif player[2] == "W":
                player[2]="S"
    elif movement == "d":
            if player[2] == "N":
                player[2]="E"
            elif player[2] == "E":
                player[2]="S"
            elif player[2] == "S":
                player[2]="W"
            elif player[2] == "W":
                player[2]="N"
    elif movement == "w" and not blocks[7][1]:
            if player[2] == "N":
                player[1]-=1

            if player[2] == "E":
                player[0]+=1
            
            if player[2] == "S":
                player[1]+=1

            if player[2] == "W":
                player[0]-=1


   
