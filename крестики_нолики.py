import pygame
import random
pygame.init()
screen = pygame.display.set_mode((620, 620))
clock = pygame.time.Clock()
place1 = pygame.Rect(0, 0, 200, 200)
place2 = pygame.Rect(210, 0, 200, 200)
place3 = pygame.Rect(420, 0, 200, 200)
place4 = pygame.Rect(0, 210, 200, 200)
place5 = pygame.Rect(210, 210, 200, 200)
place6 = pygame.Rect(420, 210, 200, 200)
place7 = pygame.Rect(0, 420, 200, 200)
place8 = pygame.Rect(210, 420, 200, 200)
place9 = pygame.Rect(420, 420, 200, 200)
x_img = pygame.image.load("x.png")
x_img = pygame.transform.scale(x_img, (200, 200))
o_img = pygame.image.load("o.png")
o_img = pygame.transform.scale(o_img, (200, 200))
places_x = [0] * 9
places_o = [0] * 9
places = [True] * 9  # True = свободна
move = 1  # 1 = игрок (X), 2 = бот (O)
bot_moved = False
top_left=(100 , 100)
top_right=(520 , 100)
bottom_right=(520 , 110)
bottom_left=(100 , 110)
vertices= [top_left , top_right , bottom_right , bottom_left]
running = True
def check_winner(player_places):
    """Проверяет, выиграл ли игрок. Возвращает индекс выигрышной линии или -1."""
    # Горизонтали
    if player_places[0] and player_places[1] and player_places[2]:
        return 0
    if player_places[3] and player_places[4] and player_places[5]:
        return 1
    if player_places[6] and player_places[7] and player_places[8]:
        return 2
    # Вертикали
    if player_places[0] and player_places[3] and player_places[6]:
        return 3
    if player_places[1] and player_places[4] and player_places[7]:
        return 4
    if player_places[2] and player_places[5] and player_places[8]:
        return 5
    # Диагонали
    if player_places[0] and player_places[4] and player_places[8]:
        return 6
    if player_places[2] and player_places[4] and player_places[6]:
        return 7
    return -1
def draw_win_line(line_type):
    """Рисует линию над выигрышной комбинацией."""
    if line_type == 0:  # Первая горизонталь
        top_left = (100, 100)
        top_right = (520, 100)
        bottom_right = (520, 110)
        bottom_left = (100, 110)
    elif line_type == 1:  # Вторая горизонталь
        top_left = (100, 310)
        top_right = (520, 310)
        bottom_right = (520, 320)
        bottom_left = (100, 320)
    elif line_type == 2:  # Третья горизонталь
        top_left = (100, 520)
        top_right = (520, 520)
        bottom_right = (520, 530)
        bottom_left = (100, 530)
    elif line_type == 3:  # Первая вертикаль
        top_left = (100, 100)
        top_right = (110, 100)
        bottom_right = (110, 520)
        bottom_left = (100, 520)
    elif line_type == 4:  # Вторая вертикаль
        top_left = (310, 100)
        top_right = (320, 100)
        bottom_right = (320, 520)
        bottom_left = (310, 520)
    elif line_type == 5:  # Третья вертикаль
        top_left = (520, 100)
        top_right = (530, 100)
        bottom_right = (530, 520)
        bottom_left = (520, 520)
    elif line_type == 6:  # Диагональ \
        top_left = (100, 110)
        top_right = (110, 100)
        bottom_right = (530, 520)
        bottom_left = (520, 530)
    elif line_type == 7:  # Диагональ /
        top_left = (520, 100)
        top_right = (530, 110)
        bottom_right = (110, 530)
        bottom_left = (100, 520)
    
    vertices = [top_left, top_right, bottom_right, bottom_left]
    pygame.draw.polygon(screen, (255, 0, 0), vertices, 0)
def end():
    """Проверяет условия окончания игры и рисует выигрышную линию."""
    x_win = check_winner(places_x)
    o_win = check_winner(places_o)
    
    if x_win != -1:
        draw_win_line(x_win)
    elif o_win != -1:
        draw_win_line(o_win)
def free_places():
    # Обновляем список доступных клеток: если в клетке уже стоит X или O, она недоступна
    for i in range(9):
        if places_x[i] != 0 or places_o[i] != 0:
            places[i] = False
        else:
            places[i] = True
class x():
    @staticmethod
    def draw_x():
        if places_x[0] == 1:
            screen.blit(x_img, (0, 0))
        if places_x[1] == 2:
            screen.blit(x_img, (210, 0))
        if places_x[2] == 3:
            screen.blit(x_img, (420, 0))
        if places_x[3] == 4:
            screen.blit(x_img, (0, 210))
        if places_x[4] == 5:
            screen.blit(x_img, (210, 210))
        if places_x[5] == 6:
            screen.blit(x_img, (420, 210))
        if places_x[6] == 7:
            screen.blit(x_img, (0, 420))
        if places_x[7] == 8:
            screen.blit(x_img, (210, 420))
        if places_x[8] == 9:
            screen.blit(x_img, (420, 420))
class o():
    @staticmethod
    def draw_o():
        if places_o[0] == 1:
            screen.blit(o_img, (0, 0))
        if places_o[1] == 2:
            screen.blit(o_img, (210, 0))
        if places_o[2] == 3:
            screen.blit(o_img, (420, 0))
        if places_o[3] == 4:
            screen.blit(o_img, (0, 210))
        if places_o[4] == 5:
            screen.blit(o_img, (210, 210))
        if places_o[5] == 6:
            screen.blit(o_img, (420, 210))
        if places_o[6] == 7:
            screen.blit(o_img, (0, 420))
        if places_o[7] == 8:
            screen.blit(o_img, (210, 420))
        if places_o[8] == 9:
            screen.blit(o_img, (420, 420))
    @staticmethod
    def move_o():
        global bot_moved, move
        # Защита: бот ходит только когда move == 2 и только один раз за ход
        if move != 2 or bot_moved:
            return
        # Убедимся, что список свободных клеток актуален
        free_places()
        # Если одно из правил выполнено — бот ставит O и переключает ход.
        made_move = False
        #бот ходит только если клетка свободна
        def place_o(idx):
            nonlocal made_move
            if places[idx]:
                places_o[idx] = idx + 1
                made_move = True
                return True
            return False
        # Логика бота
        if (places_x[1] == 2 and places[0] and places_x[0] == 0 and places[2] and places_x[2] == 0) or (places_x[3] == 4 and places[0] and places_x[0] == 0 and places_x[6] == 0):
            place_o(4)
        elif places_x[0] == 1 and places[8] and places[1] and places[3] and places[6] and move == 2:
            place_o(8)
        elif places_x[2] == 3 and places[6] and places[1] and places[5] and places[8] and places[0] and move == 2:
            place_o(6)
        elif places_x[6] == 7 and places[2] and places[3] and places[7] and places[8] and places[0] and move == 2:
            place_o(2)
        elif places_x[8] == 9 and places[0] and places[5] and places[7] and places[6] and places[2] and move == 2:
            place_o(0)
        elif places_x[0] == 1 and places_x[1] == 2 and places[2] and places_x[3] == 0 and places_x[4] == 0 and move == 2:
            place_o(2)
        elif places_x[0] == 1 and places_x[2] == 3 and places[1] and move == 2:
            place_o(1)
        elif places_x[1] == 2 and places_x[2] == 3 and places[0] and move == 2:
            place_o(0)
        elif places_x[3] == 4 and places_x[4] == 5 and places[5] and places_x[1] == 0 and move == 2:
            place_o(5)
        elif places_x[3] == 4 and places_x[5] == 6 and places[4] and move == 2:
            place_o(4)
        elif places_x[4] == 5 and places_x[5] == 6 and places[3] and move == 2:
            place_o(3)
        elif places_x[6] == 7 and places_x[7] == 8 and places[8] and move == 2:
            place_o(8)
        elif places_x[6] == 7 and places_x[8] == 9 and places[7] and move == 2:
            place_o(7)
        elif places_x[7] == 8 and places_x[8] == 9 and places[6] and move == 2:
            place_o(6)
        elif places_x[0] == 1 and places_x[3] == 4 and places[6] and move == 2:
            place_o(6)
        elif places_x[0] == 1 and places_x[6] == 7 and places[3] and move == 2:
            place_o(3)
        elif places_x[3] == 4 and places_x[6] == 7 and places[0] and move == 2:
            place_o(0)
        elif places_x[1] == 2 and places_x[4] == 5 and places[7] and move == 2:
            place_o(7)
        elif places_x[1] == 2 and places_x[7] == 8 and places[4] and move == 2:
            place_o(4)
        elif places_x[4] == 5 and places_x[7] == 8 and places[1] and move == 2:
            place_o(1)
        elif places_x[0] == 1 and places_x[4] == 5 and places[8] and move == 2:
            place_o(8)
        elif places_x[0] == 1 and places_x[8] == 9 and places[4] and move == 2:
            place_o(4)
        elif places_x[4] == 5 and places_x[8] == 9 and places[0] and move == 2:
            place_o(0)
        elif places_x[2] == 3 and places_x[4] == 5 and places[6] and move == 2:
            place_o(6)
        elif places_x[2] == 3 and places_x[6] == 7 and places[4] and move == 2:
            place_o(4)
        elif places_x[4] == 5 and places_x[6] == 7 and places[2] and move == 2:
            place_o(2)
        # Fallback: если ни одно правило не сработало, поставим O в любую свободную клетку
        if not made_move:
            free_indices = [i for i, free in enumerate(places) if free]
            if free_indices:
                idx = random.choice(free_indices)
                places_o[idx] = idx + 1
                made_move = True
        # Если мы сделали ход — отметим это и сразу переключим ход на игрока
        if made_move:
            bot_moved = True
            move = 1
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Обработка клика игрока — только когда ход игрока и клетка свободна
        if event.type == pygame.MOUSEBUTTONDOWN:
            if move == 1:
                if place1.collidepoint(event.pos) and places[0]:
                    places_x[0] = 1
                    move = 2
                elif place2.collidepoint(event.pos) and places[1]:
                    places_x[1] = 2
                    move = 2
                elif place3.collidepoint(event.pos) and places[2]:
                    places_x[2] = 3
                    move = 2
                elif place4.collidepoint(event.pos) and places[3]:
                    places_x[3] = 4
                    move = 2
                elif place5.collidepoint(event.pos) and places[4]:
                    places_x[4] = 5
                    move = 2
                elif place6.collidepoint(event.pos) and places[5]:
                    places_x[5] = 6
                    move = 2
                elif place7.collidepoint(event.pos) and places[6]:
                    places_x[6] = 7
                    move = 2
                elif place8.collidepoint(event.pos) and places[7]:
                    places_x[7] = 8
                    move = 2
                elif place9.collidepoint(event.pos) and places[8]:
                    places_x[8] = 9
                    move = 2
    # Рендер
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 255, 255), place1)
    pygame.draw.rect(screen, (255, 255, 255), place2)
    pygame.draw.rect(screen, (255, 255, 255), place3)
    pygame.draw.rect(screen, (255, 255, 255), place4)
    pygame.draw.rect(screen, (255, 255, 255), place5)
    pygame.draw.rect(screen, (255, 255, 255), place6)
    pygame.draw.rect(screen, (255, 255, 255), place7)
    pygame.draw.rect(screen, (255, 255, 255), place8)
    pygame.draw.rect(screen, (255, 255, 255), place9)
    x.draw_x()
    # Обновляем доступность клеток перед решением бота
    free_places()
    # Если сейчас ход бота — выполните ход бота (с гарантированным fallback)
    if move == 2:
        o.move_o()
    o.draw_o()
    # Сбрасываем флаг bot_moved, он уже переключил move внутри move_o
    if bot_moved:
        bot_moved = False
    end()
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
