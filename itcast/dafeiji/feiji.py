# coding=utf-8
import pygame
import time
from pygame.locals import *

step = 5

class HeroPlane(object):
    def __init__(self):
        self.x = 100
        self.y = 300
        self.image = pygame.image.load("./feiji/hero.gif").convert()

    def display(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def move_left(self):
        self.x -= 5

    def move_right(self):
        self.x += 5

    def move_up(self):
        self.y -= 5
        
    def move_down(self):
        self.y += 5

def key_process(hero):
    # 判断是否是点击了退出按钮
    for event in pygame.event.get():
        # print(event.type)
        if event.type == QUIT:
            print("exit")
            exit()
        elif event.type == KEYDOWN:
            if event.key == K_a or event.key == K_LEFT:
                print('left')
                # 控制飞机让其向左移动
                hero.move_left()
            elif event.key == K_d or event.key == K_RIGHT:
                print('right')
                # 控制飞机让其向右移动
                hero.move_right()
            elif event.key == K_UP:
                print('up')
                hero.move_up()
            elif event.key == K_DOWN:
                print('down')
                hero.move_down()
            elif event.key == K_SPACE:
                print('space')

if __name__ == "__main__":
    # 1. 创建一个窗口，用来显示内容
    screen = pygame.display.set_mode((320, 480), 0, 32)

    # 2. 创建一个和窗口大小一样的图片，当做背景
    background = pygame.image.load("./feiji/background.png").convert()

    # 3. 创建飞机图片
    hero = HeroPlane()

    # 3. 把背景图放在窗口显示
    while True:
        screen.blit(background, (0, 0))
        hero.display(screen)

        key_process(hero)
        
        pygame.display.update()
        time.sleep(0.1)
