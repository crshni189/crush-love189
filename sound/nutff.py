import pygame

# Tạo một cửa sổ
pygame.init()
screen = pygame.display.set_mode((600, 400))

# Tạo một hình tròn
center = (100, 100)
radius = 100

# Vẽ hình tròn
pygame.draw.circle(screen, (255, 0, 0), center, radius)

# Vòng lặp chính
while True:
    # Kiểm tra sự kiện:
       for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
        # Nếu người dùng nhấp vào nút
        if event.type == pygame.MOUSEBUTTONDOWN and rect.collidepoint(event.pos):
            print("Nút đã được nhấp!")

    # Cập nhật màn hình
       pygame.display.update()
       pygame.display.flip()
