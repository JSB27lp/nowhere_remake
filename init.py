import pygame
from pygame.locals import *
import random
import sys
from datetime import datetime

pygame.init()
joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
vec = pygame.math.Vector2 #2 for two dimensional
FPS = 60
deadzone = 0.3#for joystick
FramePerSec = pygame.time.Clock()
screen = pygame.display.set_mode((0, 0),pygame.NOFRAME,32)
pygame.mouse.set_visible(False) # Hide cursor here
pygame.display.set_caption("nowhere")
infoObject = pygame.display.Info()
WIDTH = infoObject.current_w
HEIGHT = infoObject.current_h


footstep_sound = pygame.mixer.Sound("assets/sounds/step.wav")

background_image = pygame.image.load("assets/MY1SYe.jpg").convert()

character_standing_sheet_surf = pygame.image.load("assets/character/neonblue&purple_8direction_standing-Sheet.png").convert_alpha()
walk_EAST_Sheet = pygame.image.load("assets/character/neonblue&purple_walk_EAST-Sheet.png").convert_alpha()
walk_NORTH_EAST_Sheet = pygame.image.load("assets/character/neonblue&purple_walk_NORTH-EAST-Sheet.png").convert_alpha()
walk_NORTH_Sheet = pygame.image.load("assets/character/neonblue&purple_walk_NORTH-Sheet.png").convert_alpha()
walk_NORTH_WEST_Sheet = pygame.image.load("assets/character/neonblue&purple_walk_NORTH-WEST-Sheet.png").convert_alpha()
walk_SOUTH_EAST_Sheet = pygame.image.load("assets/character/neonblue&purple_walk_SOUTH-EAST-Sheet.png").convert_alpha()
walk_SOUTH_Sheet = pygame.image.load("assets/character/neonblue&purple_walk_SOUTH-Sheet.png").convert_alpha()
walk_SOUTH_WEST_Sheet = pygame.image.load("assets/character/neonblue&purple_walk_SOUTH-WEST-Sheet.png").convert_alpha()
walk_WEST_Sheet = pygame.image.load("assets/character/neonblue&purple_walk_WEST-Sheet.png").convert_alpha()
character_mask = pygame.image.load("assets/character/mask2.png").convert_alpha()

character_standing_sheet_surfRED = pygame.image.load("assets/character/red_8direction_standing-Sheet.png").convert_alpha()
walk_EAST_SheetRED = pygame.image.load("assets/character/red_walk_EAST-Sheet.png").convert_alpha()
walk_NORTH_EAST_SheetRED = pygame.image.load("assets/character/red_walk_NORTH-EAST-Sheet.png").convert_alpha()
walk_NORTH_SheetRED = pygame.image.load("assets/character/red_walk_NORTH-Sheet.png").convert_alpha()
walk_NORTH_WEST_SheetRED = pygame.image.load("assets/character/red_walk_NORTH-WEST-Sheet.png").convert_alpha()
walk_SOUTH_EAST_SheetRED = pygame.image.load("assets/character/red_walk_SOUTH-EAST-Sheet.png").convert_alpha()
walk_SOUTH_SheetRED = pygame.image.load("assets/character/red_walk_SOUTH-Sheet.png").convert_alpha()
walk_SOUTH_WEST_SheetRED = pygame.image.load("assets/character/red_walk_SOUTH-WEST-Sheet.png").convert_alpha()
walk_WEST_SheetRED = pygame.image.load("assets/character/red_walk_WEST-Sheet.png").convert_alpha()

character_standing_sheet_surf = pygame.transform.scale(character_standing_sheet_surf, (800,150))
walk_EAST_Sheet = pygame.transform.scale(walk_EAST_Sheet, (800,150))
walk_NORTH_EAST_Sheet = pygame.transform.scale(walk_NORTH_EAST_Sheet, (800,150))
walk_NORTH_Sheet = pygame.transform.scale(walk_NORTH_Sheet, (800,150))
walk_NORTH_WEST_Sheet = pygame.transform.scale(walk_NORTH_WEST_Sheet, (800,150))
walk_SOUTH_EAST_Sheet = pygame.transform.scale(walk_SOUTH_EAST_Sheet, (800,150))
walk_SOUTH_Sheet = pygame.transform.scale(walk_SOUTH_Sheet, (800,150))
walk_SOUTH_WEST_Sheet = pygame.transform.scale(walk_SOUTH_WEST_Sheet, (800,150))
walk_WEST_Sheet = pygame.transform.scale(walk_WEST_Sheet, (800,150))

character_standing_sheet_surfRED = pygame.transform.scale(character_standing_sheet_surfRED, (800,150))
walk_EAST_SheetRED = pygame.transform.scale(walk_EAST_SheetRED, (800,150))
walk_NORTH_EAST_SheetRED = pygame.transform.scale(walk_NORTH_EAST_SheetRED, (800,150))
walk_NORTH_SheetRED = pygame.transform.scale(walk_NORTH_SheetRED, (800,150))
walk_NORTH_WEST_SheetRED = pygame.transform.scale(walk_NORTH_WEST_SheetRED, (800,150))
walk_SOUTH_EAST_SheetRED = pygame.transform.scale(walk_SOUTH_EAST_SheetRED, (800,150))
walk_SOUTH_SheetRED = pygame.transform.scale(walk_SOUTH_SheetRED, (800,150))
walk_SOUTH_WEST_SheetRED = pygame.transform.scale(walk_SOUTH_WEST_SheetRED, (800,150))
walk_WEST_SheetRED = pygame.transform.scale(walk_WEST_SheetRED, (800,150))

color_cube = pygame.image.load("assets/objects/color_cube.png").convert_alpha()
color_cube_sheet = pygame.image.load("assets/objects/color_cube_sheet2.png").convert_alpha()
color_cube_mask = pygame.image.load("assets/objects/color_cube_mask.png").convert_alpha()

color_cubebig_mask = pygame.image.load("assets/objects/color_cubebig_mask3.png").convert_alpha()
color_cubebig_front = pygame.image.load("assets/objects/color_cubebig_front.png").convert_alpha()

color_losange = pygame.image.load("assets/objects/color_losange.png").convert_alpha()
color_losange_mask = pygame.image.load("assets/objects/color_losange_mask.png").convert_alpha()

color_cubebig_checkpoint = pygame.image.load("assets/objects/color_cubebig_checkpoint3.png").convert_alpha()

flamme_sheet = pygame.image.load("assets/objects/flamme.png").convert_alpha()
flamme_mask = pygame.image.load("assets/objects/flamme_mask.png").convert_alpha()

lampad = pygame.image.load("assets/objects/lampad3.png").convert_alpha()
lampad_mask = pygame.image.load("assets/objects/lampad3_mask.png").convert_alpha()

lampad_hitbox_for_light = pygame.image.load("assets/objects/lampad_hitbox_for_light.png").convert_alpha()

candle_hitbox = pygame.image.load("assets/objects/candle_hitbox.png").convert_alpha()

character_standing_sheet_surfBLUE = pygame.image.load("assets/character/blue_8direction_standing-Sheet.png").convert_alpha()
walk_EAST_SheetBLUE = pygame.image.load("assets/character/blue_walk_EAST-Sheet.png").convert_alpha()
walk_NORTH_EAST_SheetBLUE = pygame.image.load("assets/character/blue_walk_NORTH-EAST-Sheet.png").convert_alpha()
walk_NORTH_SheetBLUE = pygame.image.load("assets/character/blue_walk_NORTH-Sheet.png").convert_alpha()
walk_NORTH_WEST_SheetBLUE = pygame.image.load("assets/character/blue_walk_NORTH-WEST-Sheet.png").convert_alpha()
walk_SOUTH_EAST_SheetBLUE = pygame.image.load("assets/character/blue_walk_SOUTH-EAST-Sheet.png").convert_alpha()
walk_SOUTH_SheetBLUE = pygame.image.load("assets/character/blue_walk_SOUTH-Sheet.png").convert_alpha()
walk_SOUTH_WEST_SheetBLUE = pygame.image.load("assets/character/blue_walk_SOUTH-WEST-Sheet.png").convert_alpha()
walk_WEST_SheetBLUE = pygame.image.load("assets/character/blue_walk_WEST-Sheet.png").convert_alpha()

character_standing_sheet_surfBLUE = pygame.transform.scale(character_standing_sheet_surfBLUE, (800,150))
walk_EAST_SheetBLUE = pygame.transform.scale(walk_EAST_SheetBLUE, (800,150))
walk_NORTH_EAST_SheetBLUE = pygame.transform.scale(walk_NORTH_EAST_SheetBLUE, (800,150))
walk_NORTH_SheetBLUE = pygame.transform.scale(walk_NORTH_SheetBLUE, (800,150))
walk_NORTH_WEST_SheetBLUE = pygame.transform.scale(walk_NORTH_WEST_SheetBLUE, (800,150))
walk_SOUTH_EAST_SheetBLUE = pygame.transform.scale(walk_SOUTH_EAST_SheetBLUE, (800,150))
walk_SOUTH_SheetBLUE = pygame.transform.scale(walk_SOUTH_SheetBLUE, (800,150))
walk_SOUTH_WEST_SheetBLUE = pygame.transform.scale(walk_SOUTH_WEST_SheetBLUE, (800,150))
walk_WEST_SheetBLUE = pygame.transform.scale(walk_WEST_SheetBLUE, (800,150))

front_door = pygame.image.load("assets/objects/front_door.png").convert_alpha()
back_door = pygame.image.load("assets/objects/back_door.png").convert_alpha()
right_door = pygame.image.load("assets/objects/right_door.png").convert_alpha()
left_door = pygame.image.load("assets/objects/left_door.png").convert_alpha()

blood_room_jail2_flask = pygame.image.load("assets/objects/blood_room_jail2_flask.png").convert_alpha()

eye_img = pygame.image.load("assets/objects/eye.png").convert_alpha()