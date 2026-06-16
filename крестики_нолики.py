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
o_img=pygame.transform.scale(o_img , (200 , 200))
places_x= [ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0]
places_o= [ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0]
places= [True]*9
move=1
running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running= False
    def free_places():
        if places_x[0] == 1 or places_o[0] == 1:
            places[0]=False
        if places_x[1] == 2 or places_o[1] == 2:
            places[1]=False
        if places_x[2] == 3 or places_o[2] == 3:
            places[2]=False
        if places_x[3] == 4 or places_o[3] == 4:
            places[3]=False
        if places_x[4] == 5 or places_o[4] == 5:
            places[4]=False
        if places_x[5] == 6 or places_o[5] == 6:
            places[5]=False
        if places_x[6] == 7 or places_o[6] == 7:
            places[6]=False
        if places_x[7] == 8 or places_o[7] == 8:
            places[7]=False
        if places_x[8] == 9 or places_o[8] == 9:
            places[8]=False
    class x():
        def draw_x():   
                if places_x[0] == 1 :
                    screen.blit(x_img , (0 , 0))
                    move=2
                if places_x[1] == 2 :
                    screen.blit(x_img , (210 , 0))
                    move=2
                if places_x[2] == 3 :
                    screen.blit(x_img , (420 , 0))
                    move=2
                if places_x[3] == 4 :
                    screen.blit(x_img , (0 , 210))
                    move=2
                if places_x[4] == 5 :
                    screen.blit(x_img , (210 , 210))
                    move=2
                if places_x[5] == 6 :
                    screen.blit(x_img , (420 , 210))
                    move=2
                if places_x[6] == 7 :
                    screen.blit(x_img , (0 , 420))
                    move=2
                if places_x[7] == 8 :
                    screen.blit(x_img , (210 , 420))
                    move=2
                if places_x[8] == 9 :
                    screen.blit(x_img , (420 , 420))
                    move=2
    class o():
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
            def move_o():
                global move
                if places_x[0] == 1 and places[8] == True and move == 2:
                    places_o[8]=9
                    move=1
                if places_x[2] == 3 and places[6] == True and move == 2:
                    places_o[6]=7
                    move=1
                if places_x[6] == 7 and places[2] == True and move == 2:
                    places_o[2]=3
                    move=1
                if places_x[8] == 9 and places[0] == True and move == 2:
                    places_o[0]=1
                    move=1
                else:
                    if places_x[1] == 2 or places_x[3] == 4 or places_x[5] == 6 or places_x[7] == 8 and places[4] == True and move == 2:
                        places_o[4]=5
                        move=1
                if places_x[0] == 1 and places_x[1] == 2 and places[2] == True and move == 2:
                    places_o[2]=3
                    move=1
                elif places_x[0] == 1 and places_x[2] == 3 and places[1] == True and move == 2:
                    places_o[1]=2
                    move=1
                elif places_x[1] == 2 and places_x[2] == 3 and places[0] == True and move == 2:
                    places_o[0]=1
                    move=1
                elif places_x[3] == 4 and places_x[4] == 5 and places[5] == True and move == 2:
                    places_o[5]=6
                    move=1
                elif places_x[3] == 4 and places_x[5] == 6 and places[4] == True and move == 2:
                    places_o[4]=5
                    move=1
                elif places_x[4] == 5 and places_x[5] == 6 and places[3] == True and move == 2:
                    places_o[3]=4
                    move=1
                elif places_x[6] == 7 and places_x[7] == 8 and places[8] == True and move == 2:
                    places_o[8]=9
                    move=1
                elif places_x[6] == 7 and places_x[8] == 9 and places[7] == True and move == 2:
                    places_o[7]=8
                    move=1
                elif places_x[7] == 8 and places_x[8] == 9 and places[6] == True and move == 2:
                    places_o[6]=7
                    move=1
                elif places_x[0] == 1 and places_x[3] == 4 and places[6] == True and move == 2:
                    places_o[6]=7
                    move=1
                elif places_x[0] == 1 and places_x[6] == 7 and places[3] == True and move == 2:
                    places_o[3]=4
                    move=1
                elif places_x[3] == 4 and places_x[6] == 7 and places[0] == True and move == 2:
                    places_o[0]=1
                    move=1
                elif places_x[1] == 2 and places_x[4] == 5 and places[7] == True and move == 2:
                    places_o[7]=8
                    move=1
                elif places_x[1] == 2 and places_x[7] == 8 and places[4] == True and move == 2:
                    places_o[4]=5
                    move=1
                elif places_x[4] == 5 and places_x[7] == 8 and places[1] == True and move == 2:
                    places_o[1]=2
                    move=1
                elif places_x[0] == 1 and places_x[4] == 5 and places[8] == True and move == 2:
                    places_o[8]=9
                    move=1
                elif places_x[0] == 1 and places_x[8] == 9 and places[4] == True and move == 2:
                    places_o[4]=5
                    move=1
                elif places_x[4] == 5 and places_x[8] == 9 and places[0] == True and move == 2:
                    places_o[0]=1
                    move=1
                elif places_x[2] == 3 and places_x[4] == 5 and places[6] == True and move == 2:
                    places_o[6]=7
                    move=1
                elif places_x[2] == 3 and places_x[6] == 7 and places[4] == True and move == 2:
                    places_o[4]=5
                    move=1
                elif places_x[4] == 5 and places_x[6] == 7 and places[2] == True and move == 2:
                    places_o[2]=3
                    move=1
    if event.type == pygame.MOUSEBUTTONDOWN:
            if place1.collidepoint(event.pos) and move == 1:
                places_x[0]=1
            if place2.collidepoint(event.pos) and move == 1:
                places_x[1]=2
            if place3.collidepoint(event.pos) and move == 1:
                places_x[2]=3
            if place4.collidepoint(event.pos) and move == 1:
                places_x[3]=4
            if place5.collidepoint(event.pos) and move == 1:
                places_x[4]=5
            if place6.collidepoint(event.pos) and move == 1:
                places_x[5]=6
            if place7.collidepoint(event.pos) and move == 1:
                places_x[6]=7
            if place8.collidepoint(event.pos) and move == 1:
                places_x[7]=8
            if place9.collidepoint(event.pos) and move == 1:
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
    free_places()
    x.draw_x()
    o.move_o()
    o.draw_o()
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
