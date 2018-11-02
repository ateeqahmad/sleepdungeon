from typing import Tuple
from base import Context
from base.game_constants import SpriteType
import pygame


class Sprite:
    def __init__(self):
        self.position: Tuple[int, int] = (0, 0)
        self.image: pygame.image = None
        self.z_index: int = 0
        self.rect: pygame.rect = None
        self.type: SpriteType = None

    def update(self, context: Context):
        pass
