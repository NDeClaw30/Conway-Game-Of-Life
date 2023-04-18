import pygame
from Model import GoLModel

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

class GoLView:

    def __init__(self):
        self.width = 1480
        self.height = 720
        self.displaywidth = 1280
        self.displayheight = 720
        self.blockSize = 20
        self._DS = pygame.display.set_mode((self.width,self.height))
        self.b1 = button(self._DS, (self.width // 2, self.height // 2), "Start")
        self.b2 = button(self._DS, (self.width // 2, self.height //2), "Quit")
        self.b3 = button(self._DS, (self.width // 2, self.height //2), "Start")
        self.b4 = button(self._DS, (self.width //2, self.height //2), "Stop")
        self.model = None

    def setModel(self, model):
        self.model = model
    
    def draw_grid(self):
        for x in range(0, self.displaywidth, self.blockSize):
           for y in range(0, self.displayheight, self.blockSize):
            rect = pygame.Rect(x, y, self.blockSize, self.blockSize)
            pygame.draw.rect(self._DS, (0,0,0), rect, 1)


    def draw_cells(self):
        grid = self.model.getGrid()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    pygame.draw.rect(self._DS, (255,0,0), (j * self.blockSize, i * self.blockSize, self.blockSize, self.blockSize))

    

    def start(self):
        self._DS.fill("white")
        print("Ok, let's go")
        pygame.draw.circle(self._DS, (0 , 0 , 0), (250,50) , 100 )

    def quit(self):
        self._DS.fill("Black")
        print("Thanks for Playing")
