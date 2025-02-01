from Classiq3 import *
from maze import *

def display_elements(room,player,txt_A,txt_B):
    #room
    screen.blit(room.surf, (room.rect.x, room.rect.y))

    screen.blit(txt_A.surf, (txt_A.rect.x, txt_A.rect.y))
    screen.blit(txt_B.surf, (txt_B.rect.x, txt_B.rect.y))

    if room.front_door :
        room.front_door.display()
    if room.back_door :
        room.back_door.display()
    if room.right_door :
        room.right_door.display()
    if room.left_door :
        room.left_door.display()

    if room.rubikCube : 
        room.rubikCube.display(False)

    #player
    player.display()

    if player.rubikCube : 
        player.rubikCube.display(True)
   
    #room front if necessary
    if player.pos.y <= room.rect.y + 645:
        screen.blit(room.front, (room.rect.x, room.rect.y))

    for bot in room.list_bot:
        bot.display()
        if bot.rubikCube : 
            bot.rubikCube.display(True)

def get_new_room_name():
    return "3doors"

def getRoom(new_room_name,maze,room_index,room_z_index):
    room = Room(new_room_name)
    room.addBots()

    if maze[room_z_index+1][room_index] == 1 :
        room.front_door = Door("front_door")
    if maze[room_z_index-1][room_index] == 1 :
        room.back_door = Door("back_door")
    if maze[room_z_index][room_index+1] == 1 :
        room.right_door = Door("right_door")
    if maze[room_z_index][room_index-1] == 1 :
        room.left_door = Door("left_door")

    return room

def start3():

    maze = generate(8,5)

    '''for i in range(len(maze)) :
        print(maze[i])'''

    room_index = 1
    room_z_index = 1

    empty_sprite_group()

    player = Player()

    room = getRoom(get_new_room_name(),maze,room_index,room_z_index)

    AddInCollideGroup(room)
    if room.front_door :
        AddInCollideGroup(room.front_door)
    if room.back_door :
        AddInCollideGroup(room.back_door)
    if room.right_door :
        AddInCollideGroup(room.right_door)
    if room.left_door : 
        AddInCollideGroup(room.left_door)

    new_room_name = ""


    list_of_rooms = {}
    list_of_rooms["0;0"] = room

    txt_A = Text("0 0",(255,255,255),14,(room.rect.x+167,room.rect.y+450),"Times New Roman")
    txt_B = Text("1 0",(255,255,255),14,(room.rect.x+1320,room.rect.y+450),"Times New Roman")

    frame_count = 0

    state_game = 0

    while state_game == 0:

        music.update(player,room)

        for event in pygame.event.get():
            player.controls(event)

        player.update()

        if room.rubikCube :
            if not player.rubikCube :
                if areSpritesColliding(player,room.rubikCube) :
                        player.rubikCube = room.rubikCube
                        room.rubikCube = None

        for bot in room.list_bot:
            if areSpritesColliding(player,bot) :
                if player.rubikCube and not bot.rubikCube:
                    bot.rubikCube = player.rubikCube
                    player.rubikCube = None
                elif bot.rubikCube and not player.rubikCube:
                    player.rubikCube = bot.rubikCube
                    bot.rubikCube = None

        if player.deathOrNot():
            state_game = -1

        if room_z_index == len(maze)-2 and room_index == len(maze[0])-2 :
            state_game = 3

        for bot in room.list_bot:
            if frame_count%10==0:
                bot.move(room)
            bot.update()

        if player.pos.x > room.rect.x + 1492 - 24:
            player.pos.x = room.rect.x + 24
            room_index += 1
            new_room_name = get_new_room_name()
        elif player.pos.x < room.rect.x + 24:
            player.pos.x = room.rect.x + 1492 - 24
            room_index -= 1
            new_room_name = get_new_room_name()
        elif player.pos.y < room.rect.y + 390:
            player.pos.y = room.rect.y + 845
            room_z_index += 1
            new_room_name = get_new_room_name()
        elif player.pos.y > room.rect.y + 850:
            player.pos.y = room.rect.y + 390
            room_z_index -= 1
            new_room_name = get_new_room_name()

        if new_room_name != "" :
            empty_sprite_group()
            if str(room_index)+";"+str(room_z_index) not in list_of_rooms:
                room = getRoom(new_room_name,maze,room_index,room_z_index)
                list_of_rooms[str(room_index)+";"+str(room_z_index)] = room
            else :
                room = list_of_rooms[str(room_index)+";"+str(room_z_index)]

            AddInCollideGroup(room)
            if room.front_door :
                AddInCollideGroup(room.front_door)
            if room.back_door :
                AddInCollideGroup(room.back_door)
            if room.right_door :
                AddInCollideGroup(room.right_door)
            if room.left_door : 
                AddInCollideGroup(room.left_door)

            new_room_name = ""

            txt_A = Text(str(room_index)+" "+str(room_z_index),(255,255,255),14,(room.rect.x+167,room.rect.y+450),"Times New Roman")
            txt_B = Text(str(room_index+1)+" "+str(room_z_index),(255,255,255),14,(room.rect.x+1320,room.rect.y+450),"Times New Roman")

        screen.fill(room.bg_color)

        display_elements(room,player,txt_A,txt_B)

        pygame.display.update()
        FramePerSec.tick(FPS)

        frame_count += 1

    return state_game



