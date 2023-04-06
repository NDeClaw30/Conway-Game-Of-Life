import pygame

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


