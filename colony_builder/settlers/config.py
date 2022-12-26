import os

import pygame.image

import colony_builder
from colony_builder.engine.components.sprite import Sprite

WINDOW_SIZE = (640, 480)

SPRITE_SIZE = 16

res_path = os.path.dirname(colony_builder.settlers.__file__) + "/res"
GRASS_SURFACE = pygame.image.load(res_path + "/grass.png")
CASTLE_SURFACE = pygame.image.load(res_path + "/castle.png")
FLAG_SURFACE = pygame.image.load(res_path + "/flag.png")

GROUND_ENTITIES = [
    Sprite(GRASS_SURFACE, (x, y), 0)
    for y in range(0, WINDOW_SIZE[1], SPRITE_SIZE)
    for x in range(0, WINDOW_SIZE[0], SPRITE_SIZE)
]
CASTLE_ENTITY = Sprite(CASTLE_SURFACE, (640 // 16 * 8, 480 // 16 * 8), 1)
