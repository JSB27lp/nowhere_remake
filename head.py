from init import *

collide_sprite_group = pygame.sprite.Group()
enemies_sprite_group = pygame.sprite.Group()

def empty_sprite_group():
    collide_sprite_group.empty()
    enemies_sprite_group.empty()

def AddInCollideGroup(test_room):
    test_room.add(collide_sprite_group)

def areSpritesColliding(sprite1,sprite2):
    if sprite1 and sprite2 :
        hit = pygame.sprite.collide_mask(sprite1, sprite2)
        if hit :
            return True
        else :
            return False
    else :
        return False

class GameOver(pygame.sprite.Sprite):
    def __init__(self,txt,color,death = True):
        super().__init__()  

        my_font = pygame.font.SysFont('Lucida Console', 60)
        self.surf = my_font.render(txt, True, color)
        self.rect = self.surf.get_rect(center = (WIDTH/2, HEIGHT/2))

class Text(pygame.sprite.Sprite):
    def __init__(self,txt,color,size,pos, font = 'Lucida Console'):
        super().__init__()  

        my_font = pygame.font.SysFont(font, size)
        self.surf = my_font.render(txt, False, color)
        self.rect = self.surf.get_rect(center = pos)

    def display(self):
        screen.blit(self.surf, (self.rect.x, self.rect.y))

class AnimatedObject(pygame.sprite.Sprite):
    def __init__(self,name,frames,freq,pos):
        super().__init__()  

        self.sheet = pygame.image.load("assets/objects/"+name+".png").convert_alpha()

        self.w_frame = self.sheet.get_width() / frames
        self.h_frame = self.sheet.get_height()

        self.surf = self.sheet.subsurface((0,0,self.w_frame,self.h_frame))
        self.rect = self.surf.get_rect(center = pos)

        self.special_front_for_hype = color_cubebig_front
        self.hyped = False

        self.index_frame = 0 #that keeps track on the current index of the image list.
        self.current_frame = 0 #that keeps track on the current time or current frame since last the index switched.
        self.animation_frames = freq #that define how many seconds or frames should pass before switching image.

        self.frames_number = frames

        self.mask = pygame.mask.from_surface(self.surf)

    def animate(self):
        self.surf = self.sheet.subsurface((self.w_frame*self.index_frame,0,self.w_frame,self.h_frame))

        self.current_frame += 1
        if self.current_frame >= self.animation_frames:
            self.current_frame = 0
            self.index_frame += 1
            if self.index_frame >= self.frames_number :
                self.index_frame = 0

    def display(self,animation=True):
        if animation :
            self.animate()
        screen.blit(self.surf, (self.rect.x, self.rect.y))

class CharacterSound():
    def __init__(self):
        self.freq = 15
        self.frame_cpt = 0

    def playSound(self):
        if self.vel != vec(0,0):
            self.frame_cpt += 1
            if self.frame_cpt == self.freq :
                pygame.mixer.Sound.play(footstep_sound)
                self.frame_cpt = 0

class Music():
    def __init__(self):
        pygame.mixer.music.load("assets/sounds/soundtracks/ambiance.wav")
        pygame.mixer.music.play(-1,0.0, 1000)

        self.music_name = "ambiance"

    
    def update2(self,player,room):

        if room.name == "blood_room":
            if self.music_name != "blood_room":
                self.music_name = "blood_room"
                pygame.mixer.music.unload()
                pygame.mixer.music.load("assets/sounds/soundtracks/bonhome_rouge.wav")
                pygame.mixer.music.play(-1,0.0, 1000)
        
        else :

            if self.music_name != "ambiance2_":
                self.music_name = "ambiance2_"
                pygame.mixer.music.unload()
                pygame.mixer.music.load("assets/sounds/soundtracks/ambiance2_.wav")
                pygame.mixer.music.play(-1,0.0, 1000)

    def update(self,player,room):

        if room.name == "test_room5":

            if player.pos.y > room.rect.bottom - 60 :
                if not pygame.mixer.music.get_busy():
                    pygame.mixer.music.load("assets/sounds/soundtracks/Papillon.wav")
                    pygame.mixer.music.play(-1,0.0, 1000)
            else :
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.fadeout(1000)

        elif room.name == "blood_room":
            if self.music_name != "blood_room":
                self.music_name = "blood_room"
                pygame.mixer.music.unload()
                pygame.mixer.music.load("assets/sounds/soundtracks/bonhome_rouge.wav")
                pygame.mixer.music.play(-1,0.0, 1000)

        elif room.name == "hp_room" or room.name == "3doors":
            if self.music_name != "hp":
                self.music_name = "hp"
                pygame.mixer.music.unload()
                pygame.mixer.music.load("assets/sounds/soundtracks/hp.wav")
                pygame.mixer.music.play(-1,0.0, 1000)

        elif hasattr(room, 'color_cube'):

            if room.color_cube and not room.color_cube.hyped:
                if self.music_name != "cube":
                    self.music_name = "cube"
                    pygame.mixer.music.unload()
                    pygame.mixer.music.load("assets/sounds/soundtracks/cube.wav")
                    pygame.mixer.music.play(-1,0.0, 1000)

            elif room.color_cube and room.color_cube.hyped:
                if self.music_name != "open_cube":
                    self.music_name = "open_cube"
                    pygame.mixer.music.unload()
                    pygame.mixer.music.load("assets/sounds/soundtracks/open_cube.wav")
                    pygame.mixer.music.play(-1,0.0, 1000)



        else :
            if self.music_name != "ambiance":
                self.music_name = "ambiance"
                pygame.mixer.music.unload()
                pygame.mixer.music.load("assets/sounds/soundtracks/ambiance.wav")
                pygame.mixer.music.play(-1,0.0, 1000)

music = Music()

