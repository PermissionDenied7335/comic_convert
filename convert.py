#!/usr/bin/env python3
import pygame
import os
import sys

WORKSPACE = os.path.dirname(__file__)
OUTPUT = os.path.join(WORKSPACE, "result/")
AVAILABLE_FORMATS = {".png", ".jpg", ".jpeg", ".bmp"}

def main():
    pygame.init()
    for root, dirs, files in os.walk(WORKSPACE):
        if root != WORKSPACE:
            continue
        for file in files:
            if file[file.rfind("."):] in AVAILABLE_FORMATS:
                img = pygame.image.load(os.path.join(root, file))
                width, height = img.get_size()
                result = pygame.Surface((width, height))
                screen = pygame.display.set_mode((width, height))
                screen.blit(img, (0, 0))
                finished = False
                block_num = 0
                while not finished:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            exit(0)
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_1:
                                block_num = 1 * 2
                            elif event.key == pygame.K_2:
                                block_num = 2 * 2
                            elif event.key == pygame.K_3:
                                block_num = 3 * 2
                            elif event.key == pygame.K_4:
                                block_num = 4 * 2
                            elif event.key == pygame.K_5:
                                block_num = 5 * 2
                            elif event.key == pygame.K_6:
                                block_num = 6 * 2
                            elif event.key == pygame.K_7:
                                block_num = 7 * 2
                            elif event.key == pygame.K_8:
                                block_num = 8 * 2
                            elif event.key == pygame.K_9:
                                block_num = 9 * 2
                            elif event.key == pygame.K_0: #act as 10
                                block_num = 10 * 2
                            elif event.key == pygame.K_RETURN: #save the picture
                                pygame.image.save(result, os.path.join(OUTPUT, file[0:file.rfind(".")] + ".bmp"))
                                finished = True
                                continue
                            else:
                                continue
                            
                            if block_num == 0:
                                result.blit(img)
                            else:
                                copied_height = 0
                                block_height = height // block_num
                                while copied_height < height:

                                    #the last block of original image(first block of result image) may not exactly match the division
                                    if copied_height == 0:
                                        current_height = block_height + height % block_height
                                    else:
                                        current_height = block_height
                                    porter = pygame.Surface((width, current_height))
                                    area = pygame.Rect(0, height - copied_height - current_height, width, current_height)
                                    porter.blit(img, (0, 0), area)
                                    result.blit(porter, (0, copied_height))
                                    copied_height += current_height
                                    screen.blit(result, (0, 0))
                    pygame.display.update()

if __name__ == "__main__":
    main()
