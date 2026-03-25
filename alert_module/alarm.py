import os
import platform
import pygame
import winsound


def play_alarm():
    pygame.mixer.init()
    pygame.mixer.music.load("alarm.mp3")
    pygame.mixer.music.play()

# def play_alarm():
#     if platform.system() == "Windows":
#         import winsound
#         winsound.Beep(1000, 1000)  # frequency, duration
#     else:
#         print("🔊 ALARM!")