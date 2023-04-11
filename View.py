import pygame
from pygame.locals import QUIT

pygame.init()
screen = pygame.display.set_mode((600, 600))
x = 0



def button(screen, position, text):
    font = pygame.font.SysFont("Arial", 50)
    text_render = font.render(text, 1, (255, 0, 0))
    x, y, w , h = text_render.get_rect()
    x, y = position
    pygame.draw.line(screen, (150, 150, 150), (x, y), (x + w , y), 5)
    pygame.draw.line(screen, (150, 150, 150), (x, y - 2), (x, y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x, y + h), (x + w , y + h), 5)
    pygame.draw.line(screen, (50, 50, 50), (x + w , y+h), [x + w , y], 5)
    pygame.draw.rect(screen, (100, 100, 100), (x, y, w , h))
    return screen.blit(text_render, (x, y))

def start():
    print("Ok, let's go")
    pygame.draw.circle(screen, (0 , 0 , 0), (250,50) , 100 )
def quit():
  print("Thanks for Playing")

def menu():
    b1 = button(screen, (250, 280), "Start")
    global x
    while x == 0:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                  
            if event.type == pygame.MOUSEBUTTONDOWN:
                if b1.collidepoint(pygame.mouse.get_pos()):
                    x = x + 1
                    screen.fill("white")
                    start()
                    print(x)
                    WINDOW_SIZE = (800, 800)
                    screen = pygame.display.set_mode(WINDOW_SIZE)
                    pygame.display.set_caption("Conway Game of Life")

                    ROWS = 50
                    COLS = 50
                    CELL_SIZE = 20
                    MARGIN = 5

                    grid = []
                    for row in range(ROWS):
                        grid.append([])
                        for col in range(COLS):
                            rect = pygame.Rect(col * (CELL_SIZE + MARGIN), row * (CELL_SIZE + MARGIN), CELL_SIZE, CELL_SIZE)
                            grid[row].append(rect)

                    for row in range(ROWS):
                        for col in range(COLS):
                            pygame.draw.rect(screen, (255, 255, 255), grid[row][col])
                            pygame.draw.rect(screen, (0, 0, 0), grid[row][col], 1)

                    pygame.display.update()
      
    b2 = button(screen, (250, 280), "Quit")
    while x == 1:
      for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                  
            if event.type == pygame.MOUSEBUTTONDOWN:
                if b2.collidepoint(pygame.mouse.get_pos()):
                    x = 0
                    quit()
                    screen.fill("Black")
                    print(x)
                  
      pygame.display.update()
      
    pygame.quit()
menu()





class Board:
    def __init__(self , rows , columns):
        '''
        constructor holds input from user and populates the grid with cells. 
        '''
        self._rows = rows
        self._columns = columns   
        self._grid = [[Cell() for column_cells in range(self._columns)] for row_cells in range(self._rows)]

        self._generate_board()

    def draw_board(self):
        '''
        method that draws the actual board in the terminal
        '''
        print('\n'*10)
        print('printing board')
        for row in self._grid:
            for column in row:
                print (column.get_print_character(),end='')
            print () # to create a new line pr. row.

    def _generate_board(self):
        '''
        method that sets the random state of all cells.
        '''

        for row in self._grid:
            for column in row:
                #there is a 33% chance the cells spawn alive.
                chance_number = randint(0,2)
                if chance_number == 1:
                    column.set_alive()

    def update_board(self):
        '''
        method that updates the board based on
        the check of each cell pr. generation
        '''
        #cells list for living cells to kill and cells to resurrect or keep alive
        goes_alive = []
        gets_killed = []

        for row in range(len(self._grid)):
            for column in range(len(self._grid[row])):
                #check neighbour pr. square:
                check_neighbour = self.check_neighbour(row , column)
                
                living_neighbours_count = []

                for neighbour_cell in check_neighbour:
                    #check live status for neighbour_cell:
                    if neighbour_cell.is_alive():
                        living_neighbours_count.append(neighbour_cell)

                cell_object = self._grid[row][column]
                status_main_cell = cell_object.is_alive()

                #If the cell is alive, check the neighbour status.
                if status_main_cell == True:
                    if len(living_neighbours_count) < 2 or len(living_neighbours_count) > 3:
                        gets_killed.append(cell_object)

                    if len(living_neighbours_count) == 3 or len(living_neighbours_count) == 2:
                        goes_alive.append(cell_object)

                else:
                    if len(living_neighbours_count) == 3:
                        goes_alive.append(cell_object)

        #sett cell statuses
        for cell_items in goes_alive:
            cell_items.set_alive()

        for cell_items in gets_killed:
            cell_items.set_dead()

    
    
    def check_neighbour(self, check_row , check_column):
        '''
        method that checks all the neighbours for all the cells
        and returns the list of the valid neighbours so the update 
        method can set the new status
        '''        
        #how deep the search is:
        search_min = -1
        search_max = 2

        #empty list to append neighbours into.
        neighbour_list = []
        for row in range(search_min,search_max):
            for column in range(search_min,search_max):
                neighbour_row = check_row + row
                neighbour_column = check_column + column 
                
                valid_neighbour = True

                if (neighbour_row) == check_row and (neighbour_column) == check_column:
                    valid_neighbour = False

                if (neighbour_row) < 0 or (neighbour_row) >= self._rows:
                    valid_neighbour = False

                if (neighbour_column) < 0 or (neighbour_column) >= self._columns:
                    valid_neighbour = False

                if valid_neighbour:
                    neighbour_list.append(self._grid[neighbour_row][neighbour_column])
        return neighbour_list

