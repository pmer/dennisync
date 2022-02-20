from random import randint


class CommonEntity:
    def __init__(self):
        self.id = randint(0, 2**30)


class Entity:
    def __init__(self, common):
        self.id = common.id
        self.timestamp = randint(0, 2**30)


class Actor:
    def __init__(self, entities):
        self.entities = entities


class Simulation:
    def __init__(self, n_commons, n_entities, n_actors):
        commons = [CommonEntity() for _ in range(n_commons)]

        self.actors = []
        for _ in range(n_actors):
            indicies = {randint(0, n_commons - 1) for _ in range(n_entities)}
            entities = [Entity(commons[i]) for i in indicies]

            a = Actor(entities)
            self.actors.append(a)

    def run(self):
        pass
