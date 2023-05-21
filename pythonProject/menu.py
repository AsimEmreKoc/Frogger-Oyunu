import pygame,sys,time
import mysql.connector
from pygame.locals import *
from sys import exit

startTime = time.time()
pygame.init()
pygame.mixer.init()
WIDTH = 448
HEIGHT = 546
screen=pygame.display.set_mode([WIDTH,HEIGHT])

fps = 60
timer = pygame.time.Clock()
pygame.display.set_caption('Frogger')
main_menu = True
font = pygame.font.Font('freesansbold.ttf', 24)
bg = pygame.transform.scale(pygame.image.load('images/bg.png'), (448, 546))
logo = pygame.transform.scale(pygame.image.load('images/logo.png'), (300, 100))
ball = pygame.transform.scale(pygame.image.load('images/bg.png'), (150, 150))
lotus = pygame.transform.scale(pygame.image.load('images/lotusleaf.png'), (100,100))
bg1 = pygame.transform.scale(pygame.image.load('images/bg2.png'), (448, 546))
font_name = pygame.font.get_default_font()
point_font = pygame.font.SysFont(font_name, 35)
clock = pygame.time.Clock()
menu_command = 0
base_font = pygame.font.Font(None, 32)
user_text = ''
input_rect = pygame.Rect(170, 220, 10, 32)
color_active = pygame.Color('white')
color_passive = pygame.Color('white')
color = color_passive
active = False

oyunMuzigi = pygame.mixer.Sound('./sounds/guimo.wav')
arabaCarpma = pygame.mixer.Sound('./sounds/boom.wav')
bogulmaSes = pygame.mixer.Sound('./sounds/agua.wav')
Varis_sound = pygame.mixer.Sound('./sounds/success.wav')

# Ses çubuğu boyutları ve konumu
slider_width = 300
slider_height = 50
slider_x = (WIDTH - slider_width) // 2
slider_y = (HEIGHT - slider_height) // 2
# Ses çubuğu renkleri
bar_color = (255, 225, 225)
knob_color = (0, 0, 0)
# Ses çubuğu nesneleri
slider_bar = pygame.Rect(slider_x, slider_y, slider_width, 10)
slider_knob = pygame.Rect(slider_x+290, slider_y - slider_height // 2, 20, slider_height)
# Ses çubuğu için metin ve font
text = font.render("ses seviyesi", True, (240, 255, 255))

class Button:
    def __init__(self, txt, pos):
        self.text = txt
        self.pos = pos
        self.button = pygame.rect.Rect((self.pos[0], self.pos[1]), (260, 40))

    def draw(self):
        pygame.draw.rect(screen, 'light gray', self.button, 0, 5)
        pygame.draw.rect(screen, 'dark gray', [self.pos[0], self.pos[1], 260, 40], 5, 5)
        text2 = font.render(self.text, True, 'black')
        screen.blit(text2, (self.pos[0] + 15, self.pos[1] + 7))

    def check_clicked(self):
        if self.button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            return True
        else:
            return False
class Button1:
    def __init__(self, txt, pos):
        self.text = txt
        self.pos = pos
        self.button = pygame.rect.Rect((self.pos[0], self.pos[1]), (100, 40))

    def draw(self):
        pygame.draw.rect(screen, 'light gray', self.button, 0, 5)
        pygame.draw.rect(screen, 'dark gray', [self.pos[0], self.pos[1], 100, 40], 5, 5)
        text2 = font.render(self.text, True, 'black')
        screen.blit(text2, (self.pos[0] + 15, self.pos[1] + 7))

    def check_clicked(self):
        if self.button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
            return True
        else:
            return False

def draw_menu():
    command = -1
    screen.blit(bg, (0, 0))
    screen.blit(logo, (80, 80))
    menu = Button('Çıkış', (100, 400))
    menu.draw()
    button1 = Button('Oyuna Başla', (100, 250))
    button1.draw()
    button2 = Button('En İyi Skorlar', (100, 300))
    button2.draw()
    button3 = Button('Ayarlar', (100, 350))
    button3.draw()
    if menu.check_clicked():
        command = 0
    if button1.check_clicked():
        command = 1
    if button2.check_clicked():
        command = 2
    if button3.check_clicked():
        command = 3
    return command

def namePage():
    screen.blit(bg1, (0, 0))
    screen.blit(logo, (80, 80))
    command = -1
    button1 = Button1('Başla', (170, 300))
    button1.draw()
    button2 = Button1('Geri',(170,350))
    button2.draw()
    if button1.check_clicked():
        command = 5
    if button2.check_clicked():
        command = 6
    return command
def skorPage():
    mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="qwerty123*",
            database="frogger"
        )
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM skorlar ORDER BY skor DESC")
    myresult = mycursor.fetchall()
    text_name = point_font.render(('1.{0}'.format(myresult[0][1])), 1, (0, 0, 0))
    text_name1 = point_font.render(('2.{0}'.format(myresult[1][1])), 1, (0, 0, 0))
    text_name2 = point_font.render(('3.{0}'.format(myresult[2][1])), 1, (0, 0, 0))
    text_name3 = point_font.render(('4.{0}'.format(myresult[3][1])), 1, (0, 0, 0))
    text_name4 = point_font.render(('5.{0}'.format(myresult[4][1])), 1, (0, 0, 0))
    text_points = point_font.render(('|  {0}'.format(myresult[0][2])), 1, (0, 0, 0))
    text_points1 = point_font.render(('|  {0}'.format(myresult[1][2])), 1, (0, 0, 0))
    text_points2 = point_font.render(('|  {0}'.format(myresult[2][2])), 1, (0, 0, 0))
    text_points3 = point_font.render(('|  {0}'.format(myresult[3][2])), 1, (0, 0, 0))
    text_points4 = point_font.render(('|  {0}'.format(myresult[4][2])), 1, (0, 0, 0))

    screen.blit(bg1, (0, 0))
    screen.blit(logo, (80, 80))
    screen.blit(text_name, (110, 220))
    screen.blit(text_name1, (110, 250))
    screen.blit(text_name2, (110, 280))
    screen.blit(text_name3, (110, 310))
    screen.blit(text_name4, (110, 340))
    screen.blit(text_points, (220, 220))
    screen.blit(text_points1, (220, 250))
    screen.blit(text_points2, (220, 280))
    screen.blit(text_points3, (220, 310))
    screen.blit(text_points4, (220, 340))

    command = -1
    button1 = Button1('Geri', (300, 400))
    button1.draw()
    if button1.check_clicked():
        command = 7
    return command
def settings():
    command = -1
    screen.blit(bg1, (0, 0))
    pygame.draw.rect(screen, bar_color, slider_bar)
    pygame.draw.rect(screen, knob_color, slider_knob)
    screen.blit(text, (slider_x + slider_width // 2 - 85, slider_y + slider_height))
    button1 = Button1('Geri', (300, 450))
    button1.draw()
    if button1.check_clicked():
        command = 4
    return command
def hareket():
    global lotus_speed,lotus2_speed
    moving_rect.y +=lotus_speed
    moving_rect2.y -=lotus2_speed
    if moving_rect.bottom >=HEIGHT+10 or moving_rect.top <=170:
        lotus_speed *=-1
    if moving_rect2.bottom >=556 or moving_rect2.top <=170:
        lotus2_speed *=-1
    screen.blit(lotus, (moving_rect))
    screen.blit(lotus,(moving_rect2))
moving_rect = pygame.Rect(20,170,100,100)
moving_rect2 = pygame.Rect(350,456,100,100)
lotus_speed = 2
lotus2_speed = 2

oyunMuzigi.play(-1)

run = True
while run:

    timer.tick(fps)
    if main_menu:
        menu_command = draw_menu()
        if menu_command != -1:
            main_menu = False
    else:
        main_menu = draw_menu()
        if menu_command == 3:
            run1=True
            while run1:
               settings()
               if main_menu:
                   menu_command = settings()
                   if menu_command != -1:
                       main_menu = False
               else:
                   main_menu = draw_menu()
                   if menu_command == 4:
                      run1 = False
                      draw_menu()
               for event in pygame.event.get():
                   if event.type == pygame.QUIT:
                       pygame.quit()
                       sys.exit()
                   if event.type == pygame.MOUSEBUTTONDOWN:
                       if slider_bar.collidepoint(event.pos):
                           slider_knob.centerx = event.pos[0]
                           if slider_knob.x <= slider_x:
                               oyunMuzigi.set_volume(0)
                               arabaCarpma.set_volume(0)
                               bogulmaSes.set_volume(0)
                               Varis_sound.set_volume(0)
                           if slider_knob.x > slider_x:
                               oyunMuzigi.set_volume(0.1)
                               arabaCarpma.set_volume(0.1)
                               bogulmaSes.set_volume(0.1)
                               Varis_sound.set_volume(0.1)
                           if slider_knob.x > slider_x and slider_knob.x <= slider_x + 60:
                               oyunMuzigi.set_volume(0.2)
                               arabaCarpma.set_volume(0.2)
                               bogulmaSes.set_volume(0.2)
                               Varis_sound.set_volume(0.2)
                           if slider_knob.x > slider_x+60 and slider_knob.x <= slider_x + 90:
                               oyunMuzigi.set_volume(0.3)
                               arabaCarpma.set_volume(0.3)
                               bogulmaSes.set_volume(0.3)
                               Varis_sound.set_volume(0.3)
                           if slider_knob.x > slider_x+90 and slider_knob.x <= slider_x + 120:
                               oyunMuzigi.set_volume(0.4)
                               arabaCarpma.set_volume(0.4)
                               bogulmaSes.set_volume(0.4)
                               Varis_sound.set_volume(0.4)
                           if slider_knob.x > slider_x+120 and slider_knob.x <= slider_x + 150:
                               oyunMuzigi.set_volume(0.5)
                               arabaCarpma.set_volume(0.5)
                               bogulmaSes.set_volume(0.5)
                               Varis_sound.set_volume(0.5)
                           if slider_knob.x > slider_x+150 and slider_knob.x <= slider_x + 180:
                               oyunMuzigi.set_volume(0.6)
                               arabaCarpma.set_volume(0.6)
                               bogulmaSes.set_volume(0.6)
                               Varis_sound.set_volume(0.6)
                           if slider_knob.x > slider_x+180 and slider_knob.x <= slider_x + 210:
                               oyunMuzigi.set_volume(0.7)
                               arabaCarpma.set_volume(0.7)
                               bogulmaSes.set_volume(0.7)
                               Varis_sound.set_volume(0.7)
                           if slider_knob.x > slider_x+210 and slider_knob.x <= slider_x + 240:
                               oyunMuzigi.set_volume(0.8)
                               arabaCarpma.set_volume(0.8)
                               bogulmaSes.set_volume(0.8)
                               Varis_sound.set_volume(0.8)
                           if slider_knob.x > slider_x+240 and slider_knob.x <= slider_x + 270:
                               oyunMuzigi.set_volume(0.9)
                               arabaCarpma.set_volume(0.9)
                               bogulmaSes.set_volume(0.9)
                               Varis_sound.set_volume(0.9)
                           if slider_knob.x > slider_x+270:
                               oyunMuzigi.set_volume(1)
                               arabaCarpma.set_volume(1)
                               bogulmaSes.set_volume(1)
                               Varis_sound.set_volume(1)
               pygame.display.update()
               pygame.display.flip()
               clock.tick(30)
        if menu_command == 0:
            exit()

        if menu_command == 1:
            run2 = True
            while run2:
                if main_menu:
                    menu_command = namePage()
                    if menu_command != -1:
                        main_menu = False
                else:
                    main_menu = draw_menu()
                    if menu_command == 5:
                        run2 = False
                        pygame.init()
                        pygame.font.init()

                        font_name = pygame.font.get_default_font()
                        game_font = pygame.font.SysFont(font_name, 72)
                        info_font = pygame.font.SysFont(font_name, 24)
                        menu_font = pygame.font.SysFont(font_name, 36)
                        font = pygame.font.Font('freesansbold.ttf', 24)
                        screen = pygame.display.set_mode((448, 546), 0, 32)
                        menu_command = 0
                        main_menu = True
                        background_filename = './images/bg.png'
                        frog_filename = './images/sprite_sheets_up.png'
                        arrived_filename = './images/frog_arrived.png'
                        car1_filename = './images/car1.png'
                        car2_filename = './images/car2.png'
                        car3_filename = './images/car3.png'
                        car4_filename = './images/car4.png'
                        car5_filename = './images/car5.png'
                        plataform_filename = './images/tronco.png'
                        water_filename = './images/water.png'
                        arkaplan = pygame.image.load(background_filename).convert()
                        kurbagaHareket = pygame.image.load(frog_filename).convert_alpha()
                        kurbagaVaris = pygame.image.load(arrived_filename).convert_alpha()
                        araba1 = pygame.image.load(car1_filename).convert_alpha()
                        araba2 = pygame.image.load(car2_filename).convert_alpha()
                        araba3 = pygame.image.load(car3_filename).convert_alpha()
                        araba4 = pygame.image.load(car4_filename).convert_alpha()
                        araba5 = pygame.image.load(car5_filename).convert_alpha()
                        odun = pygame.image.load(plataform_filename).convert_alpha()
                        waterEffect = pygame.image.load(water_filename).convert_alpha()
                        pygame.display.set_caption('Frogger')
                        clock = pygame.time.Clock()


                        class Button1:
                            def __init__(self, txt, pos):
                                self.text = txt
                                self.pos = pos
                                self.button = pygame.rect.Rect((self.pos[0], self.pos[1]), (100, 40))

                            def draw(self):
                                pygame.draw.rect(screen, 'light gray', self.button, 0, 5)
                                pygame.draw.rect(screen, 'dark gray', [self.pos[0], self.pos[1], 100, 40], 5, 5)
                                text2 = font.render(self.text, True, 'black')
                                screen.blit(text2, (self.pos[0] + 15, self.pos[1] + 7))

                            def check_clicked(self):
                                if self.button.collidepoint(pygame.mouse.get_pos()) and pygame.mouse.get_pressed()[0]:
                                    return True
                                else:
                                    return False


                        class Object():
                            def __init__(self, position, sprite):
                                self.sprite = sprite
                                self.position = position

                            def draw(self):
                                screen.blit(self.sprite, (self.position))

                            def rect(self):
                                return Rect(self.position[0], self.position[1], self.sprite.get_width(),
                                            self.sprite.get_height())

                        class waterDrop:
                            def __init__(self,position,sprite_sapo):
                                self.sprite = sprite_sapo
                                self.position = position
                                self.animation_counter = 0
                                self.animation_tick = 1
                            def animateWater(self):
                                if self.animation_counter != 0:
                                    if self.animation_tick <= 0:
                                        self.animation_tick = 1
                                    else:
                                        self.animation_tick = self.animation_tick - 1

                            def incAnimationCounter1(self):
                                self.animation_counter = self.animation_counter + 1
                                if self.animation_counter == 3:
                                    self.animation_counter = 0
                                    self.can_move = 1

                        class Frog(Object):
                            def __init__(self, position, sprite_sapo):
                                self.sprite = sprite_sapo
                                self.position = position
                                self.lives = 3
                                self.animation_counter = 0
                                self.animation_tick = 1
                                self.way = "UP"
                                self.can_move = 1

                            def updateSprite(self, key_pressed):
                                if self.way != key_pressed:
                                    self.way = key_pressed
                                    if self.way == "up":
                                        frog_filename = './images/sprite_sheets_up.png'
                                        self.sprite = pygame.image.load(frog_filename).convert_alpha()
                                    elif self.way == "down":
                                        frog_filename = './images/sprite_sheets_down.png'
                                        self.sprite = pygame.image.load(frog_filename).convert_alpha()
                                    elif self.way == "left":
                                        frog_filename = './images/sprite_sheets_left.png'
                                        self.sprite = pygame.image.load(frog_filename).convert_alpha()
                                    elif self.way == "right":
                                        frog_filename = './images/sprite_sheets_right.png'
                                        self.sprite = pygame.image.load(frog_filename).convert_alpha()

                            def moveFrog(self, key_pressed, key_up):
                                if self.animation_counter == 0:
                                    self.updateSprite(key_pressed)
                                self.incAnimationCounter()
                                if key_up == 1:
                                    if key_pressed == "up":
                                        if self.position[1] > 39:
                                            self.position[1] = self.position[1] - 13
                                    elif key_pressed == "down":
                                        if self.position[1] < 473:
                                            self.position[1] = self.position[1] + 13
                                    if key_pressed == "left":
                                        if self.position[0] > 2:
                                            if self.animation_counter == 2:
                                                self.position[0] = self.position[0] - 13
                                            else:
                                                self.position[0] = self.position[0] - 14
                                    elif key_pressed == "right":
                                        if self.position[0] < 401:
                                            if self.animation_counter == 2:
                                                self.position[0] = self.position[0] + 13
                                            else:
                                                self.position[0] = self.position[0] + 14

                            def animateFrog(self, key_pressed, key_up):
                                if self.animation_counter != 0:
                                    if self.animation_tick <= 0:
                                        self.moveFrog(key_pressed, key_up)
                                        self.animation_tick = 1
                                    else:
                                        self.animation_tick = self.animation_tick - 1

                            def setPos(self, position):
                                self.position = position

                            def decLives(self):
                                self.lives = self.lives - 1

                            def cannotMove(self):
                                self.can_move = 0

                            def incAnimationCounter(self):
                                self.animation_counter = self.animation_counter + 1
                                if self.animation_counter == 3:
                                    self.animation_counter = 0
                                    self.can_move = 1

                            def frogDead(self, game):
                                self.setPositionToInitialPosition()
                                self.decLives()
                                game.resetTime()
                                self.animation_counter = 0
                                self.animation_tick = 1
                                self.way = "UP"
                                self.can_move = 1

                            def setPositionToInitialPosition(self):
                                self.position = [207, 475]

                            def draw(self):
                                current_sprite = self.animation_counter * 30
                                screen.blit(self.sprite, (self.position),
                                            (0 + current_sprite, 0, 30, 30 + current_sprite))

                            def rect(self):
                                return Rect(self.position[0], self.position[1], 30, 30)


                        class Enemy(Object):
                            def __init__(self, position, sprite_enemy, way, factor):
                                self.sprite = sprite_enemy
                                self.position = position
                                self.way = way
                                self.factor = factor

                            def move(self, speed):
                                if self.way == "right":
                                    self.position[0] = self.position[0] + speed * self.factor
                                elif self.way == "left":
                                    self.position[0] = self.position[0] - speed * self.factor


                        class Plataform(Object):
                            def __init__(self, position, sprite_plataform, way):
                                self.sprite = sprite_plataform
                                self.position = position
                                self.way = way

                            def move(self, speed):
                                if self.way == "right":
                                    self.position[0] = self.position[0] + speed
                                elif self.way == "left":
                                    self.position[0] = self.position[0] - speed


                        class Game():
                            def __init__(self, speed, level):
                                self.speed = speed
                                self.level = level
                                self.points = 0
                                self.time = 30
                                self.gameInit = 0

                            def incLevel(self):
                                self.level = self.level + 1

                            def incSpeed(self):
                                self.speed = self.speed + 1

                            def incPoints(self, points):
                                self.points = self.points + points

                            def decTime(self):
                                self.time = self.time - 1

                            def resetTime(self):
                                self.time = 30


                        def drawList(list):
                            for i in list:
                                i.draw()


                        def moveList(list, speed):
                            for i in list:
                                i.move(speed)


                        def destroyEnemys(list):
                            for i in list:
                                if i.position[0] < -80:
                                    list.remove(i)
                                elif i.position[0] > 516:
                                    list.remove(i)


                        def destroyPlataforms(list):
                            for i in list:
                                if i.position[0] < -100:
                                    list.remove(i)
                                elif i.position[0] > 448:
                                    list.remove(i)



                        def createEnemys(list, enemys, game):
                            for i, tick in enumerate(list):
                                list[i] = list[i] - 1
                                if tick <= 0:
                                    if i == 0:
                                        list[0] = (40 * game.speed) / game.level
                                        position_init = [-55, 436]
                                        enemy = Enemy(position_init, araba1, "right", 1)
                                        enemys.append(enemy)
                                    elif i == 1:
                                        list[1] = (30 * game.speed) / game.level
                                        position_init = [506, 397]
                                        enemy = Enemy(position_init, araba2, "left", 2)
                                        enemys.append(enemy)
                                    elif i == 2:
                                        list[2] = (40 * game.speed) / game.level
                                        position_init = [-80, 357]
                                        enemy = Enemy(position_init, araba3, "right", 2)
                                        enemys.append(enemy)
                                    elif i == 3:
                                        list[3] = (30 * game.speed) / game.level
                                        position_init = [516, 318]
                                        enemy = Enemy(position_init, araba4, "left", 1)
                                        enemys.append(enemy)
                                    elif i == 4:
                                        list[4] = (50 * game.speed) / game.level
                                        position_init = [-56, 280]
                                        enemy = Enemy(position_init, araba5, "right", 1)
                                        enemys.append(enemy)


                        def createPlataform(list, plataforms, game):
                            for i, tick in enumerate(list):
                                list[i] = list[i] - 1
                                if tick <= 0:
                                    if i == 0:
                                        list[0] = (30 * game.speed) / game.level
                                        position_init = [-100, 200]
                                        plataform = Plataform(position_init, odun, "right")
                                        plataforms.append(plataform)
                                    elif i == 1:
                                        list[1] = (30 * game.speed) / game.level
                                        position_init = [448, 161]
                                        plataform = Plataform(position_init, odun, "left")
                                        plataforms.append(plataform)
                                    elif i == 2:
                                        list[2] = (40 * game.speed) / game.level
                                        position_init = [-100, 122]
                                        plataform = Plataform(position_init, odun, "right")
                                        plataforms.append(plataform)
                                    elif i == 3:
                                        list[3] = (40 * game.speed) / game.level
                                        position_init = [448, 83]
                                        plataform = Plataform(position_init, odun, "left")
                                        plataforms.append(plataform)
                                    elif i == 4:
                                        list[4] = (20 * game.speed) / game.level
                                        position_init = [-100, 44]
                                        plataform = Plataform(position_init, odun, "right")
                                        plataforms.append(plataform)


                        def frogOnTheStreet(frog, enemys, game):
                            for i in enemys:
                                enemyRect = i.rect()
                                frogRect = frog.rect()
                                if frogRect.colliderect(enemyRect):
                                    arabaCarpma.play()
                                    frog.frogDead(game)

                        def destroyPlataforms2(plataforms):
                            for i in plataforms:
                                plataformRect = i.rect()
                                frogRect = frog.rect()
                                if frogRect.colliderect(plataformRect):
                                    while not time.time() >= startTime + 2:
                                        plataforms.remove(i)


                        def frogInTheLake(frog, plataforms, game):
                            seguro = 0
                            water = waterDrop(frog_initial_position,waterEffect)
                            wayPlataform = ""
                            for i in plataforms:
                                plataformRect = i.rect()
                                frogRect = frog.rect()
                                if frogRect.colliderect(plataformRect):
                                    seguro = 1
                                    wayPlataform = i.way

                            if seguro == 0:
                                bogulmaSes.play()
                                water.incAnimationCounter1()
                                water.animateWater()
                                frog.frogDead(game)

                            elif seguro == 1:
                                if wayPlataform == "right":
                                    frog.position[0] = frog.position[0] + game.speed

                                elif wayPlataform == "left":
                                    frog.position[0] = frog.position[0] - game.speed


                        def frogArrived(frog, chegaram, game):
                            if frog.position[0] > 33 and frog.position[0] < 53:
                                position_init = [43, 7]
                                createArrived(frog, chegaram, game, position_init)

                            elif frog.position[0] > 115 and frog.position[0] < 135:
                                position_init = [125, 7]
                                createArrived(frog, chegaram, game, position_init)

                            elif frog.position[0] > 197 and frog.position[0] < 217:
                                position_init = [207, 7]
                                createArrived(frog, chegaram, game, position_init)

                            elif frog.position[0] > 279 and frog.position[0] < 299:
                                position_init = [289, 7]
                                createArrived(frog, chegaram, game, position_init)

                            elif frog.position[0] > 361 and frog.position[0] < 381:
                                position_init = [371, 7]
                                createArrived(frog, chegaram, game, position_init)

                            else:
                                frog.position[1] = 46
                                frog.animation_counter = 0
                                frog.animation_tick = 1
                                frog.can_move = 1


                        def whereIsTheFrog(frog):
                            if frog.position[1] > 240:
                                frogOnTheStreet(frog, enemys, game)

                            elif frog.position[1] < 240 and frog.position[1] > 40:
                                frogInTheLake(frog, plataforms, game)

                            elif frog.position[1] < 40:
                                frogArrived(frog, chegaram, game)


                        def createArrived(frog, chegaram, game, position_init):
                            sapo_chegou = Object(position_init, kurbagaVaris)
                            chegaram.append(sapo_chegou)
                            Varis_sound.play()
                            frog.setPositionToInitialPosition()
                            game.incPoints(10 + game.time)
                            game.resetTime()
                            frog.animation_counter = 0
                            frog.animation_tick = 1
                            frog.can_move = 1


                        def nextLevel(chegaram, enemys, plataforms, frog, game):
                            if len(chegaram) == 1:
                                chegaram[:] = []
                                frog.setPositionToInitialPosition()
                                destroyPlataforms2(plataforms)
                                game.incLevel()
                                game.incSpeed()
                                game.incPoints(100)
                                game.resetTime()


                        def endGame1():
                            command = -1
                            button = Button1("Geri", (300, 300))
                            button.draw()
                            if button.check_clicked():
                                command = 8
                            return command


                        def endGame():
                            screen.blit(arkaplan, (0, 0))
                            text = game_font.render('Oyun bitti', 1, (255, 0, 0))
                            text_points = game_font.render(('Puan: {0}'.format(game.points)), 1, (255, 0, 0))
                            text_reiniciar = info_font.render('Yeniden başlatmak için herhangi bir tuşa basın!', 1,
                                                              (255, 0, 0))
                            screen.blit(text, (75, 120))
                            screen.blit(text_points, (10, 170))
                            screen.blit(text_reiniciar, (70, 250))


                        text_info = menu_font.render(('Press any button to start!'), 1, (0, 0, 0))
                        gameInit = False

                        while gameInit == False:
                            for event in pygame.event.get():
                                if event.type == QUIT:
                                    exit()
                                if event.type == KEYDOWN:
                                    gameInit = True

                            screen.blit(arkaplan, (0, 0))
                            screen.blit(text_info, (80, 150))
                            pygame.display.update()

                        run5 = True
                        while run5:
                            gameInit = True
                            game = Game(3, 1)
                            key_up = 1
                            frog_initial_position = [207, 475]
                            frog = Frog(frog_initial_position, kurbagaHareket)

                            enemys = []
                            plataforms = []
                            chegaram = []
                            ticks_enemys = [30, 0, 30, 0, 60]
                            ticks_plataforms = [0, 0, 30, 30, 30]
                            ticks_time = 30
                            pressed_keys = 0
                            key_pressed = 0

                            while frog.lives > 0:

                                for event in pygame.event.get():
                                    if event.type == QUIT:
                                        exit()
                                    if event.type == KEYUP:
                                        key_up = 1
                                    if event.type == KEYDOWN:
                                        if key_up == 1 and frog.can_move == 1:
                                            key_pressed = pygame.key.name(event.key)
                                            frog.moveFrog(key_pressed, key_up)
                                            frog.cannotMove()
                                if not ticks_time:
                                    ticks_time = 30
                                    game.decTime()
                                else:
                                    ticks_time -= 1

                                if game.time == 0:
                                    frog.frogDead(game)


                                createEnemys(ticks_enemys, enemys, game)
                                createPlataform(ticks_plataforms, plataforms, game)

                                moveList(enemys, game.speed)
                                moveList(plataforms, game.speed)

                                whereIsTheFrog(frog)

                                nextLevel(chegaram, enemys, plataforms, frog, game)

                                text_info1 = info_font.render(
                                    ('Level: {0}               Puan: {1}'.format(game.level, game.points)), 1,
                                    (255, 255, 255))
                                text_info2 = info_font.render(
                                    ('Süre: {0}       Kalan Can: {1}'.format(game.time, frog.lives)), 1,
                                    (255, 255, 255))
                                screen.blit(arkaplan, (0, 0))
                                screen.blit(text_info1, (10, 520))
                                screen.blit(text_info2, (250, 520))

                                drawList(enemys)
                                drawList(plataforms)
                                drawList(chegaram)

                                frog.animateFrog(key_pressed, key_up)
                                frog.draw()

                                destroyEnemys(enemys)
                                destroyPlataforms(plataforms)
                                destroyPlataforms2(plataforms)
                                pygame.display.update()
                                time_passed = clock.tick(30)

                            mydb = mysql.connector.connect(
                                host="localhost",
                                user="root",
                                password="qwerty123*",
                                database="frogger"
                            )
                            mycursor = mydb.cursor()
                            sql = "INSERT INTO skorlar (id,name,skor) VALUES (%s,%s,%s)"
                            val = (None, user_text, game.points)
                            mycursor.execute(sql, val)
                            mydb.commit()
                            print(mycursor.rowcount, "eklendi")
                            while gameInit:

                                endGame()
                                command = -1
                                button = Button1("Geri", (300, 300))
                                button.draw()
                                if button.check_clicked():
                                    command = 8

                                if command == 8:
                                    import menu
                                    run5 = False
                                    gameInit = False

                                for event in pygame.event.get():
                                    if event.type == QUIT:
                                        exit()
                                    if event.type == KEYDOWN:
                                        gameInit = False

                                pygame.display.update()
                    if menu_command == 6:
                        run2 = False
                        draw_menu()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if input_rect.collidepoint(event.pos):
                            active = True
                        else:
                            active = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_BACKSPACE:
                            user_text = user_text[:-1]
                        else:
                            user_text += event.unicode
                if active:
                    color = color_active
                else:
                    color = color_passive
                hareket()
                pygame.draw.rect(screen, color, input_rect)
                pygame.draw.rect(screen, 'blue', input_rect, 3, 2)
                text_surface = base_font.render(user_text, True, (0, 0, 0))
                screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
                input_rect.w = max(100, text_surface.get_width() + 10)
                pygame.display.flip()
                pygame.display.update()
                clock.tick(30)
        if menu_command == 2:
            run3 = True
            while run3:
                skorPage()
                if main_menu:
                    menu_command = skorPage()
                    if menu_command != -1:
                        main_menu = False
                else:
                    main_menu = draw_menu()
                    if menu_command == 7:
                        run3 = False
                        draw_menu()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run3 = False
                pygame.display.flip()
                pygame.display.update()
                clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()

pygame.quit()
