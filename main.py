import pygame, config, sys

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))
pygame.display.set_caption(config.TITLE)

def main():
    font_style = pygame.font.Font('config.FONT', 40)

    