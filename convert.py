#!/usr/bin/env python3
import os
import sys
import pygame

WORKSPACE = os.path.dirname(__file__)
OUTPUT = os.path.join(WORKSPACE, "result/")
print(WORKSPACE)

def main():
    block = int(input("block:"))
    file = input("path:")
    pygame.init()
    img = pygame.image.load(os.path.join(WORKSPACE, file + ".jpg"))
    width, height = img.get_size()
    result = pygame.Surface((width, height))
    img.lock()
    result.lock()
    for i in range(block):
        for x in range(width):
            for y in range(height // block):
                result.set_at((x, (height // block * i) + y), img.get_at((x, height // block * (block - 1 - i) + y)))
    pygame.image.save(result, os.path.join(OUTPUT, file + ".bmp"))

if __name__ == "__main__":
    main()
