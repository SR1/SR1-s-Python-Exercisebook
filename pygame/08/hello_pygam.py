#!/usr/bin/python
#@coding=utf-8
#@source: crossin的编程教室13.18.15


# 导入pygame库
import pygame
# 从sys模块中导入exit()函数，用于退出程序
from sys import exit

# 初始化pygame，为使用硬件做准备
pygame.init()

# 创建一个窗口，窗口大小和背景图片大小一样
screen = pygame.display.set_mode((600,300),0,32)
# 设置窗口标题
pygame.display.set_caption('Hello, World!')
# 加载并转换图像
img1 = pygame.image.load('bg.jpg').convert()
img2 = pygame.image.load('bg2.jpg').convert()
plane = pygame.image.load('plane.png').convert()
background = img1

# 进入游戏主循环
while True:
    # 处理接收到的事件
    for event in pygame.event.get():
        # 接收到退出事件后退出程序
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if background == img1:
                background = img2
            else:
                background = img1
    # 将背景图画上去
    screen.blit(background,(0,0))
    x, y = pygame.mouse.get_pos()
    x -= plane.get_width()/2
    y -= plane.get_height()/2
    screen.blit(plane,(x, y))
    # 刷新画面
    pygame.display.update()
