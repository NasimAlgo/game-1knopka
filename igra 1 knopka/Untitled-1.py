from pygame import *
import random

WIDTH,HEIGHT = 800, 600
screen = display.set_mode((WIDTH,HEIGHT))
display.set_caption('One Button game')
FPS = 60
clock = time.Clock()

font_main = font.SysFont("Arial",36)
font_small = font.SysFont('Arial',24)

finish = False
running = True

def reset_game():
    player = Rect(100,450,50,50)
    velocity_y = 0
    on_ground = True
    obstacles = []
    spawn_timer = 0
    score = 0
    finish = False
    return player, velocity_y, on_ground, obstacles, spawn_timer, score, finish

gravity = 1
jump_power =-15

player, velocity_y, on_ground, obstacles, spawn_timer, score, finish = reset_game()

running = True
while running:
    for e in event.get():
        if e.type == QUIT:
            running = False

        if e.type == KEYDOWN:
            if e.key == K_SPACE and on_ground and not finish:
                velocity_y= jump_power
                on_ground= False
            if e.key == K_r and finish:
                player, velocity_y, on_ground, obstacles, spawn_timer, score, finish = reset_game()

    if not finish:
        velocity_y +=gravity
        player.y += velocity_y

        if player.y >= 450:
            player.y = 450
            velocity_y = 0
            sson_ground = True

        spawn_timer += 1
        if spawn_timer > 60:
            h = random.randint(40,70)
            obstacles.append(Rect(800, 500 - h,40,h))
            spawn_timer = 0


#скорость
        for obs in obstacles:
            obs.x -= 7 + score//50

            if player.colliderect(obs):
                finish = True
        obstacles = [o for o in obstacles if o.x > -50]

        score +=1 

    screen.fill((30,30,30))

    draw.rect(screen,(0,180,0),(0,500,WIDTH,100))
    draw.rect(screen,(50,150,255),player)

    for obs in obstacles:
        draw.rect(screen,(255,80,80),obs)

    text = font_main.render(f"score: {score//10}", True, (255,255,255))
    screen.blit(text,(20,20))

    if finish:
        over=font_main.render("GAME OVER", True, (255,0,0))   
        restart = font_small.render("Нажмите R для рестарта", True, (255,255,255))
        screen.blit(text, (270,240))
        screen.blit(text, (290,290))

display update
clock.tick(FPS)