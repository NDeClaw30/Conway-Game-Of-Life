import sys,pygame
from View import GoLView
from Model import GoLModel
from Controller import GoLController
def rungame():
    pygame.init()
    clock = pygame.time.Clock()
    view = GoLView()
    model = GoLModel(view.displaywidth // view.blockSize, view.displayheight // view.blockSize)
    view.setModel(model)
    ctrl = GoLController(view, model)
    x = 0
    while True:
        clock.tick(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                  
            if event.type == pygame.MOUSEBUTTONDOWN:
                if view.b3.collidepoint(pygame.mouse.get_pos()) and x == 1:
                    ctrl.running = True
                elif view.b4.collidepoint(pygame.mouse.get_pos()) and x == 1:
                    ctrl.running = False
                elif view.b2.collidepoint(pygame.mouse.get_pos()) and x == 1:
                    x = 2
                    view.quit()
                    pygame.quit()
                elif view.b1.collidepoint(pygame.mouse.get_pos()) and x == 0:
                    x = x + 1
                    view.start()
        if ctrl.running:
            model.DeadOrAlive()
        view.update(x)
        


if __name__ == '__main__':
    rungame()