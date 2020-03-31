import random


class Creature:
    def __init__(self, pos, characteristics=None):
        self.x = pos[0]
        self.y = pos[1]
        characteristics = characteristics or {}

        self.max_step_size = characteristics.get("max_step_size", 1)

    def make_step(self, world_size):
        x = random.randint(-self.max_step_size, self.max_step_size) + self.x
        y = random.randint(-self.max_step_size, self.max_step_size) + self.y

        self.x = max(min(x, world_size), 0)
        self.y = max(min(y, world_size), 0)
        