from ClassiqDefault import *

def display_elements(room,player,list_bot):
    #room
    room.display()

    #player
    player.display(room)
   
    #room front if necessary
    if player.pos.y <= room.rect.y + 640:
        screen.blit(room.front, (room.rect.x, room.rect.y))

    for bot in list_bot:
        bot.display(room)

def get_new_room_name(room_index):
    return "hp_room"
    
def start2():
    empty_sprite_group()

    player = Player()

    room = Room("hp_room")
    AddInCollideGroup(room)

    new_room_name = ""

    list_bot = []
    for i in range(4):
        bot = Bot(room)
        list_bot.append(bot)

    room_index = 0
    list_of_rooms = {}
    list_of_rooms[room_index] = room

    frame_count = 0

    state_game = 0

    while state_game == 0:

        music.update(player,room)

        for event in pygame.event.get():
            player.controls(event)

        player.update()

        if player.deathOrNot():
            state_game = -1

        for bot in list_bot:
            if frame_count%10==0:
                bot.move(room)
            bot.update()

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

        display_elements(room,player,list_bot)

        pygame.display.update()
        FramePerSec.tick(FPS)

        frame_count += 1

    return state_game



