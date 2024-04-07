import pygame
import os
import sys
from sysconfig import get_makefile_filename
import cv2
import mediapipe as mp
import time
import spritesheet
from sprites import *
from HealthBar import healthbar
pygame.init()
start_time = pygame.time.get_ticks()
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height),pygame.RESIZABLE)
pygame.display.set_caption("Gesture-Controlled Space Invaders")
clock=pygame.time.Clock()

start_time = pygame.time.get_ticks()
time1=0
check=0
index=0#player attack
index1=0#enemy attack
index2=0#player dead
index3=0#enemy dead

player_x = 310-20-20
player_y = 125+125+50+50+30
enemy_x=410-20-20
enemy_y=25+125+50+50+30
enemy_health=100
player_health=100
health_bar=healthbar(22,38,187,36,player_health)
enemy_health_bar=healthbar(22,38,187,36,enemy_health)

running=True

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
update_interval = 0.1
last_update_time = time.time()
cap = cv2.VideoCapture(0)
thumbs_up=False
check = 0
dgmap = pygame.image.load("battle.png")
# dgmap1 = pygame.transform.scale(dgmap, (800,600))
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    current_time = pygame.time.get_ticks()
    elapsed_time = (current_time - start_time)//1000
    screen.blit(dgmap, (0,0))
    health_bar.bdraw(player_health,screen)
    enemy_health_bar.bdraw(enemy_health,screen)
    clock.tick(900)
    dt=clock.tick(15)
    time1=time1+clock.tick(120)
    if(player_health<=0):
        if(index2 != len(player_dead)-1):
            index2 = (index2 + 1) % len(player_dead)
            time1 = 0
            screen.blit(player_dead[index2], (player_x, player_y)) 
            screen.blit(enemy_attack[0],(enemy_x,enemy_y))
        else:
             running=False
            #  sys.exit(0)

    elif(enemy_health<=0):
        if(index3 != len(enemy_dead)-1):
            index3 = (index3 + 1) % len(enemy_dead)
            time1 = 0
            screen.blit(enemy_dead[index3], (enemy_x, enemy_y+70)) 
            screen.blit(player_attack[0],(player_x,player_y))
        else:
             running=False
            #  sys.exit(1)
    else:        
        _, frame = cap.read()

        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = hands.process(rgb_frame)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                
                thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
                index_finger_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]

                
                distance = cv2.norm(
                    (thumb_tip.x, thumb_tip.y),
                    (index_finger_tip.x, index_finger_tip.y)
                )
                
                if thumb_tip.y<index_finger_tip.y:  
                    thumbs_up=True
                else:
                    thumbs_up=False
                if thumbs_up:
                    index = (index + 1) % len(player_attack)
                    time1 = 0
                    enemy_health-=1
                    screen.blit(player_attack[index], (player_x, player_y))
                else:
                    time1 = 0
                    screen.blit(player_attack[0],(player_x,player_y))
                    screen.blit(shield[0], (player_x+100, player_y-30))
                    screen.blit(shield[0], (player_x+100, player_y+30))
                    screen.blit(shield[0], (player_x+100, player_y+90))
                    screen.blit(shield[0], (player_x+100, player_y+150))
                if((elapsed_time//5)%2 == 1):
                    index1 = (index1 + 1) % len(enemy_attack)
                    time1 = 0
                    dt=clock.tick(25)
                    if(thumbs_up):
                        player_health-=10
                        screen.blit(enemy_attack[index1], (enemy_x-60, enemy_y))
                    else:
                        screen.blit(enemy_attack[index1], (enemy_x, enemy_y))
                        
                else:
                    time1 = 0
                    screen.blit(enemy_attack[0], (enemy_x-60, enemy_y))
                
                    
        else:
            index = (index + 1) % len(player_defend)
            time1 = 0
            screen.blit(player_defend[index], (player_x, player_y))
            if((elapsed_time//5)%2 == 0):
                        index1 = (index1 + 1) % len(enemy_attack)
                        time1 = 0
                        dt=clock.tick(25)
                        player_health-=10
                        screen.blit(enemy_attack[index1], (enemy_x-60, enemy_y))
            else:
                    time1 = 0
                    screen.blit(enemy_attack[0], (enemy_x-60, enemy_y))

    pygame.display.flip()
cap.release()
cv2.destroyAllWindows()
pygame.quit()