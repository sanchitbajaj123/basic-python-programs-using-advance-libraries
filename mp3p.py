import pygame

# Initialize Pygame
pygame.init()

# Load the OGG file
ogg_file = "sahil.mp3"
pygame.mixer.music.load(ogg_file)

# Play the audio
pygame.mixer.music.play()



