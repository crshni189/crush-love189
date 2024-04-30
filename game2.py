import pygame

# Tạo một cửa sổ pygame.
pygame.init()
screen = pygame.display.set_mode((1000, 509))
icon=pygame.image.load('assets/logoff.jpg').convert_alpha()
pygame.display.set_caption(' Người que')
pygame.display.set_icon(icon)

# Tạo một lớp nhân vật người que.
class Stickman:

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.image = pygame.image.load("assets/yellowbird-upflap.png")
        self.state = "standing"
        self.rect = pygame.Rect(0, 0, 50, 100)
        self.blood = 100

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        self.rect.x = self.x
        self.rect.y = self.y

    def punch(self):
        if self.state == "standing":
            self.state = "punching"

    def jump(self):
        if self.state == "standing":
            self.state = "jumping"

    def reduce_blood(self, amount):
        self.blood -= amount
        if self.blood <= 0:
            print("Game over!")
            pygame.quit()

    def draw(self, screen):
        screen.blit(self.image, self.rect)

# Tạo một đối tượng nhân vật người que.
stickman = Stickman(100, 100, 50, 100)

# Vòng lặp chính
while True:
    # Kiểm tra sự kiện:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        # Di chuyển nhân vật
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                stickman.move(10, 0)
            elif event.key == pygame.K_LEFT:
                stickman.move(-10, 0)
            elif event.key == pygame.K_UP:
                stickman.jump()
            elif event.key == pygame.K_SPACE:
                stickman.punch()

    # Vẽ màn hình
    screen.fill((255, 255, 255))
    stickman.draw(screen)
    pygame.draw.rect(screen, (255, 0, 0), (10, 10, stickman.blood, 20))
    pygame.display.update()
