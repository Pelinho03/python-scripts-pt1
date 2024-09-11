'''
021. Fazer um programa em Python que abra e reproduza o áudio de um arquivo MP3.
'''
import pygame

pygame.mixer.init()  # Inicializa o mixer
pygame.mixer.music.load('feelings.mp3')  # Carrega o arquivo MP3
pygame.mixer.music.play()  # Reproduz o arquivo MP3

# Mantém o script a correr até que o áudio termine
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)  # Aguarda até que a reprodução termine
