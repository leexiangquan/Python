import pygame, sys

pygame.init()
size = width, height = 600, 600
speed1 = [1, 1]
speed2 = [1, 1]
BLACK = 0, 0, 0
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pygame壁球")
ball1 = pygame.image.load("PYG02-ball.gif")
ballrect1 = ball1.get_rect()
ball2 = pygame.image.load("haili.png")
ballrect2 = ball2.get_rect()
ballrect2.right = width

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    ballrect1 = ballrect1.move(speed1[0], speed1[1])
    ballrect2 = ballrect2.move(speed2[0], speed2[1])
    if ballrect1.left < 0 or ballrect1.right > width:
        speed1[0] = -speed1[0]
    if ballrect1.top < 0 or ballrect1.bottom > height:
        speed1[1] = -speed1[1]
    if ballrect2.left < 0 or ballrect2.right > width:
        speed2[0] = -speed2[0]
    if ballrect2.top < 0 or ballrect2.bottom > height:
        speed2[1] = -speed2[1]
    if ballrect1.right - ballrect2.left == 0 or ballrect1.left - ballrect2.right == 0:
        speed1[0] = -speed1[0]
        speed2[0] = -speed2[0]
    if ballrect1.top - ballrect2.bottom == 0 or ballrect1.bottom - ballrect2.top == 0:
        speed1[1] = -speed1[1]
        speed2[1] = -speed2[1]

    screen.fill(BLACK)
    screen.blit(ball1, ballrect1)
    screen.blit(ball2, ballrect2)
    pygame.display.update()