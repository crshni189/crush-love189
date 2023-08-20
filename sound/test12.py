import pygame, sys
pygame.init()
screen = pygame.display.set_mode((1000, 668))
pygame.display.set_caption("HELLO CRUSH!")
icon = pygame.image.load('assets/happygirl.jpg').convert_alpha()
pygame.display.set_icon(icon)
clock = pygame.time.Clock()
bg = pygame.image.load('assets/mandem.jpg').convert()
bg = pygame.transform.scale2x(bg)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(bg, (0, 0))

    color_1 = (255, 192, 203)
    color_2 = (0, 255, 0)
    color_3 = (255, 0, 0)
    color_4 = (255, 192, 203)
    start_pos_1 = (255, 50)
    start_pos_2 = (255, 200)
    start_pos_3 = (600,200)
    start_pos_4 = (255, 150) 
    text_1 = "I LOVE YOU!"
    text_2 = "Yes"
    text_3 ="No"
    text_4 ="DO YOU LOVE ME?"
    font_1 = pygame.font.SysFont("Times New Roman", 80)
    text_surface_1 = font_1.render(text_1, True, color_1)
    font_2 = pygame.font.SysFont("Arial", 60)
    text_surface_2 = font_2.render(text_2, True, color_2)
    font_3 = pygame.font.SysFont("Arial", 60)
    text_surface_3 = font_3.render(text_3, True, color_3)
    font_4 = pygame.font.SysFont("Times New Roman", 50)
    text_surface_4 = font_4.render(text_4, True, color_4)
    screen.blit(text_surface_1, start_pos_1)
    screen.blit(text_surface_2, start_pos_2)
    screen.blit(text_surface_3, start_pos_3)
    screen.blit(text_surface_4, start_pos_4)

    pygame.display.update()
    clock.tick(120)
 