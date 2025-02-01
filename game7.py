from Classiq7 import *

def display_elements(room,player):
    #room
    room.display()

    #player
    player.display(room)
   
    #room front if necessary
    if player.pos.y <= room.rect.y + 640:
        screen.blit(room.front, (room.rect.x, room.rect.y))

def get_new_room_name(room_index):
    if room_index == 0 :
        return "underworld3_reverse"
    else :
        return "rail"
    
def start7():
    empty_sprite_group()

    player = Player()

    room = Room("underworld3_reverse")
    AddInCollideGroup(room)

    new_room_name = ""

    room_index = 0
    list_of_rooms = {}
    list_of_rooms[room_index] = room

    blk_trans = False  

    state_game = 0

    cpt_blk_trans = 0

    while state_game == 0:

        music.update(player,room)

        for event in pygame.event.get():
            if not blk_trans:
                player.controls(event)

        player.update()

        if player.deathOrNot():
            state_game = -1

        if room.name == "rail" and player.pos.y < room.rect.top + 50 :
            blk_trans = True    


        if player.pos.x > room.rect.right -20 :
            player.pos.x = room.rect.left +20
            room_index += 1
            new_room_name = get_new_room_name(room_index)
        elif player.pos.x < room.rect.left +20 :
            player.pos.x = room.rect.right -20
            room_index -= 1
            new_room_name = get_new_room_name(room_index)

        if new_room_name != "" :
            empty_sprite_group()
            if room_index not in list_of_rooms:
                room = Room(new_room_name)
                list_of_rooms[room_index] = room
            else :
                room = list_of_rooms[room_index]
            AddInCollideGroup(room)
            new_room_name = ""

        screen.fill(room.bg_color)
        if room.name == "rail" :
            screen.blit(room.bg_img, (0, 0))

        display_elements(room,player)

        if blk_trans :
            my_surface = pygame.Surface((WIDTH, HEIGHT))
            my_surface = my_surface.convert_alpha()
            my_surface.fill((0, 0, 0, cpt_blk_trans))
            screen.blit(my_surface,(0,0))

            if cpt_blk_trans < 255 :
                cpt_blk_trans +=1
            else : 
                state_game = 7

        pygame.display.update()
        FramePerSec.tick(FPS)

    return state_game



