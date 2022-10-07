from tkinter import EventType
import pygame
from pygame.locals import *
import sys
import random
pygame.init()
run = True
yükseklik = 600
geniþlik = 600
yeþil = (0,255,0)
kýrmýzý = (255,0,0)
mavi = (0,0,255)
beyaz = (255,255,255)
siyah = (0,0,0)
lacivert = (7,19,48)
dice_rolled = 0
clicked = 0
font = pygame.font.SysFont("arial",20)
pygame.display.set_caption('Dice Game')
screen_1 = pygame.display.set_mode((geniþlik,yükseklik))
d_4_rect = Rect(50, 50, 75, 50)
d_6_rect = Rect(50, 125, 75, 50)
d_8_rect = Rect(50, 200, 75, 50)
d_10_rect= Rect(50, 275, 75, 50)
d_12_rect= Rect(50, 350, 75, 50)
d_20_rect= Rect(50, 425, 75, 50)
d_100_rect = Rect(50, 500, 75, 50)

def draw_button():
    screen_1.fill(lacivert)
    d_4_text = '1d4'
    d_6_text = '1d6'
    d_8_text = '1d8'
    d_10_text = '1d10'
    d_12_text = '1d12'
    d_20_text = '1d20'
    d_100_text = '1d100'
    d_4_img = font.render(d_4_text, True, beyaz)
    d_6_img = font.render(d_6_text, True, beyaz)
    d_8_img = font.render(d_8_text, True, beyaz)
    d_10_img = font.render(d_10_text, True, beyaz)
    d_12_img = font.render(d_12_text, True, beyaz)
    d_20_img = font.render(d_20_text, True, beyaz)
    d_100_img = font.render(d_100_text, True, beyaz)
    pygame.draw.rect(screen_1, mavi, d_4_rect)
    screen_1.blit(d_4_img,(75,65))
    pygame.draw.rect(screen_1,mavi,d_6_rect)
    screen_1.blit(d_6_img,(75,140))
    pygame.draw.rect(screen_1,mavi,d_8_rect)
    screen_1.blit(d_8_img,(75,215))
    pygame.draw.rect(screen_1,mavi,d_10_rect)
    screen_1.blit(d_10_img,(70,290))
    pygame.draw.rect(screen_1,mavi,d_12_rect)
    screen_1.blit(d_12_img,(70,365))
    pygame.draw.rect(screen_1,mavi,d_20_rect)
    screen_1.blit(d_20_img,(70,440))
    pygame.draw.rect(screen_1,mavi,d_100_rect)
    screen_1.blit(d_100_img,(65,515))

draw_button()
while run :
    
    #
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False
            sys.exit()
        if dice_rolled == 0:
            if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
                clicked = True
            if event.type == pygame.MOUSEBUTTONUP and clicked == True:
                clicked = False
                pos = pygame.mouse.get_pos()
                if d_4_rect.collidepoint(pos):
                    d_4_dice = random.randint(1,4)
                    d_4_dice_str = str(d_4_dice)
                    d_4_dice_img = font.render(d_4_dice_str, True , beyaz)
                    pygame.draw.rect(screen_1, kýrmýzý,(375, 50, 50, 50))
                    screen_1.blit(d_4_dice_img,(geniþlik // 2 +95, 65))    
                if d_6_rect.collidepoint(pos):
                    d_6_dice = random.randint(1,6)
                    d_6_dice_str = str(d_6_dice)
                    d_6_dice_img = font.render(d_6_dice_str, True, beyaz)
                    pygame.draw.rect(screen_1, kýrmýzý,(375,125,50,50))
                    screen_1.blit(d_6_dice_img,(geniþlik //2 +95 ,140))
                if d_8_rect.collidepoint(pos):
                    d_8_dice = random.randint(1,8)
                    d_8_dice_str = str(d_8_dice)
                    d_8_dice_img = font.render(d_8_dice_str ,True, beyaz)
                    pygame.draw.rect(screen_1, kýrmýzý,(375,200,50,50))
                    screen_1.blit(d_8_dice_img,(geniþlik // 2 +95 ,215))
                if d_10_rect.collidepoint(pos):
                    d_10_dice = random.randint(1,10)
                    d_10_dice_str = str(d_10_dice)
                    d_10_dice_img = font.render(d_10_dice_str, True, beyaz)
                    pygame.draw.rect(screen_1, kýrmýzý,(372,275,56,50))
                    screen_1.blit(d_10_dice_img,(geniþlik // 2 +95,290))
                if d_12_rect.collidepoint(pos):
                    d_12_dice = random.randint(1,12)
                    d_12_dice_str = str(d_12_dice)
                    d_12_dice_img = font.render(d_12_dice_str, True, beyaz)
                    pygame.draw.rect(screen_1, kýrmýzý,(372,350,56,50))
                    screen_1.blit(d_12_dice_img,(geniþlik // 2 +95,365))
                if d_20_rect.collidepoint(pos):
                    d_20_dice = random.randint(1,20)
                    d_20_dice_str = str(d_20_dice)
                    d_20_dice_img = font.render(d_20_dice_str, True, beyaz)
                    pygame.draw.rect(screen_1, kýrmýzý,(372,425,56,50))
                    screen_1.blit(d_20_dice_img,(geniþlik // 2 +95,440))
                if d_100_rect.collidepoint(pos):
                    d_100_dice = random.randint(1,100)
                    d_100_dice_str = str(d_100_dice)
                    d_100_dice_img = font.render(d_100_dice_str, True, beyaz)
                    pygame.draw.rect(screen_1, kýrmýzý,(371,500,60,50))
                    screen_1.blit(d_100_dice_img,(geniþlik // 2 +95,515))



    pygame.display.update()    
    
pygame.quit()
