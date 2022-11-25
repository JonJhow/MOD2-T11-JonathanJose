from dino_runner.utils.constants import BLACK_HEART, BLACK_HEART_TYPE
from dino_runner.components.power_ups.power_up import PowerUp


class BlackHeart(PowerUp):
    def __init__(self):
        self.image = BLACK_HEART
        self.type = BLACK_HEART_TYPE
        self.duration = 8
        super().__init__(self.image, self.type, self.duration)