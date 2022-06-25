import pygame
from pygame import mixer
import random
import button

pygame.font.init()
mixer.init()

pygame.mixer.music.load("assets/sounds/star_wars_main.mp3")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1, 0.0, 5000)

WIDTH = 720
HEIGHT = 480
DIFFICULTY = 50

SPACESHIP = pygame.image.load("assets/images/spaceship.png")
SPACESHIP_HIT = pygame.USEREVENT + 1
SPACESHIP_WIDTH = SPACESHIP.get_width()
SPACESHIP_HEIGHT = SPACESHIP.get_height()
SPACESHIP_SCALE = 1

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

POINT = pygame.USEREVENT + 2
POINT_COLOR = BLUE
POINT_FONT = "montserrat"
POINT_HEIGHT = 40
POINT_TEXT = pygame.font.SysFont( POINT_FONT, 40)

SPACESHIP = pygame.transform.scale(SPACESHIP,
            (SPACESHIP_WIDTH * SPACESHIP_SCALE, SPACESHIP_HEIGHT * SPACESHIP_SCALE))
SPACESHIP_WIDTH = SPACESHIP.get_width()
SPACESHIP_HEIGHT = SPACESHIP.get_height()

ENEMY = pygame.image.load("assets/images/enemy.png")
ENEMY_WIDTH = ENEMY.get_width()
ENEMY_HEIGHT = ENEMY.get_height()
ENEMY_SCALE = 1

ENEMY = pygame.transform.scale(ENEMY,
        (ENEMY_WIDTH * ENEMY_SCALE, ENEMY_HEIGHT * ENEMY_SCALE))
ENEMY_WIDTH = ENEMY.get_width()
ENEMY_HEIGHT = ENEMY.get_height()
MAX_ENEMY = 10

BULLET_WIDTH = 17
BULLET_HEIGHT = 4
MAX_BULLET = 10
BULLET_VEL = 20
BULLET_COLOR = RED

bullet_sound = pygame.mixer.Sound("assets/sounds/laser.wav")
bullet_sound.set_volume(0.3)

hit_sound = pygame.mixer.Sound("assets/sounds/hit_spaceship.wav")
hit_sound.set_volume(0.5)

ENEMY_BULLET_WIDTH = 10
ENEMY_BULLET_HEIGHT = 2
MAX_ENEMY_BULLETS = 10
ENEMY_BULLET_VEL = 5
ENEMY_BULLET_COLOR = GREEN

enemy_explosion_sound = pygame.mixer.Sound("assets/sounds/exploading_enemy.wav")
enemy_explosion_sound.set_volume(0.3)

enemy_bullet_sound = pygame.mixer.Sound("assets/sounds/enemy_laser.wav")
enemy_bullet_sound.set_volume(0.3)

X_VEL = 5
Y_VEL = 5
ENEMY_VEL = 2

HEALTH_COLOR = WHITE
HEALTH_FONT = "montserrat"
HEALTH_HEIGHT = 40
HEALTH_TEXT = pygame.font.SysFont(HEALTH_FONT, HEALTH_HEIGHT)

LOSE_COLOR = RED
LOSE_FONT = "montserrat"
LOSE_HEIGHT = 100
LOSE_TEXT = pygame.font.SysFont(LOSE_FONT, LOSE_HEIGHT)

game_over_sound = pygame.mixer.Sound("assets/sounds/game_over.wav")
game_over_sound.set_volume(0.5)

LOSE_DELAY = 5000
LOSE_STRING = "LOSER"

FPS = 50

SPACE = pygame.image.load("assets/images/space.png")
SPACE = pygame.transform.scale(SPACE, (WIDTH, HEIGHT))

PAUSE_BUTTON = pygame.image.load("assets/images/pause.png")
PAUSE_WIDTH = PAUSE_BUTTON.get_width()
PAUSE_HEIGHT = PAUSE_BUTTON.get_height()
PAUSE_SCALE = 1
pygame.transform.scale(PAUSE_BUTTON,
        (PAUSE_WIDTH * PAUSE_SCALE, PAUSE_HEIGHT * PAUSE_SCALE))
PAUSE_WIDTH = PAUSE_BUTTON.get_width()
PAUSE_HEIGHT = PAUSE_BUTTON.get_height()

PLAY_BUTTON = pygame.image.load("assets/images/play.png")
PLAY_WIDTH = PLAY_BUTTON.get_width()
PLAY_HEIGHT = PLAY_BUTTON.get_height()
PLAY_SCALE = 1
pygame.transform.scale(PLAY_BUTTON,
        (PLAY_WIDTH * PLAY_SCALE, PLAY_HEIGHT * PLAY_SCALE))
PLAY_WIDTH = PLAY_BUTTON.get_width()
PLAY_HEIGHT = PLAY_BUTTON.get_height()

STOP_BUTTON = pygame.image.load("assets/images/stop.png")
STOP_WIDTH = STOP_BUTTON.get_width()
STOP_HEIGHT = STOP_BUTTON.get_height()
STOP_SCALE = 1
pygame.transform.scale(STOP_BUTTON,
        (STOP_WIDTH * STOP_SCALE, STOP_HEIGHT * STOP_SCALE))
STOP_WIDTH = STOP_BUTTON.get_width()
STOP_HEIGHT = STOP_BUTTON.get_height()

BORDER_X = 520
BORDER_WIDTH = 10
BORDER_HEIGHT = HEIGHT
BORDER = pygame.Rect(BORDER_X, 0, BORDER_WIDTH, BORDER_HEIGHT)

LINE_Y = 40
LINE_WIDTH = WIDTH
LINE_HEIGHT = 10
LINE = pygame.Rect(0, LINE_Y, LINE_WIDTH, LINE_HEIGHT)

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game")

PLAY = button.Button(WIN, WIDTH-160, 10, PLAY_WIDTH+6, PLAY_HEIGHT+6, GREEN, PLAY_BUTTON, False)
PAUSE = button.Button(WIN, WIDTH-110, 10, PAUSE_WIDTH+6, PAUSE_HEIGHT+6, RED, PAUSE_BUTTON, False)
STOP = button.Button(WIN, WIDTH-60, 10, STOP_WIDTH+6, STOP_HEIGHT+6, BLUE, STOP_BUTTON, False)

def movement(spaceship, key_pressed, x_vel, y_vel):

    if key_pressed[pygame.K_w] and spaceship.y - y_vel > LINE_Y + LINE_HEIGHT: #UP
        spaceship.y -= y_vel
    if key_pressed[pygame.K_s] and spaceship.y + y_vel + SPACESHIP_HEIGHT + 0 < HEIGHT: #DOWN
        spaceship.y += y_vel
    if key_pressed[pygame.K_a] and spaceship.x - x_vel > 0: #LEFT
        spaceship.x -= x_vel
    if key_pressed[pygame.K_d] and spaceship.x + x_vel + SPACESHIP_WIDTH < BORDER.x: #RIGHT
        spaceship.x += x_vel

def draw(spaceship, bullets, enemies, enemies_bullets, health, points):

    WIN.blit(SPACE, (0, 0))                                             #DRAW SPACE BACKGROUND

    pygame.draw.rect(WIN, BLACK, BORDER)                                #DRAW BORDER
    pygame.draw.rect(WIN, BLACK, LINE) 

    WIN.blit(SPACESHIP, (spaceship.x, spaceship.y))                     #DRAW SPACESHIP

    health_text = HEALTH_TEXT.render(
        "Health: " + str(health), 1, HEALTH_COLOR)                      #DEFINE HEALTH TEXT
    WIN.blit(health_text, (10, 10))                                     #DRAW HEALTH TEXT

    points_text = POINT_TEXT.render( 
        "Points: " + str(points), 1, POINT_COLOR)                       #DEFINE POINTS TEXT
    WIN.blit(points_text, (250, 10))

    PAUSE.draw()
    PLAY.draw()
    STOP.draw()

    for enemy in enemies:
        WIN.blit(ENEMY, (enemy.x, enemy.y))                             #DRAW ENEMIES
        
    for bullet in bullets:
        pygame.draw.rect(WIN, BULLET_COLOR, bullet)                     #DRAW BULLETS

    for enemy_bullet in enemies_bullets:
        pygame.draw.rect(WIN, ENEMY_BULLET_COLOR, enemy_bullet)         #DRAW ENEMIES' BULLETS

def move_bullets(bullets):

    for bullet in bullets:
        bullet.x += BULLET_VEL                                          #MOVE BULLETS
        if bullet.x >= WIDTH:
            bullets.remove(bullet)                                      #REMOVE OFFSCREEN BULLETS

def move_enemy_bullets(enemies_bullets):

    for enemy_bullet in enemies_bullets:
        enemy_bullet.x -= ENEMY_BULLET_VEL                              #MOVE ENEMIES' BULLETS
        if enemy_bullet.x <= 0:
            enemies_bullets.remove(enemy_bullet)                        #REMOVE OFFSCREEN ENEMIES' BULLETS

def move_enemies(enemies):

    for enemy in enemies:
        if enemy.x > BORDER.x + BORDER_WIDTH:
            enemy.x -= ENEMY_VEL                                        #MOVE ENEMIES TILL THEY ARE AT THE BORDER

def hit_enemy(enemies, bullets):

    for enemy in enemies:
        for bullet in bullets:
            if enemy.colliderect(bullet):
                enemy_explosion_sound.play()
                pygame.event.post(pygame.event.Event(POINT))
                bullets.remove(bullet)                                  #REMOVE BULLETS THAT HIT ENEMIES
                enemies.remove(enemy)                                   #REMOVE ENEMIES THAT GOT HIT BY BULLETS

def spawn_enemies(enemies, difficulty):
    
    spawn = random.randint(1, difficulty)                               #1/DIFFICULTY % OF SPAWNING AN ENEMY

    if spawn == 1 and len(enemies) < MAX_ENEMY:
        enemy = pygame.Rect( random.randint(WIDTH-50, WIDTH+50),
        random.randint(LINE_Y + LINE_HEIGHT, HEIGHT - ENEMY_HEIGHT), ENEMY_WIDTH, ENEMY_HEIGHT)
        enemies.append(enemy)

def enemies_bullets(enemies, difficulty, enemies_bullets):

    for enemy in enemies:
        if random.randint(1, difficulty) == 1 and len(enemies_bullets) < MAX_ENEMY_BULLETS:
            enemy_bullet_sound.play()
            enemy_bullet = pygame.Rect(enemy.x, enemy.y + ENEMY_HEIGHT/2 - 2,
                        ENEMY_BULLET_WIDTH, ENEMY_BULLET_HEIGHT)
            enemies_bullets.append(enemy_bullet)

def hit_spaceship(spaceship, enemies_bullets):
    
    for enemy_bullet in enemies_bullets:
        if spaceship.colliderect(enemy_bullet):
            hit_sound.play()
            pygame.event.post(pygame.event.Event(SPACESHIP_HIT))
            enemies_bullets.remove(enemy_bullet)

def lose(text):
    lose_text = LOSE_TEXT.render(text, 1, LOSE_COLOR)
    WIN.blit(lose_text, (WIDTH/2 - lose_text.get_width() /
                         2, HEIGHT/2 - lose_text.get_height()/2))
    game_over_sound.play()
    pygame.display.update()
    pygame.time.delay(LOSE_DELAY)

def main():

    spaceship = pygame.Rect(300, 200, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    SPACESHIP_HEALTH = 10
    points = 0
    
    run = True
    clock = pygame.time.Clock()
    bullets = []
    enemies = []
    enemy_bullets_list = []

    while run:

        clock.tick(FPS)

        for event in pygame.event.get():

            if event.type == pygame.QUIT or STOP.is_pressed_left(event):
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1 and len(bullets) < MAX_BULLET:
                    bullet = pygame.Rect(spaceship.x + SPACESHIP_WIDTH, spaceship.y + SPACESHIP_HEIGHT/2 - 2,
                        BULLET_WIDTH, BULLET_HEIGHT)
                    bullets.append(bullet)
                    bullet_sound.play()

            if event.type == SPACESHIP_HIT:
                SPACESHIP_HEALTH -= 1

            if event.type == POINT:
                points += 1

            if PAUSE.is_pressed_left(event):
                pygame.mixer.music.pause()
                variable = True
                while variable:
                    for event in pygame.event.get():

                        if event.type == pygame.QUIT:
                            variable = False
                            run = False

                        if PLAY.is_pressed_left(event):
                                variable = False
                                pygame.mixer.music.unpause()

        keys_pressed = pygame.key.get_pressed()

        movement(spaceship, keys_pressed, X_VEL, Y_VEL)
        draw(spaceship, bullets, enemies, enemy_bullets_list, SPACESHIP_HEALTH, points)
        move_bullets(bullets)
        hit_enemy(enemies, bullets)
        move_enemies(enemies)
        spawn_enemies(enemies, DIFFICULTY)
        enemies_bullets(enemies, DIFFICULTY, enemy_bullets_list)
        move_enemy_bullets(enemy_bullets_list)
        hit_spaceship(spaceship, enemy_bullets_list)

        if SPACESHIP_HEALTH <= 0:
            pygame.mixer.music.stop()
            lose(LOSE_STRING)
            break
        
        pygame.display.update()

    if run:
        pygame.mixer.music.play(-1, 0.0, 5000)
        main()

if __name__ == "__main__":
    main()

#record = 64