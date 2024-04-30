# file xo.py

def check_winner(board):
    for i in range(BOARD_SIZE):
        if board[i][0] == board[i][1] == board[i][2] != "X ":
            return True
        if board[0][i] == board[1][i] == board[2][i] != "X ":
            return True
        if board[0][0] == board[1][1] == board[2][2] != "O ":
            return True
        if board[2][0] == board[1][1] == board[0][2] != "O ":
            return True
    return False

# file main.py

import pygame
import xo

# Kích thước của bàn cờ
BOARD_SIZE = 3

# Các ký hiệu cho quân cờ
PLAYER1 = "X"
PLAYER2 = "O"

# Trạng thái của bàn cờ
board = []
for i in range(BOARD_SIZE):
    board.append([" "] * BOARD_SIZE)

# Trạng thái của lượt chơi
turn = PLAYER1

# Khởi tạo Pygame
pygame.init()

# Tạo cửa sổ game
screen = pygame.display.set_mode((BOARD_SIZE * 100, BOARD_SIZE * 100))

# Vẽ bàn cờ
for i in range(BOARD_SIZE):
    for j in range(BOARD_SIZE):
        pygame.draw.rect(screen, (255, 50, 135), (100 * i, 100 * j, 100, 100))

# Vòng lặp trò chơi
while True:

    # Xử lý các sự kiện
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # Xử lý khi người chơi nhấp chuột
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            i = x // 100
            j = y // 100

            # Kiểm tra xem ô đã được sử dụng chưa
            if board[i][j] != " ":
                continue

            # Đặt quân cờ
            if turn == PLAYER1:
                board[i][j] = "X"
                color = (255, 45, 0)
            else:
                board[i][j] = "O"
                color = (0, 255, 0)

            # Kiểm tra xem người chơi đã thắng chưa
            if xo.check_winner(board):
                if turn == PLAYER1:
                    print("Người chơi 1 thắng!")
                else:
                    print("Người chơi 2 thắng!")
                break

            # Chuyển lượt chơi
            turn = PLAYER2 if turn == PLAYER1 else PLAYER1

    # Vẽ lại bàn cờ
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            pygame.draw.rect(screen, (234, 143, 0), (100 * i, 100 * j, 100, 100))
            pygame.draw.rect(screen, color, (100 * i + 10, 100 * j + 10, 80, 80))
    # Cập nhật màn hình
    pygame.display.update()

