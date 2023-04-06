import sys,pygame
from view import GoLView
from model import GoLModel
def rungame():
    pygame.init()
    view = GoLView()
    model = GoLModel(view.displaywidth // view.blockSize, view.displayheight // view.blockSize)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        view.update()
        


if __name__ == '__main__':
    rungame()