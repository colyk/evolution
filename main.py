from world import World
from creature import Creature
from evolution import Evolution

import time

if __name__ == "__main__":
    size = 35
    population_size = 10
    evolution_steps = 20
    default_creatures_spec = {'max_step_size': 3}

    world = World(size)
    evolution = Evolution(size, population_size, default_creatures_spec)
    for step in range(evolution_steps):
        world.draw_world()
        world.draw_creatures(evolution.creatures)
        world.redraw()
        evolution.make_step()
        time.sleep(0.3)
