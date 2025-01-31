from game0 import *
from game import *
from game2 import *
from game3 import *
from game4 import *
from game5 import *
from game6 import *
from game7 import *

list_game_over = ["Think before","Fail better","Suicide is forbidden"]

def save(level):
    # Writing to an existing file (content will be overwritten)
    with open("save.txt", "w") as f:
        f.write(str(level*2777))

def getSave():
    f = open("save.txt","r")
    level = int(f.read())
    level = level/2777
    return level

def intro():
    while(start0()==-1):
        pass

def level1():
    save(1)
    while(start()==-1):
        screen.fill((0,0,0))
        number = random.randint(0,len(list_game_over)-1)
        game_over = GameOver(list_game_over[number],(255, 0, 0))
        screen.blit(game_over.surf, (game_over.rect.x, game_over.rect.y))
        pygame.display.update()
        pygame.time.wait(3000)

    screen.fill((0,0,0))
    game_over = GameOver("Death is a lie",(0, 0, 255))
    screen.blit(game_over.surf, (game_over.rect.x, game_over.rect.y))
    pygame.display.update()
    pygame.time.wait(5000)

def level2():
    save(2)
    while(start2()==-1):
        screen.fill((0,0,0))
        number = random.randint(0,len(list_game_over)-1)
        game_over = GameOver(list_game_over[number],(255, 0, 0))
        screen.blit(game_over.surf, (game_over.rect.x, game_over.rect.y))
        pygame.display.update()
        pygame.time.wait(3000)

    screen.fill((0,0,0))
    game_over = GameOver("Calm down Neo",(0, 255, 0),False)
    screen.blit(game_over.surf, (game_over.rect.x, game_over.rect.y))
    pygame.display.update()
    pygame.time.wait(5000)

def level3():
    save(3)
    while(start3()==-1):
        screen.fill((0,0,0))
        number = random.randint(0,len(list_game_over)-1)
        game_over = GameOver(list_game_over[number],(255, 0, 0))
        screen.blit(game_over.surf, (game_over.rect.x, game_over.rect.y))
        pygame.display.update()
        pygame.time.wait(3000)

    screen.fill((0,0,0))
    game_over = GameOver("Even a glob could do it",(255, 96, 0),False)
    screen.blit(game_over.surf, (game_over.rect.x, game_over.rect.y))
    pygame.display.update()
    pygame.time.wait(5000)

def level4():
    save(4)
    while(start4()==-1):
        pass

    screen.fill((0,0,0))
    number = random.randint(0,len(list_game_over)-1)
    game_over = GameOver(list_game_over[number],(255, 0, 0))
    screen.blit(game_over.surf, (game_over.rect.x, game_over.rect.y))
    pygame.display.update()
    pygame.time.wait(3000)

def level5():
    save(5)
    while(start5()==-1):
        screen.fill((0,0,0))
        number = random.randint(0,len(list_game_over)-1)
        game_over = GameOver(list_game_over[number],(255, 0, 0))
        screen.blit(game_over.surf, (game_over.rect.x, game_over.rect.y))
        pygame.display.update()
        pygame.time.wait(3000)

def level6():
    save(6)
    while(start6()==-1):
        screen.fill((0,0,0))
        number = random.randint(0,len(list_game_over)-1)
        game_over = GameOver(list_game_over[number],(255, 0, 0))
        screen.blit(game_over.surf, (game_over.rect.x, game_over.rect.y))
        pygame.display.update()
        pygame.time.wait(3000)

    screen.fill((255,255,255))
    pygame.display.update()
    pygame.time.wait(3000)

def level7():
    save(7)

    state_game = -1
    while(state_game==-1):
        state_game = start7()

    screen.fill((0,0,0))
    game_over = GameOver("A train could kill you, but here and now you are free",(255, 255, 255))
    screen.blit(game_over.surf, (game_over.rect.x, game_over.rect.y))
    pygame.display.update()
    pygame.time.wait(8000)

    screen.fill((0,0,0))
    game_over = GameOver("Congratulation",(255, 255, 255))
    screen.blit(game_over.surf, (game_over.rect.x, game_over.rect.y))
    pygame.display.update()
    pygame.time.wait(8000)

def nowhere(level):

    intro()

    if level == 1:
        level1()
        level2()
        level3()
        level4()
        level5()
        level6()
        level7()
    elif level == 2:
        level2()
        level3()
        level4()
        level5()
        level6()
        level7()
    elif level == 3:
        level3()
        level4()
        level5()
        level6()
        level7()
    elif level == 4:
        level4()
        level5()
        level6()
        level7()
    elif level == 5:
        level5()
        level6()
        level7()
    elif level == 6:
        level6()
        level7()
    elif level == 7:
        level7()

nowhere(getSave())