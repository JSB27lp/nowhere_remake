from Classiq0 import *

def start0():
    player = Player()

    glitch_list = []

    game_over = GameOver("Nowhere",(255, 255, 255))

    frame_count = 0

    while frame_count < 60*4:

        screen.fill((0,0,0))
        
        screen.blit(game_over.surf, (game_over.rect.x, game_over.rect.y))

        pygame.display.update()
        FramePerSec.tick(FPS)

        frame_count += 1

    frame_count = 0

    while frame_count < 60*10:

        if frame_count%6 == 0:
            glitch = AnimatedObject("glitchSheet",8,4,(random.randint(0,WIDTH),random.randint(0,HEIGHT)))
            glitch_list.append(glitch)

        screen.fill((0,0,0))

        screen.blit(game_over.surf, (game_over.rect.x, game_over.rect.y))

        if frame_count%10 == 0:
            for glitch in glitch_list :
                glitch.display(True)

        pygame.display.update()
        FramePerSec.tick(FPS)

        frame_count += 1



    frame_count = 0

    while frame_count < 60*5:

        for event in pygame.event.get():
            player.controls(event)
        player.update()


        screen.fill((0,0,0))

        for glitch in glitch_list :
            glitch.display(True)

        player.display()

        pygame.display.update()
        FramePerSec.tick(FPS)

        frame_count += 1


    return 0



