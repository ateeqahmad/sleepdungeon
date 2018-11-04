from .enemy import Enemy
from .weapons import Bow
from ..base.game_constants import SpriteType
from .. import res
from ..base.game_constants import Facing
import pygame


class EnemyArcher(Enemy):
    __BASE_UP_SURFACE: pygame.Surface = None
    __BASE_DOWN_SURFACE: pygame.Surface = None
    __BASE_LEFT_SURFACE: pygame.Surface = None
    __BASE_RIGHT_SURFACE: pygame.Surface = None

    __SURFACE_UP: pygame.Surface = None
    __SURFACE_DOWN: pygame.Surface = None
    __SURFACE_LEFT: pygame.Surface = None
    __SURFACE_RIGHT: pygame.Surface = None

    _WIDTH = 1
    _HEIGHT = 1
    _ANIMATION_LENGTH = 4
    _MILISECONDS_PER_FRAME = 200
    _MOVE_COOLDOWN = 400

    def __init__(self):
        super().__init__([1, 1])

        self.animation_i = 0
        self.frame_cooldown = 0

        self.lifes = 2
        self.max_lifes = 2

        self.selected_weapon = Bow()
        self.weapon_list = [self.selected_weapon]

        self.target_distance = 3

    def _image(self) -> pygame.Surface:
        img = None
        if self.facing == Facing.FACING_UP:
            img = EnemyArcher.__SURFACE_UP
        elif self.facing == Facing.FACING_DOWN:
            img = EnemyArcher.__SURFACE_DOWN
        if self.facing == Facing.FACING_LEFT:
            img = EnemyArcher.__SURFACE_LEFT
        elif self.facing == Facing.FACING_RIGHT:
            img = EnemyArcher.__SURFACE_RIGHT

        return img.subsurface(
            pygame.Rect(
                self.tile_size * self.animation_i,
                0,
                self.tile_size,
                self.tile_size
            )
        )

    @property
    def sprite_type(self) -> SpriteType:
        return SpriteType.ENEMY

    @classmethod
    def update_render_context(cls, render_context):
        if not cls.__BASE_UP_SURFACE:
            cls.__BASE_UP_SURFACE = pygame.image.load(res.IMG_DIR + "player/bow/walk/up.png").convert_alpha()
            cls.__BASE_DOWN_SURFACE = pygame.image.load(res.IMG_DIR + "player/bow/walk/down.png").convert_alpha()
            cls.__BASE_LEFT_SURFACE = pygame.image.load(res.IMG_DIR + "player/bow/walk/left.png").convert_alpha()
            cls.__BASE_RIGHT_SURFACE = pygame.image.load(res.IMG_DIR + "player/bow/walk/right.png").convert_alpha()

        cls.__SURFACE_UP = pygame.transform.smoothscale(
            cls.__BASE_UP_SURFACE,
            (
                cls._WIDTH * cls.tile_size * cls._ANIMATION_LENGTH,
                cls._HEIGHT * cls.tile_size
            )
        )
        cls.__SURFACE_DOWN = pygame.transform.smoothscale(
            cls.__BASE_DOWN_SURFACE,
            (
                cls._WIDTH * cls.tile_size * cls._ANIMATION_LENGTH,
                cls._HEIGHT * cls.tile_size
            )
        )
        cls.__SURFACE_LEFT = pygame.transform.smoothscale(
            cls.__BASE_LEFT_SURFACE,
            (
                cls._WIDTH * cls.tile_size * cls._ANIMATION_LENGTH,
                cls._HEIGHT * cls.tile_size
            )
        )
        cls.__SURFACE_RIGHT = pygame.transform.smoothscale(
            cls.__BASE_RIGHT_SURFACE,
            (
                cls._WIDTH * cls.tile_size * cls._ANIMATION_LENGTH,
                cls._HEIGHT * cls.tile_size
            )
        )
