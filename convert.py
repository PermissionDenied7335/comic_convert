#!/usr/bin/env python3
import os
import sys
import pygame

WORKSPACE = os.path.dirname(__file__)
OUTPUT = os.path.join(WORKSPACE, "result/")
print(WORKSPACE)

def main():
    file = input("path:")
    pygame.init()
    img = pygame.image.load(os.path.join(WORKSPACE, file + ".jpg"))
    width, height = img.get_size()
    result = pygame.Surface((width, height))
    img.lock()
    result.lock()
    for i in range(10):
        for x in range(width):
            for y in range(height // 10):
                result.set_at((x, (height // 10 * i) + y), img.get_at((x, height // 10 * (10 - 1 - i) + y)))
    pygame.image.save(result, os.path.join(OUTPUT, file + ".bmp"))

if __name__ == "__main__":
    main()
