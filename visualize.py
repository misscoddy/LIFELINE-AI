import pygame
import sys
import math
import time
import random

pygame.init()

# -------------------------
# Screen Setup
# -------------------------
WIDTH, HEIGHT = 900, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lifeline AI - Rescue Ops")
clock = pygame.time.Clock()

# -------------------------
# Colors & Fonts
# -------------------------
SKY = (235, 240, 255)
MOUNTAIN_BACK = (190, 200, 220)
MOUNTAIN_FRONT = (160, 175, 200)
GROUND = (110, 110, 130)

DRONE = (60, 60, 80)
HUMAN = (90, 90, 110)
HAZARD = (200, 120, 120)

UI_BG = (25, 25, 45)
UI_CARD = (70, 70, 110)
WHITE = (250, 250, 255)

font = pygame.font.SysFont("consolas", 20)
big_font = pygame.font.SysFont("consolas", 48)

# -------------------------
# Game States
# -------------------------
START, PLAY, PAUSE, END = 0, 1, 2, 3
state = START

start_time = 0
score = 0
difficulty = 1

# -------------------------
# Drone
# -------------------------
class Drone:
    def __init__(self):
        self.x = 150
        self.y = 200
        self.speed = 3
        self.angle = 0

    def move(self, keys):
        if keys[pygame.K_LEFT]: self.x -= self.speed
        if keys[pygame.K_RIGHT]: self.x += self.speed
        if keys[pygame.K_UP]: self.y -= self.speed
        if keys[pygame.K_DOWN]: self.y += self.speed

    def update(self):
        self.angle += 0.25

# -------------------------
# Human
# -------------------------
class Human:
    def __init__(self, x, y):
        self.x = x
        self.base_y = y
        self.y = y
        self.rescued = False
        self.t = 0

    def update(self):
        self.t += 0.1
        self.y = self.base_y + math.sin(self.t) * 2

# -------------------------
# Hazard
# -------------------------
class Hazard:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.flash = 0

    def update(self):
        self.flash += 0.1

# -------------------------
# Init Game
# -------------------------
drone = Drone()

def init_game(level):
    global humans, hazards, difficulty, score
    difficulty = level
    score = 0
    drone.x, drone.y = 150, 200

    if level == 1:
        humans = [Human(400,380), Human(600,380)]
        hazards = [Hazard(300,385)]
    elif level == 2:
        humans = [Human(350,380), Human(550,380), Human(750,380)]
        hazards = [Hazard(300,385), Hazard(650,385)]
    else:
        humans = [Human(250,380), Human(450,380), Human(650,380), Human(800,380)]
        hazards = [Hazard(200,385), Hazard(500,385), Hazard(700,385)]

init_game(1)
auto_mode = False

# -------------------------
# Background Animations
# -------------------------
clouds = [[100,80], [400,60], [700,90]]
back_offset = 0
front_offset = 0
ground_offset = 0

def update_bg():
    global back_offset, front_offset, ground_offset
    for c in clouds:
        c[0] -= 0.3
        if c[0] < -100: c[0] = WIDTH + 50

    back_offset -= 0.3
    front_offset -= 0.8
    ground_offset -= 3

    if back_offset < -300: back_offset = 0
    if front_offset < -300: front_offset = 0
    if ground_offset < -40: ground_offset = 0

def draw_bg():
    screen.fill(SKY)

    # mountains
    for i in range(4):
        x = i*300 + back_offset
        pygame.draw.polygon(screen, MOUNTAIN_BACK, [(x,350),(x+150,220),(x+300,350)])
    for i in range(4):
        x = i*300 + front_offset
        pygame.draw.polygon(screen, MOUNTAIN_FRONT, [(x,380),(x+150,260),(x+300,380)])

    # clouds
    for x,y in clouds:
        pygame.draw.circle(screen,(220,220,230),(int(x),int(y)),20)
        pygame.draw.circle(screen,(220,220,230),(int(x+20),int(y+5)),18)
        pygame.draw.circle(screen,(220,220,230),(int(x-20),int(y+5)),18)

    # ground
    for i in range(30):
        x = i*40 + ground_offset
        pygame.draw.rect(screen, GROUND, (x,400,40,100))

# -------------------------
# Draw Objects
# -------------------------
def draw_drone():
    x,y = drone.x, drone.y
    pygame.draw.rect(screen, DRONE, (x,y,30,12), border_radius=4)
    cx, cy = x+15, y-5
    l = 15
    pygame.draw.line(screen, DRONE,
        (cx + l*math.cos(drone.angle), cy + l*math.sin(drone.angle)),
        (cx - l*math.cos(drone.angle), cy - l*math.sin(drone.angle)),2)

def draw_human(h):
    pygame.draw.circle(screen,HUMAN,(int(h.x+4),int(h.y-3)),3)
    pygame.draw.rect(screen,HUMAN,(h.x,h.y,8,12),border_radius=2)

def draw_hazard(h):
    alpha = int((math.sin(h.flash)*0.5+0.5)*255)
    color = (200,100+alpha//4,100)
    pygame.draw.rect(screen,color,(h.x,h.y,80,15),border_radius=5)

# -------------------------
# UI
# -------------------------
def draw_ui():
    pygame.draw.rect(screen,UI_BG,(0,0,WIDTH,60))
    rescued = sum(1 for h in humans if h.rescued)
    total = len(humans)
    elapsed = int(time.time()-start_time)

    screen.blit(font.render(f"Saved: {rescued}/{total}", True, WHITE), (20,20))
    screen.blit(font.render(f"Time: {elapsed}s", True, WHITE), (180,20))
    screen.blit(font.render(f"Score: {score}", True, WHITE), (320,20))

    mode = "AUTO" if auto_mode else "MANUAL"
    pygame.draw.rect(screen,UI_CARD,(450,10,120,40),border_radius=8)
    screen.blit(font.render(mode,True,WHITE),(480,20))

# -------------------------
# Screens
# -------------------------
def draw_start():
    draw_bg()

    title = big_font.render("LIFELINE AI", True, (50,50,80))
    screen.blit(title,(250,120))

    subtitle = font.render("Rescue Mission Simulator", True, (80,80,110))
    screen.blit(subtitle,(300,180))

    pygame.draw.rect(screen, UI_CARD, (300,250,300,160), border_radius=12)

    lines = [
        "Press 1 → Easy",
        "Press 2 → Medium",
        "Press 3 → Hard",
        "",
        "Arrow Keys → Move",
        "A → Auto | P → Pause"
    ]

    for i,line in enumerate(lines):
        screen.blit(font.render(line, True, WHITE),(320,270+i*25))

def draw_end():
    draw_bg()
    msg = big_font.render("MISSION COMPLETE", True, (20,120,20))
    screen.blit(msg,(200,180))
    screen.blit(font.render(f"Score: {score}", True, WHITE),(380,260))

# -------------------------
# Logic
# -------------------------
def check_rescue():
    global score, state
    for h in humans:
        if not h.rescued:
            if abs(drone.x-h.x)<15 and abs(drone.y-h.y)<25:
                h.rescued=True
                score+=100

    if all(h.rescued for h in humans):
        state=END

def auto_move():
    targets=[h for h in humans if not h.rescued]
    if not targets: return
    t=targets[0]

    if drone.x<t.x: drone.x+=drone.speed
    elif drone.x>t.x: drone.x-=drone.speed
    if drone.y<t.y: drone.y+=drone.speed
    elif drone.y>t.y: drone.y-=drone.speed

# -------------------------
# Main Loop
# -------------------------
running=True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

        if state==START:
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_1:
                    init_game(1); state=PLAY; start_time=time.time()
                if event.key==pygame.K_2:
                    init_game(2); state=PLAY; start_time=time.time()
                if event.key==pygame.K_3:
                    init_game(3); state=PLAY; start_time=time.time()

        elif state==PLAY:
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_a: auto_mode=not auto_mode
                if event.key==pygame.K_p: state=PAUSE

        elif state==PAUSE:
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_p: state=PLAY

    update_bg()
    drone.update()
    for h in humans: h.update()
    for hz in hazards: hz.update()

    if state==START:
        draw_start()

    elif state==PLAY:
        keys=pygame.key.get_pressed()
        if auto_mode: auto_move()
        else: drone.move(keys)

        draw_bg()

        for hz in hazards: draw_hazard(hz)
        for h in humans:
            if not h.rescued: draw_human(h)

        draw_drone()
        draw_ui()
        check_rescue()

    elif state==PAUSE:
        draw_ui()
        pause_text = big_font.render("PAUSED", True, WHITE)
        screen.blit(pause_text,(350,200))

    elif state==END:
        draw_end()

    pygame.display.update()

pygame.quit()
sys.exit()