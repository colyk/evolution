import random
import colorsys
import math


class Creature:
    def __init__(self, pos, characteristics=None):
        self.x = pos[0]
        self.y = pos[1]
        self.step = 0
        characteristics = characteristics or {}

        self.max_step_size = characteristics.get("max_step_size", 1)
        self.steps_before_die = characteristics.get("steps_before_die", 1)

    def make_step(self, world):
        self.step += 1
        x = random.randint(-self.max_step_size, self.max_step_size) + self.x
        y = random.randint(-self.max_step_size, self.max_step_size) + self.y

        self.x = max(min(x, world.size), 0)
        self.y = max(min(y, world.size), 0)

    @property
    def color(self):
        hsl_red = 0
        hsl_green = 1 / 360 * 110
        state = self.steps_before_die - self.step
        hue = hsl_green * state / self.steps_before_die - hsl_red
        r, g, b = colorsys.hls_to_rgb(hue, 0.5, 1)
        r = math.floor(r * 255)
        g = math.floor(g * 255)
        b = math.floor(b * 255)
        return f"#{r:02x}{g:02x}{b:02x}"
