#Crie um programa que:
#Abra e reproduza o áudio de um arquivo MP3.

import pygame

pygame.init()

pygame.mixer.music.load('PalmTree.mp3')

pygame.mixer.music.play()

pygame.event.wait()
