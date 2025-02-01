from Classiq5 import *

def display_elements(test_room,player,player2,pris_dans_le_sang_mouvant):
    #room
    screen.blit(test_room.surf, (test_room.rect.x, test_room.rect.y))
    #room number if necessary
    if test_room.room_number :
        screen.blit(test_room.room_number.surf, (test_room.room_number.rect.x, test_room.room_number.rect.y))
    #Butterfly
    if test_room.butterfly :
        screen.blit(test_room.butterfly.surf, (test_room.butterfly.rect.x, test_room.butterfly.rect.y))
    #lampad if necessary
    if test_room.lampad :
        screen.blit(test_room.lampad.surf, (test_room.lampad.rect.x, test_room.lampad.rect.y))
    #color cube if necessary
    if test_room.color_cube :
        screen.blit(test_room.color_cube.surf, (test_room.color_cube.rect.x, test_room.color_cube.rect.y))
    #color losange if necessary
    if test_room.color_losange :
        screen.blit(test_room.color_losange.surf, (test_room.color_losange.rect.x, test_room.color_losange.rect.y))
    #players
    screen.blit(player.surf, (player.rect.x, player.rect.y))
    if player2 :
        screen.blit(player2.surf, (player2.rect.x, player2.rect.y))








    if pris_dans_le_sang_mouvant :
        screen.blit(blood_room_jail2_flask, (test_room.rect.x, test_room.rect.y))


    #lampad front if necessary
    if test_room.lampad and player.pos.y < test_room.rect.y + 629:
        screen.blit(test_room.lampad.surf, (test_room.lampad.rect.x, test_room.lampad.rect.y))
    #flamme Player if necessary
    if player.flamme :
        screen.blit(player.flamme.surf, (player.flamme.rect.x, player.flamme.rect.y))
    #color cube front if necessary
    if test_room.color_cube :
        if test_room.color_cube.hyped :
            if player.pos.y < test_room.color_cube.rect.y + 315 :
                screen.blit(test_room.color_cube.surf, (test_room.color_cube.rect.x, test_room.color_cube.rect.y))
            elif player.pos.y < test_room.color_cube.rect.y + 424 :
                screen.blit(test_room.color_cube.special_front_for_hype, (test_room.color_cube.rect.x, test_room.color_cube.rect.y))
        else :
            if player.pos.y < test_room.color_cube.rect.y + 369 :
                screen.blit(test_room.color_cube.surf, (test_room.color_cube.rect.x, test_room.color_cube.rect.y))
    #room front if necessary
    if player.pos.y <= test_room.rect.y + 640:
        screen.blit(test_room.front, (test_room.rect.x, test_room.rect.y))
    #room again if necessary
    if test_room.name == "test_room4" and player.pos.y < test_room.rect.y + 427:
        screen.blit(test_room.surf, (test_room.rect.x, test_room.rect.y))
    #enemy if necessary
    for enemy in enemies_sprite_group:
        screen.blit(enemy.surf, (enemy.rect.x, enemy.rect.y))
    #flamme if necessary
    if test_room.flamme :
        screen.blit(test_room.flamme.surf, (test_room.flamme.rect.x, test_room.flamme.rect.y))








def get_new_room_name(room_index,actually_room_name):
    nb_room = 6
    room = room_index
    if room <  0 :
        room = room * -1

    if room%nb_room == 0:
        if actually_room_name == "blood_room" or actually_room_name == "blood_room_jail2" :
            return "blood_room_jail2"
        else :
            return "test_room" + str(0)
    else :
        if actually_room_name == "blood_room" or actually_room_name == "blood_room_jail2" :
            return "blood_room"
        else :
            return "test_room" + str(random.randint(1,nb_room-1))
    
def add_sprite_collision(test_room):
    test_room.add(collide_sprite_group)
    if test_room.color_cube :
            test_room.color_cube.add(collide_sprite_group)
    if test_room.lampad :
            test_room.lampad.add(collide_sprite_group)

def start5():
    empty_sprite_group()

    player = Player()


    room_index = 0#0

    test_room = Room("test_room0",room_index)
    add_sprite_collision(test_room)

    in_back_room_n_outside_checkpoint = False
    in_test_room0_n_outside_checkpoint = False

    new_room_name = ""

    list_of_rooms = {}
    list_of_rooms[room_index] = test_room

    room_index_first_hyped_cube = 0

    last_scene = False
    frame_cpt = 0

    state_game = 0

    
    player2 = Player()
    player2.pos.y += 120
    player2.pos.x = test_room.rect.right - 30


    pris_dans_le_sang_mouvant = False

    while state_game == 0:
        music.update(player,test_room)

        if player2 :

            if player2.pos.x > test_room.rect.x + 1492 - 29 - 4:
                player2.pos.x = test_room.rect.x + 30
            elif player2.pos.x < test_room.rect.x + 30:
                player2.pos.x = test_room.rect.x + 1492 - 29 - 4



        if player.pos.x < test_room.rect.x + 406 and player.pos.y < test_room.rect.y + 460 and test_room.name =="blood_room_jail2" :
            pris_dans_le_sang_mouvant = True

        if pris_dans_le_sang_mouvant :
            player.pos.y += 0.3

        if player.pos.y > test_room.rect.y + 620 and pris_dans_le_sang_mouvant:
            state_game = 5




        if player.amIdead():
            if last_scene:
                state_game = 1
            else :
                state_game = -1

        for event in pygame.event.get():
            player.controls(event)
        player.move()
        if player2 :
            player2.vel = vec(-1,0)
            player2.move()



        frame_cpt += 1
        #last_scene
        if not last_scene :
            last_scene = test_room.light_me(player)
            if last_scene :
                player.flamme = None

                bot1 = Bot(test_room)
                bot1.pos.x = test_room.rect.x + 153
                bot1.pos.y = test_room.rect.y + 580
                bot1.add(enemies_sprite_group)

                bot2 = Bot(test_room)
                bot2.add(enemies_sprite_group)
                bot2.pos.x = test_room.rect.x + 1335
                bot2.pos.y = test_room.rect.y + 580
        elif frame_cpt%60 == 0:
                bot1 = Bot(test_room)
                bot1.pos.x = test_room.rect.x + 153
                bot1.pos.y = test_room.rect.y + 580
                bot1.add(enemies_sprite_group)

                bot2 = Bot(test_room)
                bot2.add(enemies_sprite_group)
                bot2.pos.x = test_room.rect.x + 1335
                bot2.pos.y = test_room.rect.y + 580



        for enemy in enemies_sprite_group:
            enemy.path_finding(player.pos.x, player.pos.y)
            enemy.move()

        test_room.animation(player)

        screen.fill(test_room.bg_color)
        display_elements(test_room,player,player2,pris_dans_le_sang_mouvant)


        if not player.checkSpriteExistsnCollision(test_room.check_point_back_room):
            if test_room.name == "back_room" :
                in_back_room_n_outside_checkpoint = True
            elif test_room.name == "test_room0" :
                in_test_room0_n_outside_checkpoint = True


        if test_room.name == "back_room" :
            if room_index_first_hyped_cube == 0 :
                room_index_first_hyped_cube = room_index

            if player.pos.x > test_room.rect.x+1270:
                if room_index == room_index_first_hyped_cube :
                    new_room_name = "antichamber"
                else :
                    new_room_name = "antichamber2"
                player.pos.x = 395 + test_room.rect.x
                player.pos.y = 595 + test_room.rect.y
            if player.checkSpriteExistsnCollision(test_room.check_point_back_room) and in_back_room_n_outside_checkpoint:
                new_room_name = "test_room0"
                in_back_room_n_outside_checkpoint = False
        else :
            if (test_room.name == "antichamber" or test_room.name == "antichamber2") and player.pos.x < 395 + test_room.rect.x :
                new_room_name = "back_room"
                player.pos = (test_room.rect.x+1264, test_room.rect.y+280)
            elif player.checkSpriteExistsnCollision(test_room.check_point_back_room) and in_test_room0_n_outside_checkpoint:
                new_room_name = "back_room"
                in_test_room0_n_outside_checkpoint = False
            elif test_room.name == "test_room4" and player.pos.y < test_room.rect.y + 400:
                new_room_name = "blood_room"
                player.pos.y = test_room.rect.bottom
            elif test_room.name == "blood_room" and player.pos.y > test_room.rect.bottom :
                new_room_name = "test_room4"
                player.pos.y = test_room.rect.y + 400
            elif player.pos.x > test_room.rect.x + 1492 - 29 - 4:
                player.pos.x = test_room.rect.x + 30
                room_index += 1
                new_room_name = get_new_room_name(room_index,test_room.name)
            elif player.pos.x < test_room.rect.x + 30:
                player.pos.x = test_room.rect.x + 1492 - 29 - 4
                room_index -= 1
                new_room_name = get_new_room_name(room_index,test_room.name)


        if new_room_name != "" :
            empty_sprite_group()

            if new_room_name == "test_room0" :
                if room_index not in list_of_rooms:
                    test_room = Room(new_room_name,room_index)
                    list_of_rooms[room_index] = test_room
                else :
                    test_room = list_of_rooms[room_index]
            else :
                test_room = Room(new_room_name,room_index)
    
            add_sprite_collision(test_room)

            if test_room.name =="test_room4" :
                bot = Bot(test_room)
                bot.add(enemies_sprite_group)
            elif test_room.name =="blood_room":
                for i in range(6):
                    bot = Bot(test_room)
                    bot.add(enemies_sprite_group)

            if test_room.name =="blood_room" or test_room.name =="blood_room_jail2" :
                player2 = None
                
            new_room_name = ""


        pygame.display.update()
        FramePerSec.tick(FPS)

    return state_game



