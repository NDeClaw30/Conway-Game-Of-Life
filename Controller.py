import pygame
from Model import GoLModel
from View import GoLView

class GoLController:

    def __init__(self, view, model):
        self._view = view
        self._model = model
        self.running = False

    def toggleCell(self, click):
        if click.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.getPos()
            if pygame.Rect(0,0, self._view.displaywidth, self._view.displayheight).collidepoint(pos):
                pass
