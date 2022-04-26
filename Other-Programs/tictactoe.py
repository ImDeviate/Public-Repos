#!/usr/bin/env python3

import pygame
pygame.init()

width, height = 900, 900
dis = pygame.display.set_mode((width, height))
title = pygame.display.set_caption("Tic-Tac-Toe")
fontstyle = pygame.font.SysFont("ariel", 40)

white = (255,255,255)
black = (0,0,0)
red = (255, 0, 0)
blue = (0,0, 255)
fps = 144

def draw_window():
    dis.fill(white)
    
    # Vertical Lines
    pygame.draw.line(dis, black, (300,0), (300,1000), width = 10)
    pygame.draw.line(dis, black, (600,0), (600,1000), width = 10)
    
    # Horizontal Lines
    pygame.draw.line(dis, black, (0,300), (1000,300), width = 10)
    pygame.draw.line(dis, black, (0,600), (1000,600), width = 10)

    pygame.display.update()

def draw_x(xpos,ypos):
    #xpos = xx//300
    #ypos = yy//300
    pygame.draw.line(dis, red, ((xpos * 300)+10, (ypos * 300)+290), ((xpos * 300)+290, (ypos * 300)+10),10)
    pygame.draw.line(dis, red, ((xpos * 300)+10, (ypos * 300)+10), ((xpos * 300)+290, (ypos * 300)+290),10)

    pygame.display.update()

def draw_o(xpos,ypos):
    #xpos = xxx//300
    #ypos = yyy//300
    pygame.draw.circle(dis, blue, ((xpos * 300)+150, (ypos * 300)+150), 140, 10)

    pygame.display.update()

def wincon(g):
    total = 0
    
    for i in range(0,3):
        total = sum(g[i])
        if total == 3 and 0 not in g[i]:
            return 'x'
        if total == 6 and 0 not in g[i]:
            return 'o'

    for i in range(0,3):
        total = 0
        lst = []
        for j in range(0,3):
            lst.append(g[j][i])
        total = sum(lst)
        if total == 3 and 0 not in lst:
            return 'x'
        if total == 6 and 0 not in lst:
            return 'o'

    lst = [g[0][0], g[1][1], g[2][2]]
    total = sum(lst)
    if total == 3 and 0 not in lst:
        return 'x'
    if total == 6 and 0 not in lst:
        return 'o'

    lst = [g[0][2], g[1][1], g[2][0]]
    total = sum(lst)
    if total == 3 and 0 not in lst:
        return 'x'
    if total == 6 and 0 not in lst:
        return 'o'

    return None

def winscreen(msg,color,pos):
    dis.fill(white)
    mesg = fontstyle.render(msg,True,color)
    dis.blit(mesg, [900/3, 900/pos])

    pygame.display.update()

def turn(coords, counter, grd):
    x, y = coords
    x = x // 300
    y = y // 300
    if grd[x][y] == 0:
        if counter % 2:
            grd[x][y] = 1
            draw_x(x,y)
        else:
            grd[x][y] = 2
            draw_o(x,y)
        
        winner = wincon(grd)
        if winner:
            print(f'winner is {winner}')
            winscreen(f'Congrats, the winner is {winner}!', red, 2)

    return grd

def main():
    clock = pygame.time.Clock()
    running = True
    grid = []
    xy = 0
    draw_window()

    for i in range(0,3):
        grid.append([])
        for j in range(0,3):
            grid[i].append(0)

    while running:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONUP:
                xy += 1
                grid = turn(pygame.mouse.get_pos(), xy, grid)        
                
    pygame.quit()

if __name__ == "__main__":
    main()