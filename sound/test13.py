import pygame

# Khởi tạo pygame
pygame.init()

# Tạo cửa sổ
screen = pygame.display.set_mode((640, 480))

# Viết câu DO YOU LOVE ME
font = pygame.font.Font(None, 100)
text = font.render("DO YOU LOVE ME?", True, (0, 0, 0))
screen.blit(text, (100, 100))

# Tạo nút yes
button_yes = pygame.Rect(100, 200, 100, 50)
text_yes = font.render("Yes", True, (0, 255, 0))

# Tạo nút no
button_no = pygame.Rect(200, 200, 100, 50)
text_no = font.render("No", True, (255, 0, 0))

# Vòng lặp chính
running = True
while running:

    # Xử lý sự kiện
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_yes.collidepoint(event.pos):
                text = font.render("I love you", True, (0, 0, 0))
            else:
                text = font.render("I don't love you", True, (0, 0, 0))
                
                pygame.quit()

    # Vẽ màn hình
    screen.fill((255, 255, 255))
    screen.blit(text, (100, 100))
    screen.blit(text_yes, (100, 200))
    screen.blit(text_no, (200, 200))

    pygame.display.update()

# Đóng pygame
pygame.quit()
