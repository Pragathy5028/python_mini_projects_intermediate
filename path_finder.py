import curses
from curses import wrapper
from gettext import find
import queue
import time

maze = [
    ["#", "O", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#"]
]
# stdstr-standard output screen.
# Instead of uisng standard print statement ,other commands are  used. 
# This is gonna take over the terminal


def print_maze(maze,stdscr,path=[]):
    BLUE=curses.color_pair(1)#default maze blue
    RED=curses.color_pair(2)#path red

    for i,row in enumerate(maze):
        for j,value in enumerate(row):
            if(i,j) in path:
                stdscr.addstr(i,j*4,"X",RED)
            else:
                stdscr.addstr(i,j*4,value,BLUE)

                


def find_start(maze,start):#breadth for search algorithm
    for i,row in enumerate(maze):
        for j,value in enumerate(row):
            return i,j

    return None

def find_neighbors(maze,row,col):
        neigbors=[]
        if row>0:#UP
            neigbors.append((row-1,col))
        if row+1<len(maze):#DOWN
            neigbors.append((row+1,col))
        if col>0:#LEFT
            neigbors.append((row,col-1))
        if col+1< len(maze[0]):#RIGHT
            neigbors.append((row,col+1))
        
        return neigbors



def find_path(maze,stdscr):
    start="O"
    end="X"
    start_position=find_start(maze,start)
    q=queue.Queue()
    q.put((start_position,[start_position]))

    visited = set()


    while not q.empty():
        current_position,path=q.get()
        row ,col =current_position

        stdscr.clear()
        print_maze(maze,stdscr,path)
        time.sleep(0.2)
        stdscr.refresh()

        if maze[row][col]== end:
            return path
        neighbors=find_neighbors(maze,row,col)
        for neighor in neighbors:
            if neighor in visited:
                continue
            r,c=neighor
            if maze[r][c]=="#":
                continue

            new_path= path + [neighor]
            q.put((neighor,new_path))
            visited.add(neighor)

    


def main(stdscr): 
    curses.init_pair(1,curses.COLOR_BLUE,curses.COLOR_BLACK)#1st foreground colr,2nd background color
    curses.init_pair(2,curses.COLOR_RED,curses.COLOR_BLACK)
    find_path(maze,stdscr)
    stdscr.getch() #used to view the output or else the program wont wait long enough to see the output.


wrapper(main
)

