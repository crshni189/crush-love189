import pygame,random

pygame.init()

screen = pygame.display.set_mode((1000, 668))
pygame.display.set_caption("HELLO CRUSH!")
icon = pygame.image.load('assets/happygirl.jpg').convert_alpha()
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
bg = pygame.image.load('assets/mandem.jpg').convert()
bg = pygame.transform.scale2x(bg)

font = pygame.font.Font(None,100)
text = font.render("I LOVE YOU!", True, (255, 192, 203))
screen.blit(text, (100, 100))

button_yes = pygame.Rect(100, 200, 100, 50)
text_yes = font.render("Yes", True, (0, 255, 0))

button_no = pygame.Rect(200, 200, 100, 50)
text_no = font.render("No", True, (255, 0, 0))

text_dou = font.render("DO YOU LOVE ME?", True, (255, 192, 203))

running = True
text_no_red = font.render("No", True, (255, 0, 0))
x = 0
y = 0
pygame.event.pump() 
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_yes.collidepoint(pygame.mouse.get_pos()):
                text = font.render("iuuu ni!!!", True, (255, 192, 203))
            else:
                text = font.render("iuuu ni!!!", True, (255, 192, 203))
            if button_no.collidepoint(pygame.mouse.get_pos()):
                text = font.render(" NO òi =-=", True, (255, 192, 203))                                                                                                                                                                                                                                                                                    

                screen.blit(text_no_red, (x, y))
                x = random.randint(0, screen.get_width() - text_no_red.get_width())
                y = random.randint(0, screen.get_height() - text_no_red.get_height())

    
    screen.blit(bg, (0, 0))
    screen.blit(text, (300, 50))
    screen.blit(text_dou, (200, 140))
    screen.blit(text_yes, (600, 200)) 
    if button_no.collidepoint(pygame.mouse.get_pos()):
        screen.blit(text_no_red, (x, y))
    else:
        screen.blit(text_no_red, (200, 200))
    pygame.display.update()
pygame.quit()
clock.tick(120)