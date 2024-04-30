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
        pygame.draw.rect(screen, (255, 255, 255), (100 * i, 100 * j, 100, 100))

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
            board[i][j] = turn

            # Kiểm tra xem người chơi đã thắng chưa
            if xo.check_winner(board):
                # Xác định người chơi nào đã thắng, thua, hay hòa
                winner = PLAYER1 if turn == PLAYER2 else PLAYER2
                if winner == " ":
                    message = "Hòa"
                else:
                    message = "Người chơi {} thắng!".format(winner)

                # Tạo một hộp thoại để hiển thị thông báo
                win_dialog = pygame.display.set_mode((200, 100))
                pygame.draw.rect(win_dialog, (255, 0, 0), (0, 0, 200, 100))
                pygame.draw.rect(win_dialog, (255, 255, 255), (10, 10, 180, 80))
                pygame.draw.text(win_dialog, message, (40, 30), (0, 0, 0))

                # Hiện hộp thoại lên màn hình
                pygame.display.update()
                while pygame.event.wait().type != pygame.QUIT:
                    pass
                break

            # Chuyển lượt chơi
            turn = PLAYER2 if turn == PLAYER1 else PLAYER1

    # Vẽ lại bàn cờ
    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            pygame.draw.rect(screen, (0, 0, 0), (100 * i, 100 * j, 100, 100))
            color = (255, 0, 0) if board[i][j] == PLAYER1 else (0, 255, 0)
            pygame.draw.rect(screen, color, (100 * i + 10, 100 * j + 10, 80, 80))
    # Cập nhật màn hình
    pygame.display.update()
