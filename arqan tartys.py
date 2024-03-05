import pygame
import sys

pygame.init()

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600 

WHITE = (255, 255, 255)
BLACK = (0, 0, 0) 

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
pygame.display.set_caption("Arqan tartys!")
menu_background = pygame.image.load("mn.png")
menu_background = pygame.transform.scale(menu_background, (SCREEN_WIDTH, SCREEN_HEIGHT))
game_background = pygame.image.load("dala.png")
play_button = pygame.image.load("go.png")
p = pygame.image.load("1p.png")
p = pygame.transform.scale(p, (300, 300))
pp = pygame.image.load("2p.png")
pp = pygame.transform.scale(pp, (300, 300))
arqan = pygame.image.load("arqan.png")
arqan = pygame.transform.scale(arqan, (800, 464))
victory = pygame.mixer.Sound("win.mp3")
loss = pygame.mixer.Sound("loss.mp3")
music = pygame.mixer.Sound("mus.mp3") 

def main_menu():
    on_menu = True
    while on_menu: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit() 
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if SCREEN_WIDTH // 2 - play_button.get_width() // 2 <= x <= SCREEN_WIDTH // 2 + play_button.get_width() // 2 and \
                   SCREEN_HEIGHT // 2 - play_button.get_height() // 2 <= y <= SCREEN_HEIGHT // 2 + play_button.get_height() // 2:
                    on_menu = False 

        screen.blit(menu_background, (0, 0))
        screen.blit(play_button, (SCREEN_WIDTH // 2 - play_button.get_width() // 2, SCREEN_HEIGHT // 2 - play_button.get_height() // 2))
        pygame.display.update() 
    
    choose()

def choose():
    s = False
    on_choose = True
    while on_choose: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 100 <= x <= 400 and 100 <= y <= 500:
                    on_choose = False
                elif 600 <= x <= 900 and 100 <= y <= 500:
                    s = True 
                    on_choose = False

        screen.fill(WHITE)
        screen.blit(p, (100, 100))
        screen.blit(pp, (600, 100))
        font = pygame.font.Font(None, 36)
        text1 = font.render(f"Бір адамдық ойын", True, BLACK)
        text2 = font.render(f"Екі адамдық ойын", True, BLACK)
        text3 = font.render(f"Ойнау үшін Z бас.", True, BLACK)
        text4 = font.render(f"Ойнау үшін Z және L бас.", True, BLACK)
        screen.blit(text1, (100, 520))
        screen.blit(text2, (600, 520))
        screen.blit(text3, (100, 550))
        screen.blit(text4, (600, 550))
        pygame.display.update() 
    count_down(s)

def count_down(n):
    for i in range(3, 0, -1):
        screen.fill(WHITE)
        font = pygame.font.Font(None, 100)
        text = font.render(str(i), True, BLACK)
        screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - text.get_height() // 2))
        pygame.display.update()
        pygame.time.delay(1000) 
    game_loop(n)

def game_loop(n):
    player = pygame.Rect(100, 150, 800, 464) 
    message = "1 ойыншы жеңді!"
    strength = 0
    enemy = 0 
    s = 0
    e = 0 
    pressed = False
    pressed2 = False 
    game = True
    running = True
    music.play() 
    while running: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()

        if game:
            if keys[pygame.K_z] and not pressed:
                strength += 1
                pressed = True
            
            if not keys[pygame.K_z]:
                pressed = False
            
            if n and keys[pygame.K_l] and not pressed2:
                enemy += 1
                pressed2 = True
            
            if not keys[pygame.K_l]:
                pressed2 = False
            
            if strength > 0:
                strength -= 0.3
                if strength < 0:
                    strength = 0

            if enemy > 0:
                enemy -= 0.3
                if enemy < 0:
                    enemy = 0
            
            if not n: 
                if enemy < 9.5:
                    enemy += 0.4
                            
            player.x -= (abs(strength) - abs(enemy)) 

            if player.x < -400:
                game = False
                music.stop()
                victory.play() 
            
            if player.x > 600:
                game = False
                music.stop()
                if n:
                    message = "2 ойыншы жеңді!"
                    victory.play() 
                else:
                    message = "Компьютер жеңді!"
                    loss.play() 
        else:
            if keys[pygame.K_SPACE]:
                running = False 

        screen.fill(WHITE)
        screen.blit(game_background, (0, 0))
        screen.blit(arqan, player)

        font = pygame.font.Font(None, 36)
        if game:
            text = font.render(f"Ойын басталды!", True, BLACK)
        else:
            text = font.render(f"Ойын аяқталды! {message} Мәзірге қайту үшін Space басыңыз!", True, BLACK)
        screen.blit(text, (20, 20))

        s = abs(strength)*20
        if s > 200:
            s = 200
        e = abs(enemy)*20
        if e > 200:
            e = 200
        
        pygame.draw.rect(screen, (0, 0, 0), [(5, 545), (210, 40)])
        pygame.draw.rect(screen, (0, 0, 0), [(785, 545), (210, 40)])
        if strength > 0:
            pygame.draw.rect(screen, (0, 255, 0), [(10, 550), (s, 30)])
        if enemy > 0:
            pygame.draw.rect(screen, (0, 255, 0), [(990-e, 550), (e, 30)])
        
        pygame.display.update()
        pygame.time.Clock().tick(30)
    
while True:
    main_menu()
