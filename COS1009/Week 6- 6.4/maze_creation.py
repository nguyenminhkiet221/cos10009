import pygame
import sys


class Cell:
    def __init__(self):
        self.north = None
        self.south = None
        self.east = None
        self.west = None

        self.vacant = False
        self.visited = False
        self.on_path = False

    def copy_from(self, other: "Cell"):
        self.north = other.north
        self.south = other.south
        self.east = other.east
        self.west = other.west
        self.vacant = other.vacant
        self.visited = other.visited
        self.on_path = other.on_path


pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Maze Creation")
clock = pygame.time.Clock()

# Colours
GREEN = (0, 255, 0)
YELLOW = (255, 255, 100)
RED = (255, 0, 0)


MAP_WIDTH = SCREEN_WIDTH
MAP_HEIGHT = SCREEN_HEIGHT
CELL_DIM = 60

x_cell_count = MAP_WIDTH // CELL_DIM
y_cell_count = MAP_HEIGHT // CELL_DIM


maze: list[list[Cell]] = []

i = 0
while i < x_cell_count:
    maze.append([])
    j = 0
    while j < y_cell_count:
        maze[i].append(Cell())
        j += 1
    i += 1


# Connect cells
i = 0
while i < x_cell_count:
    j = 0
    while j < y_cell_count:

        # North
        if j > 0:
            maze[i][j].north = maze[i][j - 1]

        # South
        if j < y_cell_count - 1:
            maze[i][j].south = maze[i][j + 1]

        # West
        if i > 0:
            maze[i][j].west = maze[i - 1][j]

        # East
        if i < x_cell_count - 1:
            maze[i][j].east = maze[i + 1][j]

        j += 1
    i += 1



def print_maze():

    i = 0
    while i < x_cell_count:

        j = 0
        while j < y_cell_count:

            cell = maze[i][j]

            north = 1 if cell.north is not None else 0
            south = 1 if cell.south is not None else 0
            east  = 1 if cell.east  is not None else 0
            west  = 1 if cell.west  is not None else 0

            print(f"Cell x: {i}, y: {j} north:{north} south:{south} east:{east} west:{west}")

            j += 1

        print("---------- End of Column ----------")
        i += 1


print_maze()



while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

        elif event.type == pygame.MOUSEBUTTONDOWN:

            if event.button == 1: 
                mouse_pos = event.pos
                col = mouse_pos[0] // CELL_DIM
                row = mouse_pos[1] // CELL_DIM

                cell = maze[col][row]
                cell.vacant = not cell.vacant

    
    screen.fill((0, 0, 0))

    col = 0
    while col < x_cell_count:
        row = 0
        while row < y_cell_count:

            cell = maze[col][row]

            color = YELLOW if cell.vacant else GREEN
            if cell.on_path:
                color = RED

            pygame.draw.rect(
                screen,
                color,
                (col * CELL_DIM,
                 row * CELL_DIM,
                 CELL_DIM - 1,
                 CELL_DIM - 1)
            )

            row += 1
        col += 1

    pygame.display.flip()
    clock.tick(60)