import pygame, config, sys, random

def init_game():
    pygame.init()
    pygame.mixer.init()
    pygame.font.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))
    pygame.display.set_caption(config.TITLE)
    return screen

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
    return True




def draw_text(screen, text, font, text_color, y):
    img = font.render(text, True, text_color)
    screen.blit(img, (90, y))

def main():
    screen = init_game()
    clock = pygame.time.Clock()
    music_active = False
    text_font = pygame.font.Font('Roboto.ttf', 30)
    text_color = (random.randrange(0, 254), random.randrange(0, 254), random.randrange(0, 254))
    instructions = ['Press "1" to play sound effect #1', 'Press "2" to play sound effect #2', 'Press "3" to play sound effect #3', 'Press "E" to begin/stop background music' ]
    sound1 = pygame.mixer.Sound('roblox-death-sound.ogg')
    sound2 = pygame.mixer.Sound('doom-death-sound-effect.ogg')
    sound3 = pygame.mixer.Sound('zap13.ogg')
    bg_music = pygame.mixer.music.load('Stay&Decay.ogg')

    
    base_y = 30
    line_height = 20

    running = True
    while running:
        running = handle_events()
        screen.fill(config.COLOR_DARKGRAY)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_1]:
            sound1.play()
        if keys[pygame.K_2]:
            sound2.play()
        if keys[pygame.K_3]:
            sound3.play()
        if keys[pygame.K_e]:
            pygame.mixer.music.play()
            print('play')
        if keys[pygame.K_r]:
            pygame.mixer.music.stop()
            print('stop')

        for i in range(len(instructions)):
            draw_text(screen, instructions[i], text_font, text_color, base_y + i * line_height)

        
        pygame.display.flip()

        clock.tick(config.FPS)

    pygame.quit()
    sys.exit()    


if __name__ == '__main__':
    main()