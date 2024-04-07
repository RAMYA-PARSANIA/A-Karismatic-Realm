import pygame
import spritesheet

width = 800
height = 600
screen=pygame.display.set_mode((width,height), pygame.RESIZABLE)
black=000
#clock=pygame.time.Clock()

black=000
sprite_sheet_image=pygame.image.load('Knight_01__ATTACK_000.png').convert_alpha() 
sprite_sheet=spritesheet.sprite_sheet(sprite_sheet_image)
player_idle=[sprite_sheet.image(0.8,220,200,2,black)]

sprite_sheet_image=pygame.image.load('1_shield_.png').convert_alpha() 
sprite_sheet=spritesheet.sprite_sheet(sprite_sheet_image)
shield=[sprite_sheet.image(0,220,200,2,black)]


sprite_sheet_image=pygame.image.load('Knight_01__ATTACK_000.png').convert_alpha()
sprite_sheet=spritesheet.sprite_sheet(sprite_sheet_image)
player_attack=[sprite_sheet.image(0.8,220,200,2,black)]

sprite_sheet_image=pygame.image.load('Knight_01__ATTACK_001.png').convert_alpha()
sprite_sheet=spritesheet.sprite_sheet(sprite_sheet_image)
#player_attack.extend([sprite_sheet.image(0.8,220,200,2,black)])

sprite_sheet_image=pygame.image.load('Knight_01__ATTACK_002.png').convert_alpha()
sprite_sheet=spritesheet.sprite_sheet(sprite_sheet_image)
player_attack.extend([sprite_sheet.image(0.8,220,200,2,black)])

sprite_sheet_image=pygame.image.load('Knight_01__ATTACK_003.png').convert_alpha()
sprite_sheet=spritesheet.sprite_sheet(sprite_sheet_image)
#player_attack.extend([sprite_sheet.image(0.8,220,200,2,black)])

sprite_sheet_image=pygame.image.load('Knight_01__ATTACK_004.png').convert_alpha()
sprite_sheet=spritesheet.sprite_sheet(sprite_sheet_image)
player_attack.extend([sprite_sheet.image(0.8,220,200,2,black)])

sprite_sheet_image=pygame.image.load('Knight_01__ATTACK_005.png').convert_alpha()
sprite_sheet=spritesheet.sprite_sheet(sprite_sheet_image)
#player_attack.extend([sprite_sheet.image(0.8,220,200,2,black)])

sprite_sheet_image=pygame.image.load('Knight_01__ATTACK_006.png').convert_alpha()
sprite_sheet=spritesheet.sprite_sheet(sprite_sheet_image)
player_attack.extend([sprite_sheet.image(0.8,220,200,2,black)])

sprite_sheet_image=pygame.image.load('Knight_01__ATTACK_007.png').convert_alpha()
sprite_sheet=spritesheet.sprite_sheet(sprite_sheet_image)
#player_attack.extend([sprite_sheet.image(0.8,220,200,2,black)])

sprite_sheet_image=pygame.image.load('Knight_01__ATTACK_008.png').convert_alpha()
sprite_sheet=spritesheet.sprite_sheet(sprite_sheet_image)
player_attack.extend([sprite_sheet.image(0.8,220,200,2,black)])

sprite_sheet_image=pygame.image.load('Knight_01__ATTACK_009.png').convert_alpha()
sprite_sheet=spritesheet.sprite_sheet(sprite_sheet_image)
player_attack.extend([sprite_sheet.image(0.8,220,200,2,black)])

sprite_sheet_image=pygame.image.load('Knight_01__ATTACK_007.png').convert_alpha()
sprite_sheet=spritesheet.sprite_sheet(sprite_sheet_image)
player_defend=([sprite_sheet.image(0.8,220,200,2,black)])

sprite_sheet_image=pygame.image.load('Knight_01__ATTACK_000.png').convert_alpha()
sprite_sheet=spritesheet.sprite_sheet(sprite_sheet_image)
player_idle=[sprite_sheet.image(0.8,220,200,2,black)]

sprite_sheet_image=pygame.image.load('Knight_01__DIE_000.png').convert_alpha()
sprite_sheet=spritesheet.sprite_sheet(sprite_sheet_image)
player_dead=[sprite_sheet.image(0.6,220,200,2,black)]

sprite_sheet_image=pygame.image.load('Knight_01__DIE_001.png').convert_alpha()
sprite_sheet=spritesheet.sprite_sheet(sprite_sheet_image)
player_dead.extend([sprite_sheet.image(0.6,220,200,2,black)])

sprite_sheet_image=pygame.image.load('Knight_01__DIE_002.png').convert_alpha()
sprite_sheet=spritesheet.sprite_sheet(sprite_sheet_image)
player_dead.extend([sprite_sheet.image(0.6,220,200,2,black)])

sprite_sheet_image=pygame.image.load('Knight_01__DIE_003.png').convert_alpha()
sprite_sheet=spritesheet.sprite_sheet(sprite_sheet_image)
player_dead.extend([sprite_sheet.image(0.6,220,200,2,black)])

sprite_sheet_image=pygame.image.load('Knight_01__DIE_004.png').convert_alpha()
sprite_sheet=spritesheet.sprite_sheet(sprite_sheet_image)
player_dead.extend([sprite_sheet.image(0.6,220,200,2,black)])

sprite_sheet_image=pygame.image.load('Knight_01__DIE_005.png').convert_alpha()
sprite_sheet=spritesheet.sprite_sheet(sprite_sheet_image)
player_dead.extend([sprite_sheet.image(0.6,220,200,2,black)])

sprite_sheet_image=pygame.image.load('Knight_01__DIE_006.png').convert_alpha()
sprite_sheet=spritesheet.sprite_sheet(sprite_sheet_image)
player_dead.extend([sprite_sheet.image(0.6,220,200,2,black)])

sprite_sheet_image=pygame.image.load('Knight_01__DIE_007.png').convert_alpha()
sprite_sheet=spritesheet.sprite_sheet(sprite_sheet_image)
player_dead.extend([sprite_sheet.image(0.6,220,200,2,black)])

sprite_sheet_image=pygame.image.load('Knight_01__DIE_008.png').convert_alpha()
sprite_sheet=spritesheet.sprite_sheet(sprite_sheet_image)
player_dead.extend([sprite_sheet.image(0.6,220,200,2,black)])

sprite_sheet_image=pygame.image.load('Knight_01__DIE_009.png').convert_alpha()
sprite_sheet=spritesheet.sprite_sheet(sprite_sheet_image)
player_dead.extend([sprite_sheet.image(0.6,220,200,2,black)])

d1=pygame.image.load('Dead_001.png').convert_alpha()
sprite_sheet5=spritesheet.sprite_sheet(d1)
enemy_dead=[sprite_sheet5.image(0.13,330,300,2,black)]

d1=pygame.image.load('Dead_002.png').convert_alpha()
sprite_sheet5=spritesheet.sprite_sheet(d1)
enemy_dead.extend([sprite_sheet5.image(0.13,330,300,2,black)])

d1=pygame.image.load('Dead_003.png').convert_alpha()
sprite_sheet5=spritesheet.sprite_sheet(d1)
enemy_dead.extend([sprite_sheet5.image(0.1,330,300,2,black)])

d1=pygame.image.load('Dead_004.png').convert_alpha()
sprite_sheet5=spritesheet.sprite_sheet(d1)
enemy_dead.extend([sprite_sheet5.image(0.1,330,300,2,black)])

d1=pygame.image.load('Dead_005.png').convert_alpha()
sprite_sheet5=spritesheet.sprite_sheet(d1)
enemy_dead.extend([sprite_sheet5.image(0.08,330,300,2,black)])

d1=pygame.image.load('Dead_006.png').convert_alpha()
sprite_sheet5=spritesheet.sprite_sheet(d1)
enemy_dead.extend([sprite_sheet5.image(0.1,330,300,2,black)])

d1=pygame.image.load('Dead_007.png').convert_alpha()
sprite_sheet5=spritesheet.sprite_sheet(d1)
enemy_dead.extend([sprite_sheet5.image(0.13,330,300,2,black)])

d1=pygame.image.load('Dead_008.png').convert_alpha()
sprite_sheet5=spritesheet.sprite_sheet(d1)
enemy_dead.extend([sprite_sheet5.image(0.13,330,300,2,black)])

d1=pygame.image.load('Dead_009.png').convert_alpha()
sprite_sheet5=spritesheet.sprite_sheet(d1)
enemy_dead.extend([sprite_sheet5.image(0.1,330,300,2,black)])

d1=pygame.image.load('Attack_000.png').convert_alpha()
sprite_sheet5=spritesheet.sprite_sheet(d1)
enemy_attack=([sprite_sheet5.image(0,330,300,2,black)])

d1=pygame.image.load('Attack_001.png').convert_alpha()
sprite_sheet5=spritesheet.sprite_sheet(d1)
enemy_attack.extend([sprite_sheet5.image(0,330,300,2,black)])

d1=pygame.image.load('Attack_002.png').convert_alpha()
sprite_sheet5=spritesheet.sprite_sheet(d1)
enemy_attack.extend([sprite_sheet5.image(0,330,300,2,black)])

d1=pygame.image.load('Attack_003.png').convert_alpha()
sprite_sheet5=spritesheet.sprite_sheet(d1)
enemy_attack.extend([sprite_sheet5.image(0,330,300,2,black)])

d1=pygame.image.load('Attack_004.png').convert_alpha()
sprite_sheet5=spritesheet.sprite_sheet(d1)
enemy_attack.extend([sprite_sheet5.image(0,330,300,2,black)])

d1=pygame.image.load('Attack_005.png').convert_alpha()
sprite_sheet5=spritesheet.sprite_sheet(d1)
enemy_attack.extend([sprite_sheet5.image(0,330,300,2,black)])
'''print(len(player_attack))
pygame.init()
running =True
screen.fill((40,40,40))
time=0
index=0
while running:
    clock.tick(25)
    dt=clock.tick(25)
    time+=clock.tick(120)
    index=(1+index)%len(enemy_attack)
    time=0
    screen.blit(enemy_attack[index],(0,0))
    #screen.blit(run[1],(100,0))
    #screen.blit(run[2],(200,0))
    #screen.blit(run[3],(0,100))
    #screen.blit(run[4],(0,200))
    #screen.blit(run[5],(100,100))
    pygame.display.flip()
pygame.quit()'''
