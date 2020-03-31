from creature import Creature
import numpy as np
import random


class Evolution:
    def __init__(self, world_size, population_size, creature_spec=None):
        self.step = 0
        self.world_size = world_size
        self.creature_spec = creature_spec or {}
        self.population_size = population_size
        self.creatures = self.create_creatures()

    def create_creatures(self):
        creatures = []
        for creature_id in range(self.population_size):
            pos = self._create_creature_pos()
            creature = Creature(pos, self.creature_spec)
            creatures.append(creature)

        return creatures

    def _create_creature_pos(self):
        x = random.triangular(0, self.world_size)
        y = random.triangular(0, self.world_size)
        return int(x), int(y)

    def make_step(self):
        print(self.step)
        self.step += 1
        for creature in self.creatures:
            creature.make_step(self.world_size)
