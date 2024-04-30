import pygame

# Tạo một cửa sổ
pygame.init()
screen = pygame.display.set_mode((1000, 670))
icon=pygame.image.load('assets/logoff.jpg').convert_alpha()
pygame.display.set_caption(' VIP PRO HACK')
pygame.display.set_icon(icon)

# Tạo hai nhân vật người que
class Stickman:

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.image.load("assets/yellowbird-upflap.png")
        self.state = "standing"
        self.rect = pygame.Rect(0, 0, 50, 100)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        self.rect.x = self.x
        self.rect.y = self.y

    def attack(self):
        if self.state == "standing":
            self.state = "attacking"

    def be_hit(self):
        if self.state == "standing":
            self.state = "hit"
    def draw(self, screen):
        screen.blit(self.image, self.rect)


stickman1 = Stickman(100, 100, 50, 100)
stickman2 = Stickman(600, 100, 50, 100)

# Vòng lặp chính
while True:
    # Kiểm tra sự kiện:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    # Di chuyển nhân vật 1
    if stickman1.state == "standing":
        if pygame.key.get_pressed()[pygame.K_d]:
            stickman1.move(10, 0)
        elif pygame.key.get_pressed()[pygame.K_LEFT]:
            stickman1.move(-10, 0)

    # Di chuyển nhân vật 2
    if stickman2.state == "standing":
        if pygame.key.get_pressed()[pygame.K_d]:
            stickman2.move(10, 0)
        elif pygame.key.get_pressed()[pygame.K_a]:
            stickman2.move(-10, 0)

    # Kiểm tra va chạm
    if stickman1.rect.colliderect(stickman2.rect):
        if stickman1.state == "attacking":
            stickman2.be_hit()
        elif stickman2.state == "attacking":
            stickman1.be_hit()

    # Vẽ màn hình
    screen.fill((255, 255, 255))
    stickman1.draw(screen)
    stickman2.draw(screen)

    pygame.display.update()
