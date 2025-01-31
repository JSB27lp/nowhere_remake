from head import *

class Character(pygame.sprite.Sprite, CharacterSound):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self) 
        CharacterSound.__init__(self) 

        self.surf = character_standing_sheet_surf.subsurface((0,0,100,150))
        self.mask = pygame.mask.from_surface(character_mask)
        self.rect = self.surf.get_rect()
   
        self.pos = vec((WIDTH/2,HEIGHT/2))
        self.vel = vec(0,0)
        self.last_direction = ""

        self.index_frame = 0 #that keeps track on the current index of the image list.
        self.current_frame = 0 #that keeps track on the current time or current frame since last the index switched.
        self.animation_frames = 3 #that define how many seconds or frames should pass before switching image.
        
        self.velocity = 6#6
        self.slowvelocity = False
        self.ratioslowvelocity = 3

    def update(self):   
        if self.vel != vec(0,0):
            direction = pygame.math.Vector2.normalize(self.vel)
        else :
            direction = self.vel

        velocity = self.velocity
        if self.slowvelocity :
            velocity = self.velocity / self.ratioslowvelocity

        self.pos += direction * velocity

        self.rect.midbottom = self.pos

        blocks_hit_list = pygame.sprite.spritecollide(self, collide_sprite_group, False, collided = pygame.sprite.collide_mask)
        if blocks_hit_list:
            self.pos -= direction * velocity
            self.rect.midbottom = self.pos 

    def display(self,room):
        self.animate()
        self.playSound()
        if (self.pos.x < room.rect.left +30 or self.pos.x > room.rect.right -30) and self.pos.y < room.rect.bottom - 185:
            pass
        else :
            screen.blit(self.surf, (self.rect.x, self.rect.y))

    def animate(self):
        if self.vel.x == 0 and self.vel.y == 0:
            if self.last_direction == "walk_EAST_Sheet":
                self.surf = character_standing_sheet_surf.subsurface((100*7,0,100,150))
            elif self.last_direction == "walk_NORTH_EAST_Sheet":
                self.surf = character_standing_sheet_surf.subsurface((100*6,0,100,150))
            elif self.last_direction == "walk_NORTH_Sheet":
                self.surf = character_standing_sheet_surf.subsurface((100*5,0,100,150))
            elif self.last_direction == "walk_NORTH_WEST_Sheet":
                self.surf = character_standing_sheet_surf.subsurface((100*4,0,100,150))
            elif self.last_direction == "walk_WEST_Sheet":
                self.surf = character_standing_sheet_surf.subsurface((100*3,0,100,150))
            elif self.last_direction == "walk_SOUTH_WEST_Sheet":
                self.surf = character_standing_sheet_surf.subsurface((100*2,0,100,150))
            elif self.last_direction == "walk_SOUTH_Sheet":
                self.surf = character_standing_sheet_surf.subsurface((100*1,0,100,150))
            elif self.last_direction == "walk_SOUTH_EAST_Sheet":
                self.surf = character_standing_sheet_surf.subsurface((100*0,0,100,150))
        elif self.vel.x > 0 and self.vel.y == 0:
            self.surf = walk_EAST_Sheet.subsurface((100*self.index_frame,0,100,150))
            self.last_direction = "walk_EAST_Sheet"
        elif self.vel.x > 0 and self.vel.y < 0:
            self.surf = walk_NORTH_EAST_Sheet.subsurface((100*self.index_frame,0,100,150))
            self.last_direction = "walk_NORTH_EAST_Sheet"
        elif self.vel.x == 0 and self.vel.y < 0:
            self.surf = walk_NORTH_Sheet.subsurface((100*self.index_frame,0,100,150))
            self.last_direction = "walk_NORTH_Sheet"
        elif self.vel.x < 0 and self.vel.y < 0:
            self.surf = walk_NORTH_WEST_Sheet.subsurface((100*self.index_frame,0,100,150))
            self.last_direction = "walk_NORTH_WEST_Sheet"
        elif self.vel.x < 0 and self.vel.y == 0:
            self.surf = walk_WEST_Sheet.subsurface((100*self.index_frame,0,100,150))
            self.last_direction = "walk_WEST_Sheet"
        elif self.vel.x < 0 and self.vel.y > 0:
            self.surf = walk_SOUTH_WEST_Sheet.subsurface((100*self.index_frame,0,100,150))
            self.last_direction = "walk_SOUTH_WEST_Sheet"
        elif self.vel.x == 0 and self.vel.y > 0:
            self.surf = walk_SOUTH_Sheet.subsurface((100*self.index_frame,0,100,150))
            self.last_direction = "walk_SOUTH_Sheet"
        elif self.vel.x > 0 and self.vel.y > 0:
            self.surf = walk_SOUTH_EAST_Sheet.subsurface((100*self.index_frame,0,100,150))
            self.last_direction = "walk_SOUTH_EAST_Sheet"

        self.current_frame += 1
        if self.current_frame >= self.animation_frames:
            self.current_frame = 0
            self.index_frame += 1
            if self.index_frame >= 8 :
                self.index_frame = 0          

class Player(Character):
    def __init__(self):
        super().__init__()  

    def deathOrNot(self):
        return False

    def controlsJoystick(self):
        if pygame.joystick.get_count()>0:
            hat = joysticks[0].get_hat(0)
            self.vel.x = hat[0]
            self.vel.y = hat[1] * -1

            axis_pos = joysticks[0].get_axis(0)
            if axis_pos < -1 * deadzone:
                self.vel.x -= 1
            elif axis_pos > deadzone:
                self.vel.x += 1 
            else:
                self.vel.x = 0
            axis_pos = joysticks[0].get_axis(1)
            if axis_pos < -1 * deadzone:
                self.vel.y -= 1
            elif axis_pos > deadzone:
                self.vel.y += 1 
            else:
                self.vel.y = 0

    def controls(self,event):

        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:  
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key == pygame.K_q or event.key == pygame.K_LEFT:
                self.vel.x = -1
            if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                self.vel.x = 1 
            if event.key == pygame.K_z or event.key == pygame.K_UP:
                self.vel.y = -1
            if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                self.vel.y = 1
        if event.type == pygame.KEYUP:   
            if (event.key == pygame.K_q or event.key == pygame.K_LEFT) or (event.key == pygame.K_d or event.key == pygame.K_RIGHT):
                self.vel.x = 0
            if (event.key == pygame.K_z or event.key == pygame.K_UP) or (event.key == pygame.K_s or event.key == pygame.K_DOWN):
                self.vel.y = 0

        self.controlsJoystick()

class Bot(Character):
    def __init__(self,room):
        super().__init__()  
 
        self.pos.x = random.randint(room.rect.x+295,room.rect.x+1183)
        self.pos.y = random.randint(room.rect.y+460,room.rect.y+805)

    def move(self,room):
        magic_number = random.randint(1,9)
        if magic_number == 1:
            self.vel.x = 1
            self.vel.y = 0
        elif magic_number == 2:
            self.vel.x = -1
            self.vel.y = 0
        elif magic_number == 3:
            self.vel.x = 0
            self.vel.y = 1
        elif magic_number == 4:
            self.vel.x = 0
            self.vel.y = -1
        elif magic_number == 5:
            self.vel.x = 1
            self.vel.y = 1
        elif magic_number == 6:
            self.vel.x = -1
            self.vel.y = -1
        elif magic_number == 7:
            self.vel.x = 1
            self.vel.y = -1
        elif magic_number == 9:
            self.vel.x = -1
            self.vel.y = 1
        elif magic_number == 9:
            self.vel.x = 0
            self.vel.y = 0

        if self.pos.x > room.rect.x+1183 :
            self.vel.x = -1
        if self.pos.x < room.rect.x+295 :
            self.vel.x = 1

class Room(pygame.sprite.Sprite):
    def __init__(self, room_name_):
        super().__init__()  

        self.name = room_name_

        self.surf = pygame.image.load("assets/rooms/"+room_name_+".png").convert_alpha()

        tmp_room_mask = pygame.image.load("assets/rooms/"+room_name_+"_mask.png").convert_alpha()
        self.mask = pygame.mask.from_surface(tmp_room_mask)

        self.front = pygame.image.load("assets/rooms/"+room_name_+"_front.png").convert_alpha()

        self.rect = self.surf.get_rect(center = (WIDTH/2, HEIGHT/2))

        self.bg_color = (0,0,0)

    def display(self):
        self.animate()
        screen.blit(self.surf, (self.rect.x, self.rect.y))

    def animate(self):
        pass


        