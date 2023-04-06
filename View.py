import pygame

class GoLView:

    def __init__(self):
        self.width = 1480
        self.height = 720
        self.displaywidth = 1280
        self.displayheight = 720
        self.blockSize = 20
        self._DS = pygame.display.set_mode((self.width,self.height))
    
    def draw_grid(self):
        for x in range(0, self.displaywidth, self.blockSize):
           for y in range(0, self.displayheight, self.blockSize):
            rect = pygame.Rect(x, y, self.blockSize, self.blockSize)
            pygame.draw.rect(self._DS, (0,0,0), rect, 1)

    def update(self):
        self._DS.fill((220,220,220))
        pygame.draw.line(self._DS, (0,0,0), (self.displaywidth,0),(self.displaywidth,self.displayheight))
        self.draw_grid()
        pygame.display.update()
    
