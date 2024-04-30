import pygame

# Kích thước bàn cờ
WIDTH = 300
HEIGHT = 300

# Tạo một bảng cờ 3x3
board = [[None] * 3 for _ in range(3)]

# Màu sắc của các ô cờ
X_COLOR = (255, 0, 0)
O_COLOR = (0, 255, 0)

# Tạo một cửa sổ Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Tạo một con trỏ chuột
cursor = pygame.cursors.Cursor(pygame.cursors.CROSS)
pygame.display.set_cursor(cursor)

# Tạo một vòng lặp chơi game
while True:
    # Vẽ bàn cờ
    for i in range(3):
        for j in range(3):
            if board[i][j] == "X":
                pygame.draw.rect(screen, X_COLOR, (i * 100, j * 100, 100, 100))
            elif board[i][j] == "O":
                pygame.draw.rect(screen, O_COLOR, (i * 100, j * 100, 100, 100))

    # Xử lý sự kiện chuột
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Lấy tọa độ của con trỏ chuột
            x, y = pygame.mouse.get_pos()

            # Tìm ô cờ được nhấp chuột
            i = x // 100
            j = y // 100

            # Xác định quân cờ của người chơi hiện tại
            turn = "X" if board[i][j] is None else board[i][j]

            # Đặt quân cờ của người chơi hiện tại vào ô cờ
            board[i][j] = turn

            # Kiểm tra xem ai đã thắng
            winner = check_winner(board)
            if winner is not None:
                print(f"Người chơi {winner} đã thắng!")
                break

    # Cập nhật màn hình
    pygame.display.update()


# Hàm kiểm tra xem ai đã thắng
def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != None:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != None:
            return board[0][i]
        if board[i][0] == board[1][1] == board[2][2] != None:
            return board[i][0]
        if board[2][0] == board[1][1] == board[0][2] != None:
            return board[2][0]
    return None
