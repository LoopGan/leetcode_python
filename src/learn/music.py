#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    @author: LoopGan
    @contact: ganwei4955@gamil.com
    @time: 8/24/2018 10:55 AM
"""
import pygame

file = 'C://CloudMusic//Jam - 七月上.mp3'
pygame.mixer.init()
print("Play music")
track = pygame.mixer.music.load(file)
pygame.mixer.music.play()

if __name__ == "__main__":
    print("hello imp")
