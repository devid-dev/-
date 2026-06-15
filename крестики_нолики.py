import pygame
pygame.init()
screen=pygame.display.set_mode((620 , 620))
clock=pygame.time.Clock()
place1=pygame.Rect(0 , 0 , 200 , 200)
place2=pygame.Rect(210 , 0 , 200 , 200)
place3=pygame.Rect(420 , 0 , 200 , 200)
place4=pygame.Rect(0 , 210 , 200 , 200)
place5=pygame.Rect(210 , 210 , 200 , 200)
place6=pygame.Rect(420 , 210 , 200 , 200)
place7=pygame.Rect(0 , 420 , 200 , 200)
place8=pygame.Rect(210 , 420 , 200 , 200)
place9=pygame.Rect(420 , 420 , 200 , 200)
x_img=pygame.image.load("x.png")
x_img=pygame.transform.scale(x_img , (200 , 200))
o_img=pygame.image.load("o.png")
places_x= [ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0]
places_o= [ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0]
running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running= False
    class x():
        move=1
        def draw_x():
                if places_x[0] == 1 and x.move == 1 :
                    screen.blit(x_img , (0 , 0))
                    x.move=2
                if places_x[1] == 2 and x.move == 1:
                    screen.blit(x_img , (210 , 0))
                    x.move=2
                if places_x[2] == 3 and x.move == 1:
                    screen.blit(x_img , (420 , 0))
                    x.move=2
                if places_x[3] == 4 and x.move == 1:
                    screen.blit(x_img , (0 , 210))
                    x.move=2
                if places_x[4] == 5 and x.move == 1:
                    screen.blit(x_img , (210 , 210))
                    x.move=2
                if places_x[5] == 6 and x.move == 1:
                    screen.blit(x_img , (420 , 210))
                    x.move=2
                if places_x[6] == 7 and x.move == 1:
                    screen.blit(x_img , (0 , 420))
                    x.move=2
                if places_x[7] == 8 and x.move == 1:
                    screen.blit(x_img , (210 , 420))
                    x.move=2
                if places_x[8] == 9 and x.move == 1:
                    screen.blit(x_img , (420 , 420))
                    x.move=2
    class o():
            def move_o():
                if places_x[0] == 1 and x.move == 2:
                    places_o[8]=9
                if places_x[2] == 3 and x.move == 2:
                    places_o[6]=7
                if places_x[6] == 7 and x.move == 2:
                    places_x[2]=3
                if places_x[8] == 9 and x.move == 2:
                    places_o[0]=1
                else:
                    if places_x[1] == 2 or places_x[3] == 4 or places_x[5] == 6 or places_x[7] == 8 and x.move == 2:
                        places_o[4]=5
                if places_x[0] == 1 and places_x[1] == 2 and x.move == 2:
                    places_o[2]=3
                if places_x[0] == 1 and places_x[2] == 3 and x.move == 2:
                    places_o[1]=2
                if places_x[1] == 2 and places_x[2] == 3 and x.move == 2:
                    places_o[0]=1
                if places_x[3] == 4 and places_x[4] == 5 and x.move == 2:
                    places_o[5]=6
                if places_x[3] == 4 and places_x[5] == 6 and x.move == 2:
                    places_o[4]=5
                if places_x[4] == 5 and places_x[5] == 6 and x.move == 2:
                    places_o[3]=4
                if places_x[6] == 7 and places_x[7] == 8 and x.move == 2:
                    places_o[8]=9
                if places_x[6] == 7 and places_x[8] == 9 and x.move == 2:
                    places_o[7]=8
                if places_x[7] == 8 and places_x[8] == 9 and x.move == 2:
                    places_o[6]=7
                if places_x[0] == 1 and places_x[3] == 4 and x.move == 2:
                    places_o[6]=7
                if places_x[0] == 1 and places_x[6] == 7 and x.move == 2:
                    places_o[3]=4
                if places_x[3] == 4 and places_x[6] == 7 and x.move == 2:
                    places_o[0]=1
                if places_x[1] == 2 and places_x[4] == 5 and x.move == 2:
                    places_o[7]=8
                if places_x[1] == 2 and places_x[7] == 8 and x.move == 2:
                    places_o[4]=5
                if places_x[4] == 5 and places_x[7] == 8 and x.move == 2:
                    places_o[1]=2
                if places_x[0] == 1 and places_x[4] == 5 and x.move == 2:
                    places_o[8]=9
                if places_x[0] == 1 and places_x[8] == 9 and x.move == 2:
                    places_o[4]=5
                if places_x[4] == 5 and places_x[8] == 9 and x.move == 2:
                    places_o[0]=1
                if places_x[2] == 3 and places_x[4] == 5 and x.move == 2:
                    places_o[6]=7
                if places_x[2] == 3 and places_x[6] == 7 and x.move == 2:
                    places_o[4]=5
                if places_x[4] == 5 and places_x[6] == 7 and x.move == 2:
                    places_o[2]=3
                else:
                    if places_o[8] == 9 and places_x[7] == 0 and x.move == 2:
                        places_o[7]=8
                    if places_o[8] == 9 and places_o[7] == 8 and places_x[6] == o and x.move == 2:
                        places_o[6]=7
                    else:
                        if places_o[8] == 9 and places_x[5] == 0 and x.move == 2:
                            places_o[5]=6
                        if places_o[8] == 9 and places_o[5] == 6 and places_x[2] == 0 and x.move == 2:
                            places_o[2]=3
            def draw_o():
                if places_o[0] == 1 :
                    screen.blit(o_img , (0 , 0))
                if places_o[1] == 2 :
                    screen.blit(o_img , (210 , 0))
                if places_o[2] == 3 :
                    screen.blit(o_img , (420 , 0))
                if places_o[3] == 4 :
                    screen.blit(o_img , (0 , 210))
                if places_o[4] == 5 :
                    screen.blit(o_img , (210 , 210))
                if places_o[5] == 6 :
                    screen.blit(o_img , (420 , 210))
                if places_o[6] == 7 :
                    screen.blit(o_img , (0 , 420))
                if places_o[7] == 8 :
                    screen.blit(o_img , (210 , 420))
                if places_o[8] == 9 :
                    screen.blit(o_img , (420 , 420))
    draw_o()
    if event.type == pygame.MOUSEBUTTONDOWN:
            if place1.collidepoint(event.pos):
                places_x[0]=1
            if place2.collidepoint(event.pos):
                places_x[1]=2
            if place3.collidepoint(event.pos):
                places_x[2]=3
            if place4.collidepoint(event.pos):
                places_x[3]=4
            if place5.collidepoint(event.pos):
                places_x[4]=5
            if place6.collidepoint(event.pos):
                places_x[5]=6
            if place7.collidepoint(event.pos):
                places_x[6]=7
            if place8.collidepoint(event.pos):
                places_x[7]=8
            if place9.collidepoint(event.pos):
                places_x[8]=9
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255 , 255 , 255),place1)
    pygame.draw.rect(screen, (255 , 255 , 255),place2)
    pygame.draw.rect(screen, (255 , 255 , 255),place3)
    pygame.draw.rect(screen, (255 , 255 , 255),place4)
    pygame.draw.rect(screen, (255 , 255 , 255),place5)
    pygame.draw.rect(screen, (255 , 255 , 255),place6)
    pygame.draw.rect(screen, (255 , 255 , 255),place7)
    pygame.draw.rect(screen, (255 , 255 , 255),place8)
    pygame.draw.rect(screen, (255 , 255 , 255),place9)
    x.draw_x()
    o.draw_o()
    pygame.display.flip()
    clock.tick(60)
pygame.quit()

