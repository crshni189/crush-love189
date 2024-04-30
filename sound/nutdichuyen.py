import pygame

# Tạo một cửa sổ
pygame.init()
screen = pygame.display.set_mode((1000, 630))
icon=pygame.image.load('assets/logoff.jpg').convert_alpha()
pygame.display.set_caption(' VIP PRO HACK')
pygame.display.set_icon(icon)
# Tạo một hình tròn
center = (100, 520)
radius = 100
# Vẽ hình tròn
pygame.draw.circle(screen, (189, 225, 229), center, radius)


# Vòng lặp chính
while True:
  #  Kiểm tra sự kiện:
       for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
        # Nếu người dùng nhấp vào nút
        if event.type == pygame.MOUSEBUTTONDOWN:
            print("Nút đã được nhấp!")

    # Cập nhật màn hình
       pygame.display.update()
