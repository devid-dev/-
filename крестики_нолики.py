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
running = True
def end():
    #конец игры
    if (places_o[0] == 1 and places_o[1] == 2 and places_o[2] == 3) or (places_o[3] == 4 and places_o[4] == 5 and places_o[5] == 6):
        print('победа компьютера')
        move=2
    if (places_o[6] == 7 and places_o[7] == 8 and places_o[8] == 9) or (places_o[0] == 1 and places_o[3] == 4 and places_o[6] == 7):
        print('победа компьютера')
        move=2
    if (places_o[1] == 2 and places_o[4] == 5 and places_o[7] == 8) or (places_o[2] == 3 and places_o[5] == 6 and places_o[8] == 9):
        print('победа компьютера')
    if (places_o[2] == 3 and places_o[4] == 5 and places_o[6] == 7) or (places_o[0] == 1 and places_o[4] == 5 and places_o[8] == 9):
        print('победа компьютера')
        move=2
    if (places_x[0] == 1 and places_x[1] == 2 and places_x[2] == 3) or (places_x[3] == 4 and places_x[4] == 5 and places_x[5] == 6):
        print('победа игрока')
        move=1
    if (places_x[6] == 7 and places_x[7] == 8 and places_x[8] == 9) or (places_x[0] == 1 and places_x[3] == 4 and places_x[6] == 7):
        print('победа игрока')
        move=1
    if (places_x[1] == 2 and places_x[4] == 5 and places_x[7] == 8) or (places_x[2] == 3 and places_x[5] == 6 and places_x[8] == 9):
        print('победа игрока')
        move=1
    if (places_x[2] == 3 and places_x[4] == 5 and places_x[6] == 7) or (places_x[0] == 1 and places_x[4] == 5 and places_x[8] == 9):
        print('победа игрока')
        move=1
    else:
        if places == [False]*9:
            print('ничья')
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
        # Логика бота
        if (places_x[1] == 2 and places[0] and places_x[0] == 0 and places[2] and places_x[2] == 0) or (places_x[3] == 4 and places[0] and places_x[0] == 0 and places_x[6] == 0):
            places_o[4] = 5
            made_move = True
        elif places_x[0] == 1 and places[8] and places[1] and places[3] and places[6] and move == 2:
            places_o[8] = 9
            made_move = True
        elif places_x[2] == 3 and places[6] and places[1] and places[5] and places[8] and places[0] and move == 2:
            places_o[6] = 7
            made_move = True
        elif places_x[6] == 7 and places[2] and places[3] and places[7] and places[8] and places[0] and move == 2:
            places_o[2] = 3
            made_move = True
        elif places_x[8] == 9 and places[0] and places[5] and places[7] and places[6] and places[2] and move == 2:
            places_o[0] = 1
            made_move = True
        elif places_x[0] == 1 and places_x[1] == 2 and places[2] and places_x[3] == 0 and places_x[4] == 0 and move == 2:
            places_o[2] = 3
            made_move = True
        elif places_x[0] == 1 and places_x[2] == 3 and places[1] and move == 2:
            places_o[1] = 2
            made_move = True
        elif places_x[1] == 2 and places_x[2] == 3 and places[0] and move == 2:
            places_o[0] = 1
            made_move = True
        elif places_x[3] == 4 and places_x[4] == 5 and places[5] and places_x[1] == 0 and move == 2:
            places_o[5] = 6
            made_move = True
        elif places_x[3] == 4 and places_x[5] == 6 and places[4] and move == 2:
            places_o[4] = 5
            made_move = True
        elif places_x[4] == 5 and places_x[5] == 6 and places[3] and move == 2:
            places_o[3] = 4
            made_move = True
        elif places_x[6] == 7 and places_x[7] == 8 and places[8] and move == 2:
            places_o[8] = 9
            made_move = True
        elif places_x[6] == 7 and places_x[8] == 9 and places[7] and move == 2:
            places_o[7] = 8
            made_move = True
        elif places_x[7] == 8 and places_x[8] == 9 and places[6] and move == 2:
            places_o[6] = 7
            made_move = True
        elif places_x[0] == 1 and places_x[3] == 4 and places[6] and move == 2:
            places_o[6] = 7
            made_move = True
        elif places_x[0] == 1 and places_x[6] == 7 and places[3] and move == 2:
            places_o[3] = 4
            made_move = True
        elif places_x[3] == 4 and places_x[6] == 7 and places[0] and move == 2:
            places_o[0] = 1
            made_move = True
        elif places_x[1] == 2 and places_x[4] == 5 and places[7] and move == 2:
            places_o[7] = 8
            made_move = True
        elif places_x[1] == 2 and places_x[7] == 8 and places[4] and move == 2:
            places_o[4] = 5
            made_move = True
        elif places_x[4] == 5 and places_x[7] == 8 and places[1] and move == 2:
            places_o[1] = 2
            made_move = True
        elif places_x[0] == 1 and places_x[4] == 5 and places[8] and move == 2:
            places_o[8] = 9
            made_move = True
        elif places_x[0] == 1 and places_x[8] == 9 and places[4] and move == 2:
            places_o[4] = 5
            made_move = True
        elif places_x[4] == 5 and places_x[8] == 9 and places[0] and move == 2:
            places_o[0] = 1
            made_move = True
        elif places_x[2] == 3 and places_x[4] == 5 and places[6] and move == 2:
            places_o[6] = 7
            made_move = True
        elif places_x[2] == 3 and places_x[6] == 7 and places[4] and move == 2:
            places_o[4] = 5
            made_move = True
        elif places_x[4] == 5 and places_x[6] == 7 and places[2] and move == 2:
            places_o[2] = 3
            made_move = True
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
