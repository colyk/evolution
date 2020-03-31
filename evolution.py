from creature import Creature
import random


class Evolution:
    def __init__(self, world, population_size, creature_spec=None):
        self.step = 0
        self.world = world
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
        x = random.triangular(0, self.world.size)
        y = random.triangular(0, self.world.size)
        return int(x), int(y)

    def make_step(self):
        # print(self.step)
        self.step += 1
        self._filter_dead_creatures()
        for creature in self.creatures:
            creature.make_step(self.world)

    def _filter_dead_creatures(self):
        self.creatures = [
            creature
            for creature in self.creatures
            if creature.step < creature.steps_before_die
        ]
