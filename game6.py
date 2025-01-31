from Classiq6 import *

def display_elements(room,player,list_txt_sprite):
    #room
    room.display()

    if room.flamme1 :
        room.flamme1.display()
    if room.flamme2 :
        room.flamme2.display()

    if room.eye : 
        room.eye.display(player)

    #player
    player.display(room)
   
    #room front if necessary
    if player.pos.y <= room.rect.y + 660:
        screen.blit(room.front, (room.rect.x, room.rect.y))

    for txt_sprite in list_txt_sprite :
        txt_sprite.display()

def get_new_room_name(room_index):
    if room_index == 0 :
        return "underworld"
    elif room_index == -7 :
        return "underworld4"
    else :
        return "underworld3"
        
def start6():
    empty_sprite_group()

    going_crazy = False

    player = Player()
    player.pos.y += 110
    player.pos.x -= 500

    room = Room("underworld")
    AddInCollideGroup(room)

    new_room_name = ""

    room_index = 0
    list_of_rooms = {}
    list_of_rooms[room_index] = room

    list_txt = ["Why are u still running away ?","There is no escape","Only the void, everywhere","PLEASE, just stay here and die","Stop move","Stop FUCKIN move","STOP","There is no escape","STOP !!","There is no escape","Only the void","STOP !!!","PLEASE, just stay here and die","There is no escape","Only the void"]
    list_txt_sprite = []
    cpt_txt = 0



    state_game = 0

    while state_game == 0:

        for event in pygame.event.get():
            player.controls(event)

        player.update()

        if player.deathOrNot():
            state_game = -1

        if player.velocity > 1000 :
            state_game = 6

        if room.name == "underworld4" :
            going_crazy = True
            list_of_rooms[0] = list_of_rooms[-1]

        if player.pos.x > room.rect.right -20 :
            player.pos.x = room.rect.left +20
            room_index += 1
            new_room_name = get_new_room_name(room_index)
        elif player.pos.x < room.rect.left +20 :
            player.pos.x = room.rect.right -20
            room_index -= 1
            new_room_name = get_new_room_name(room_index)

        if room_index > 0 :
            room_index = 0   

        if new_room_name != "" :
            if going_crazy :

                txt_ = ""
                if cpt_txt < len(list_txt):
                    txt_ = list_txt[cpt_txt]
                else :
                    txt_ = list_txt[len(list_txt)-1]
                txt_sprite_ = Text(txt_,(255,255,255),20+cpt_txt,(random.randint(100,WIDTH-100),random.randint(100,HEIGHT-100)))
                list_txt_sprite.append(txt_sprite_)
                cpt_txt +=1

                player.velocity = 6*cpt_txt
             
            empty_sprite_group()
            if room_index not in list_of_rooms:
                room = Room(new_room_name)
                list_of_rooms[room_index] = room
            else :
                room = list_of_rooms[room_index]
            AddInCollideGroup(room)
            new_room_name = ""

        screen.fill(room.bg_color)

        display_elements(room,player,list_txt_sprite)

        pygame.display.update()
        FramePerSec.tick(FPS)

    return state_game



