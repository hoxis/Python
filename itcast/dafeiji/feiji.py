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

        # 用来存储英雄飞机发射的所有子弹
        self.bullets = []

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
    
    def add_bullet(self):
        bullet = Bullet(hero.x+5, hero.y+20)
        self.bullets.append(bullet)

class Bullet(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = pygame.image.load("./feiji/bullet-3.gif").convert()

    def display(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.y -= 5

    def isInScreen(self):
        if self.y < 0 or self.x < 0:
            return False
        else:
            return True

class EnemyPlane(object):
    def __init__(self):
        self.x = 0
        self.y = 0
        self.image = pygame.image.load("./feiji/enemy-1.gif").convert()

    def display(self, screen):
        screen.blit(self.image, (self.x, self.y))

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
                hero.add_bullet()

if __name__ == "__main__":
    # 创建一个窗口，用来显示内容
    screen = pygame.display.set_mode((320, 480), 0, 32)

    # 创建一个和窗口大小一样的图片，当做背景
    background = pygame.image.load("./feiji/background.png").convert()

    # 创建飞机
    hero = HeroPlane()

    # 创建敌机
    enemy = EnemyPlane()

    # 把背景图放在窗口显示
    while True:
        screen.blit(background, (0, 0))

        # 显示飞机
        hero.display(screen)

        enemy.display(screen)

        # 存储最终要显示的子弹
        finalBullets = []

        # 判断子弹是否出界
        for bullet in hero.bullets:
            if bullet.isInScreen():
                finalBullets.append(bullet)

        # 显示子弹
        for bullet in finalBullets:
            bullet.display(screen)
            bullet.move()

        key_process(hero)
        
        pygame.display.update()
        time.sleep(0.1)
