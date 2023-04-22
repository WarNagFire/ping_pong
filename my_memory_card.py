from pygame import *
from random import randint
from time import time as timer
from time import sleep


a = 0
b = 0


mw = display.set_mode((700,500))
display.set_caption('Galasxy Strike')
background = transform.scale(image.load('galaxy.jpg'),(700,500))



mixer.init()
mixer.music.load('space.ogg')
kick = mixer.Sound('fire.ogg')
mixer.music.play()
font.init()
bullets = sprite.Group()
start_time = 0
real_time = 0





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


class GameSprite1(sprite.Sprite):
    def __init__(self,image_player,rect_x,rect_y,speed):
        super().__init__()
        self.image = transform.scale(image.load(image_player),(40,40))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = rect_x
        self.rect.y = rect_y
    def reset(self):
        mw.blit(self.image,(self.rect.x,self.rect.y))
    def update(self):
        if self.rect.y < 500:
            self.rect.y += self.speed
        else:
            self.rect.x = randint(0,550)
            self.rect.y = 0


class UFO(GameSprite):
    def update(self):
        global a
        if self.rect.y < 500:
            self.rect.y += self.speed
        else:
            a += 1
            self.rect.x = randint(0,550)
            self.rect.y = 0



class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
    
        if keys_pressed[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_d] and self.rect.x < 595:
            self.rect.x += self.speed     
    def Fire(self):
        global abc
        bull = bullet('bullet.png',Rocket.rect.centerx, Rocket.rect.top,14)
        bullets.add(bull)
        kick.play()
        abc += 1
        
        


        

class bullet(sprite.Sprite):
    def __init__(self,image_player,rect_x,rect_y,speed):
        super().__init__()
        self.image = transform.scale(image.load(image_player),(20,20))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = rect_x
        self.rect.y = rect_y
    def update(self):
        self.rect.y -= self.speed
        if self.rect.bottom < 0:
            self.kill()
        global b
        if sprite.spritecollide(plate,bullets,True):
            plate.rect.x = randint(0,550)
            plate.rect.y = 0
            b += 1
        elif sprite.spritecollide(plate1,bullets,True):
            plate1.rect.x = randint(0,550)
            plate1.rect.y = 0
            b += 1
        elif sprite.spritecollide(plate2,bullets,True):
            plate2.rect.x = randint(0,550)
            plate2.rect.y = 0
            b += 1
        elif sprite.spritecollide(plate3,bullets,True):
            plate3.rect.x = randint(0,550)
            plate3.rect.y = 0
            b += 1
        elif sprite.spritecollide(plate4,bullets,True):
            plate4.rect.x = randint(0,550)
            plate4.rect.y = 0
            b += 1

Rocket = Player('rocket.png',300,395,10)
plate = UFO('ufo.png',randint(0,550),0,1)
plate1 = UFO('ufo.png',randint(0,550),0,2)
plate2 = UFO('ufo.png',randint(0,550),0,3)
plate3 = UFO('ufo.png',randint(0,550),0,4)
plate4 = UFO('ufo.png',randint(0,550),0,5)
Asteroid = GameSprite1('asteroid.png',randint(0,550),0,1)
Asteroid1 = GameSprite1('asteroid.png',randint(0,550),0,2)
Asteroid2 = GameSprite1('asteroid.png',randint(0,550),0,3)
font.init()
font = font.Font(None,30)



clock = time.Clock()
run = True
ray = True
abc = 0

while run:
    display.update()
    clock.tick(45)
    win = font.render('Уничтоженно:'+str(b),True,(255,255,255))
    over = font.render('Пропущено:'+str(a),True,(255,255,255))
    win1 = font.render('RAAAMPAAAGE!',True,(255,215,0))
    over1 = font.render('LUUUSEEEEER',True,(255,0,0))
    mw.blit(background,(0,0))
    Rocket.reset()
    Rocket.update()
    plate.reset()
    plate.update()
    plate1.reset()
    plate1.update()
    plate2.reset()
    plate2.update()
    plate3.reset()
    plate3.update()
    plate4.update()
    Asteroid.reset()
    Asteroid1.reset()
    Asteroid2.reset()
    Asteroid.update()
    Asteroid1.update()
    Asteroid2.update()
    mw.blit(win,(0,10))
    mw.blit(over,(0,50))

    if sprite.collide_rect(Rocket,plate) or sprite.collide_rect(Rocket,plate1) or sprite.collide_rect(Rocket,plate2) or sprite.collide_rect(Rocket,plate3) or sprite.collide_rect(Rocket,plate4):
        run = False

    if a == 5:
        mw.blit(over1,(250,250))
        sleep(0.1)
        run = False
    
    if b == 10:
        mw.blit(win1,(250,250))
        sleep(0.1)
        run = False


    for e in event.get():
        if e.type == QUIT:
            run = False
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                if ray == True:
                    Rocket.Fire()

    bullets.update()
    bullets.draw(mw)
    display.update()
    clock.tick(45)
