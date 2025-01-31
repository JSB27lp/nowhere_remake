from head import *

class Character(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()  

        self.surf = character_standing_sheet_surf.subsurface((100*7,0,100,150))
        self.mask = pygame.mask.from_surface(character_mask)
        self.rect = self.surf.get_rect()
   
        self.pos = vec((WIDTH/2,HEIGHT/2))
        self.vel = vec(0,0)
        self.last_direction = ""

        self.frame_cpt = 0
        self.direction_cpt = 0

        self.velocity = 6#6

    def update(self):

        if self.frame_cpt%10 == 0 :

            self.direction_cpt += 1
            if self.direction_cpt == 8 :
                self.direction_cpt = 0

        self.frame_cpt += 1

        self.rect.midbottom = self.pos

    def display(self):
        self.animate()
        screen.blit(self.surf, (self.rect.x, self.rect.y))

    def animate(self):
        if self.direction_cpt == 0:
            self.surf = character_standing_sheet_surf.subsurface((100*7,0,100,150))
        elif self.direction_cpt == 1:
            self.surf = character_standing_sheet_surf.subsurface((100*6,0,100,150))
        elif self.direction_cpt == 2:
            self.surf = character_standing_sheet_surf.subsurface((100*5,0,100,150))
        elif self.direction_cpt == 3:
            self.surf = character_standing_sheet_surf.subsurface((100*4,0,100,150))
        elif self.direction_cpt == 4:
            self.surf = character_standing_sheet_surf.subsurface((100*3,0,100,150))
        elif self.direction_cpt == 5:
            self.surf = character_standing_sheet_surf.subsurface((100*2,0,100,150))
        elif self.direction_cpt == 6:
            self.surf = character_standing_sheet_surf.subsurface((100*1,0,100,150))
        elif self.direction_cpt == 7:
            self.surf = character_standing_sheet_surf.subsurface((100*0,0,100,150))

class Player(Character):
    def __init__(self):
        super().__init__()  

    def controls(self,event):

        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:  
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
