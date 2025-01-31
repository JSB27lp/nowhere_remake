from head import *

class Personnage(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()  

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

    def move(self):   
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

        if self.flamme :
            self.flamme.rect.midbottom = self.pos
            self.flamme.rect.y -= 30

        self.animate()            

class Player(Personnage, CharacterSound):
    def __init__(self):
        Personnage.__init__(self) 
        CharacterSound.__init__(self) 
        self.dead = False
        self.flamme = None

    def amIdead(self):
        blocks_hit_list = pygame.sprite.spritecollide(self, enemies_sprite_group, False, collided = pygame.sprite.collide_mask)
        if blocks_hit_list:
            return True
        else :
            return False
        
    def test_if_i_can_become_light(self,flamme):
        if flamme :
            hitbox_ = CandleHitbox()
            hit = pygame.sprite.collide_mask(self, hitbox_)
            if hit :
                if not self.flamme :
                    self.flamme = Flamme((self.pos.x,self.pos.y-100),2)
                return True
            else :
                return False
        else :
            return False

    def checkSpriteExistsnCollision(self,sprite):
        if sprite :
            hit = pygame.sprite.collide_mask(self, sprite)
            if hit :
                return True
            else :
                return False
        else :
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

        

    def animate(self):
        self.playSound()

        if self.flamme :
            self.flamme.animate()

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

class Bot(Personnage):
    def __init__(self,test_room):
        super().__init__()  
 
        self.pos.x = random.randint(test_room.rect.x+295,test_room.rect.x+1183)
        self.pos.y = random.randint(test_room.rect.y+460,test_room.rect.y+805)

        self.slowvelocity = True

        self.animation_frames = self.animation_frames*self.ratioslowvelocity

        self.flamme = None

    def path_finding(self,x,y):
        x_offset = self.pos.x - x
        y_offset = self.pos.y - y
        if x_offset < -1 :
            self.vel.x = 1
        elif x_offset > 1  :
            self.vel.x = -1
        else :
            self.vel.x = 0
        if y_offset < -1 :
            self.vel.y = 1
        elif y_offset > 1 :
            self.vel.y = -1
        else :
            self.vel.y = 0

    def animate(self):
        if self.vel.x == 0 and self.vel.y == 0:
            if self.last_direction == "walk_EAST_Sheet":
                self.surf = character_standing_sheet_surfRED.subsurface((100*7,0,100,150))
            elif self.last_direction == "walk_NORTH_EAST_Sheet":
                self.surf = character_standing_sheet_surfRED.subsurface((100*6,0,100,150))
            elif self.last_direction == "walk_NORTH_Sheet":
                self.surf = character_standing_sheet_surfRED.subsurface((100*5,0,100,150))
            elif self.last_direction == "walk_NORTH_WEST_Sheet":
                self.surf = character_standing_sheet_surfRED.subsurface((100*4,0,100,150))
            elif self.last_direction == "walk_WEST_Sheet":
                self.surf = character_standing_sheet_surfRED.subsurface((100*3,0,100,150))
            elif self.last_direction == "walk_SOUTH_WEST_Sheet":
                self.surf = character_standing_sheet_surfRED.subsurface((100*2,0,100,150))
            elif self.last_direction == "walk_SOUTH_Sheet":
                self.surf = character_standing_sheet_surfRED.subsurface((100*1,0,100,150))
            elif self.last_direction == "walk_SOUTH_EAST_Sheet":
                self.surf = character_standing_sheet_surfRED.subsurface((100*0,0,100,150))
        elif self.vel.x > 0 and self.vel.y == 0:
            self.surf = walk_EAST_SheetRED.subsurface((100*self.index_frame,0,100,150))
            self.last_direction = "walk_EAST_Sheet"
        elif self.vel.x > 0 and self.vel.y < 0:
            self.surf = walk_NORTH_EAST_SheetRED.subsurface((100*self.index_frame,0,100,150))
            self.last_direction = "walk_NORTH_EAST_Sheet"
        elif self.vel.x == 0 and self.vel.y < 0:
            self.surf = walk_NORTH_SheetRED.subsurface((100*self.index_frame,0,100,150))
            self.last_direction = "walk_NORTH_Sheet"
        elif self.vel.x < 0 and self.vel.y < 0:
            self.surf = walk_NORTH_WEST_SheetRED.subsurface((100*self.index_frame,0,100,150))
            self.last_direction = "walk_NORTH_WEST_Sheet"
        elif self.vel.x < 0 and self.vel.y == 0:
            self.surf = walk_WEST_SheetRED.subsurface((100*self.index_frame,0,100,150))
            self.last_direction = "walk_WEST_Sheet"
        elif self.vel.x < 0 and self.vel.y > 0:
            self.surf = walk_SOUTH_WEST_SheetRED.subsurface((100*self.index_frame,0,100,150))
            self.last_direction = "walk_SOUTH_WEST_Sheet"
        elif self.vel.x == 0 and self.vel.y > 0:
            self.surf = walk_SOUTH_SheetRED.subsurface((100*self.index_frame,0,100,150))
            self.last_direction = "walk_SOUTH_Sheet"
        elif self.vel.x > 0 and self.vel.y > 0:
            self.surf = walk_SOUTH_EAST_SheetRED.subsurface((100*self.index_frame,0,100,150))
            self.last_direction = "walk_SOUTH_EAST_Sheet"

        self.current_frame += 1
        if self.current_frame >= self.animation_frames:
            self.current_frame = 0
            self.index_frame += 1
            if self.index_frame >= 8 :
                self.index_frame = 0  

class Room(pygame.sprite.Sprite):
    def __init__(self, room_name_arguement,room_index):
        super().__init__()  

        self.name = room_name_arguement

        self.surf = pygame.image.load("assets/rooms/"+room_name_arguement+".png").convert_alpha()

        test_room_mask = None
        if room_name_arguement == "antichamber2" or room_name_arguement == "blood_room" or room_name_arguement == "test_room5" or room_name_arguement == "test_room4" or room_name_arguement == "back_room" or room_name_arguement == "antichamber":
            test_room_mask = pygame.image.load("assets/rooms/"+room_name_arguement+"_mask.png").convert_alpha()
        else :
            test_room_mask = pygame.image.load("assets/rooms/test_room_mask.png").convert_alpha()
        self.mask = pygame.mask.from_surface(test_room_mask)

        self.front = pygame.image.load("assets/rooms/"+room_name_arguement+"_front.png").convert_alpha()

        self.rect = self.surf.get_rect(center = (WIDTH/2, HEIGHT/2))

        self.color_cube = None
        self.color_losange = None

        self.flamme = None

        self.butterfly = None

        self.room_number = None

        self.check_point_back_room = None

        self.lampad = None

        if room_name_arguement == "back_room":
            self.check_point_back_room = CheckPointBackRoom()

        self.bg_color = (0,0,0)
        if room_name_arguement == "test_room0" :
            my_prison_text = "_ F I N D  Y O U R  P R I S O N"
            self.bg_color = (27,27,27)
            if (room_index >2 or room_index < -2) :
                self.add_cube()
            self.setNumPrison(room_index,my_prison_text)
        elif room_name_arguement == "test_room4" :
            self.bg_color = (255,255,255)
        elif room_name_arguement == "blood_room" or room_name_arguement == "blood_room_jail" :
            self.bg_color = (23,0,0)
            if room_name_arguement == "blood_room_jail" :
                self.setNumPrison(room_index,"_ L O O K I N G  F O R  A N O T H E R  J A I L")
                self.lampad = Lampad()
        elif room_name_arguement == "test_room5" :
            self.bg_color = (0,0,72)
            self.butterfly = ButterflyText()
        elif room_name_arguement == "antichamber2" :
            self.flamme = Flamme((self.rect.x + 820,self.rect.y + 460),1)

        self.cube_already_animated = False
        
    def setNumPrison(self,room_index,my_prison_text):
        str_ = '{num:#b}'.format(num=room_index)
        str_ += my_prison_text
        self.room_number = RoomNumber(str_)

    def animation(self,player):
        if self.flamme :
            self.flamme.animate()
        if player.checkSpriteExistsnCollision(self.color_losange):
            self.color_cube.animate()
            self.cube_already_animated = True
            
            if not self.check_point_back_room :
                self.check_point_back_room = CheckPointBackRoom()

        elif self.cube_already_animated :
            self.color_cube.concludeAnimation()

    def add_cube(self):
        if not self.color_cube :
            self.color_cube = ColorCube()
            self.color_losange = ColorLosange()

    def light_me(self,player_):
        mes_bool = False
        if player_.flamme and self.lampad :
            hitbox_ = LampadHitBoxFlamme()
            hit = pygame.sprite.collide_mask(hitbox_, player_)
            if hit :
                if not self.flamme :
                    self.flamme = Flamme((WIDTH/2,HEIGHT/2+50),3)
                    mes_bool = True
        return mes_bool


class ColorCube(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()  

        self.surf = color_cube
        self.mask = pygame.mask.from_surface(color_cube_mask)
        self.rect = self.surf.get_rect(center = (WIDTH/2, HEIGHT/2+100))

        self.special_front_for_hype = color_cubebig_front
        self.hyped = False

        self.index_frame = 0 #that keeps track on the current index of the image list.
        self.current_frame = 0 #that keeps track on the current time or current frame since last the index switched.
        self.animation_frames = 7 #that define how many seconds or frames should pass before switching image.

        self.bigcube_mask = pygame.mask.from_surface(color_cubebig_mask)

    def animate(self):
        self.mask = self.bigcube_mask

        self.surf = color_cube_sheet.subsurface((600*self.index_frame,0,600,600))

        self.current_frame += 1
        if self.current_frame >= self.animation_frames:
            self.current_frame = 0
            self.index_frame += 1
            if self.index_frame >= 11 :
                self.index_frame = 0

    def concludeAnimation(self):
        self.surf = color_cube_sheet.subsurface((600*self.index_frame,0,600,600))
        self.hyped = True

        if self.index_frame != 5 :
            self.current_frame += 1
            if self.current_frame >= self.animation_frames:
                self.current_frame = 0
                self.index_frame += 1
                if self.index_frame >= 11 :
                    self.index_frame = 0

class ColorLosange(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()  

        self.surf = color_losange
        self.mask = pygame.mask.from_surface(color_losange_mask)
        self.rect = self.surf.get_rect()
        self.rect.midbottom = vec(WIDTH/2,HEIGHT)

class CheckPointBackRoom(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()  

        self.surf = color_cubebig_checkpoint
        self.mask = pygame.mask.from_surface(color_cubebig_checkpoint)
        self.rect = self.surf.get_rect(center = (WIDTH/2, HEIGHT/2+100))

class RoomNumber(pygame.sprite.Sprite):
    def __init__(self,numb):
        super().__init__()  

        my_font = pygame.font.SysFont('Lucida Console', 20)
        self.surf = my_font.render(numb, False, (255, 0, 0))
        self.rect = self.surf.get_rect()
        self.rect.bottomleft = vec(WIDTH/2-440, HEIGHT/2-40)

class ButterflyText(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        
        image = pygame.Surface([520,360], pygame.SRCALPHA, 32)
        self.surf = image.convert_alpha()
        self.rect = self.surf.get_rect(center = (WIDTH/2, HEIGHT/2-300))

        list_of_text = []
        list_of_text.append("                `         '                ")
        list_of_text.append(";,,,             `       '             ,,,;")
        list_of_text.append("`YESXXXXno.       :     :       .on8888YES'")
        list_of_text.append("  88855NOW88b.     :   :     .d8HERE8DO88  ")
        list_of_text.append("  8DEATH'  `Y8b.   `   '   .d8Y'  `DEATH8  ")
        list_of_text.append(" jTHEE!  .db.  Yb. '   ' .dY  .db.  8THEE! ")
        list_of_text.append("   `???  Y72Y    `b ( ) d'    Y72Y  ???'   ")
        list_of_text.append("    2NO7  '`        ,',        ''  HERE    ")
        list_of_text.append("   NOWHEREnowhe`'   ':'   `'?r3no/nau/dk   ")
        list_of_text.append("     'Y'   .7'     d' 'b     '2.   'Y'     ")
        list_of_text.append("      !   .7' no  d'; ;`b  wher7e   !      ")
        list_of_text.append("         d34  `'  2 ; ; 7  `'  ere         ")
        list_of_text.append("        /hir/   .g8 ',' 8g.   dI88b        ")
        list_of_text.append("       :88DEATH55Y'     'Y34LOVE888:       ")
        list_of_text.append("       '! HERE272'       `& .NOW. !'       ")
        list_of_text.append("          '8Y  `Y         Y'  Y8'          ")
        list_of_text.append("           Y                   Y           ")
        list_of_text.append("           !                   !           ")

        my_font = pygame.font.SysFont('Lucida Console', 20)

        for i in range(len(list_of_text)):
            txt = list_of_text[i]
            txt_surf = my_font.render(txt, True, (255,255,255))
            self.surf.blit(txt_surf, (0, i*20))

class Flamme(pygame.sprite.Sprite):
    def __init__(self,pos,size):
        super().__init__()  

        self.big_size = size

        tmp_surf = flamme_sheet.subsurface((0,0,500,630))
        self.surf = tmp_surf
        if self.big_size == 3 :
            self.surf = pygame.transform.scale(tmp_surf, (300, 378))
        elif self.big_size == 2 :
            self.surf = pygame.transform.scale(tmp_surf, (150, 189))
        else :
            self.surf = pygame.transform.scale(tmp_surf, (50, 63))

        self.rect = self.surf.get_rect(center = pos)

        self.index_frame = 0 #that keeps track on the current index of the image list.
        self.current_frame = 0 #that keeps track on the current time or current frame since last the index switched.
        self.animation_frames = 3 #that define how many seconds or frames should pass before switching image.


        tmp_mask = flamme_mask
        if self.big_size == 3 :
            tmp_mask = pygame.transform.scale(tmp_mask, (300, 378))
        elif self.big_size == 2 :
            tmp_mask = pygame.transform.scale(tmp_mask, (150, 189))
        else :
            tmp_mask = pygame.transform.scale(tmp_mask, (50, 63))

        self.mask = pygame.mask.from_surface(tmp_mask)

    def animate(self):
        tmp_surf = flamme_sheet.subsurface((500*self.index_frame,0,500,630))

        self.current_frame += 1
        if self.current_frame >= self.animation_frames:
            self.current_frame = 0
            self.index_frame += 1
            if self.index_frame >= 56 :
                self.index_frame = 0
        
        if self.big_size == 3 :
            self.surf = pygame.transform.scale(tmp_surf, (300, 378))
        elif self.big_size == 2 :
            self.surf = pygame.transform.scale(tmp_surf, (150, 189))
        else :
            self.surf = pygame.transform.scale(tmp_surf, (50, 63))

class Lampad(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()  

        self.surf = lampad
        self.mask = pygame.mask.from_surface(lampad_mask)
        self.rect = self.surf.get_rect(center = (WIDTH/2, HEIGHT/2))




class LampadHitBoxFlamme(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()  

        self.surf = lampad_hitbox_for_light
        self.mask = pygame.mask.from_surface(lampad_hitbox_for_light)
        self.rect = self.surf.get_rect(center = (WIDTH/2, HEIGHT/2))

class CandleHitbox(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()  

        self.surf = candle_hitbox
        self.mask = pygame.mask.from_surface(candle_hitbox)
        self.rect = self.surf.get_rect(center = (WIDTH/2, HEIGHT/2))


