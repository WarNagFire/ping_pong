from pygame import *
from random import randint
from time import time as timer
from time import sleep


a = 0
b = 0


mw = display.set_mode((700,500))
display.set_caption('Ping_pong')
background = transform.scale(image.load('backgroud.png'),(700,500))


class GameSprite(sprite.Sprite):
    def __init__(self,image_player,rect_x,rect_y,speed):
        super().__init__()
        self.image = transform.scale(image.load(image_player),(65,65))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = rect_x
        self.rect.y = rect_y
    def reset(self):
        mw.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def update_left()
        key = keys.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed

class PLayer1(GameSprite):
    def update_right()
        key = keys.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        
    bullets.update()
    bullets.draw(mw)
    display.update()
    clock.tick(45)