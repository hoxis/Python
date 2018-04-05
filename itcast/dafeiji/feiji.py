# coding=utf-8
import pygame
import time
import random
from pygame.locals import *

step = 5


class HeroPlane(object):
    def __init__(self):
        self.x = 100
        self.y = 350
        self.image = pygame.image.load("./feiji/hero.gif").convert()

        # 用来存储飞机发射的所有子弹
        self.bullets = []

    def display(self, screen):
        screen.blit(self.image, (self.x, self.y))
        # 存储最终要显示的子弹
        finalBullets = []
        # 判断子弹是否越界，越界的进行剔除
        for bullet in self.bullets:
            if bullet.isInScreen():
                finalBullets.append(bullet)
        self.bullets = finalBullets

        # 显示子弹
        for bullet in self.bullets:
            bullet.display(screen)
            bullet.move()

    def move_left(self):
        self.x -= step

    def move_right(self):
        self.x += step

    def move_up(self):
        self.y -= step

    def move_down(self):
        self.y += step

    def add_bullet(self):
        bullet = Bullet(self.x+43.5, self.y+20, "./feiji/bullet-3.gif", "up")
        self.bullets.append(bullet)


class Bullet(object):
    def __init__(self, x, y, imageName, direction):
        self.x = x
        self.y = y
        self.direction = direction
        self.imageName = imageName
        self.image = pygame.image.load(imageName).convert()

    def display(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def move(self):
        if self.direction == "up":
            self.y -= step*2
        elif self.direction == "down":
            self.y += step*2

    def isInScreen(self):
        if self.y < 0 or self.x < 0 or self.y > 480 or self.x > 320:
            return False
        else:
            return True


class EnemyPlane(object):
    def __init__(self):
        self.x = 0
        self.y = 0
        # 存储飞机的移动方向
        self.direction = "right"
        self.image = pygame.image.load("./feiji/enemy-1.gif").convert()

        # 用来存储飞机发射的所有子弹
        self.bullets = []

    def display(self, screen):
        screen.blit(self.image, (self.x, self.y))
        # 存储最终要显示的子弹
        finalBullets = []
        # 判断子弹是否越界，越界的进行剔除
        for bullet in self.bullets:
            if bullet.isInScreen():
                finalBullets.append(bullet)
        self.bullets = finalBullets

        # 显示子弹
        for bullet in self.bullets:
            bullet.display(screen)
            bullet.move()

    def move(self):
        if self.x >= 320 - 50:
            self.direction = "left"
        elif self.x <= 0:
            self.direction = "right"

        if self.direction == "left":
            self.x -= step
        else:
            self.x += step

    def add_bullet(self):
        num = random.randint(1, 100)
        if num == 88:
            bullet = Bullet(self.x+10, self.y+10,
                            "./feiji/bullet-1.gif", "down")
            self.bullets.append(bullet)


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
        enemy.move()
        enemy.add_bullet()

        key_process(hero)

        pygame.display.update()

        # 通过延时的方式，来降低这个while循环的循环速度，从而降低了cpu占用率
        time.sleep(0.1)
