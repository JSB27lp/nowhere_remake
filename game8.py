from ClassiqDefault import *

def display_elements(room,player):
    #room
    room.display()

    #player
    player.display(room)
   
    #room front if necessary
    if player.pos.y <= room.rect.y + 640:
        screen.blit(room.front, (room.rect.x, room.rect.y))


def get_new_room_name(room_index):
    
    return "hp_room"
    
def start8():
    empty_sprite_group()

    player = Player()


    room = Room("test_room_truth")
    AddInCollideGroup(room)

    new_room_name = ""

    player.pos.x = room.rect.x + 1059
    player.pos.y = room.rect.bottom - 10

    room_index = 0
    list_of_rooms = {}
    list_of_rooms[room_index] = room


    state_game = 0

    while state_game == 0:

        for event in pygame.event.get():
            player.controls(event)

        player.update()

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

        display_elements(room,player)

        pygame.display.update()
        FramePerSec.tick(FPS)


    return state_game



