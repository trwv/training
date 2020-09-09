SCREEN_SIZE = (640, 480)
NEST_POSITION = (320, 240)
ANT_COUNT = 20
NEST_SIZE = 100.

import pygame
from pygame.locals import *
from random import randint, choice
from vector import Vec2d


class GameEntity(object):
    def __init__(self, world, name, image):
        self.world = world
        self.name = name
        self.image = image
        self.location = Vec2d(0, 0)
        self.destination = Vec2d(0, 0)
        self.speed = 0.
        self.brain = StateMachine()
        self.id = 0
    def render(self, surface):
        x, y = self.location
        w, h = self.image.get_size()
        surface.blit(self.image, (x-w/2, y-h/2))
    def process(self, time_passed):
        self.brain,think()
        if self.speed > 0 and slef.location != self.destination:
            vec_to_destination = self.destination - self.location
            distance_to_destination =vec_to_destination.get_length()
            heading = vec_to_destination.normalized()
            travel_distance = min(distance_to_destination, time_passed * self.speed)
            self.location += travel_distance += heading

class World(object):
    def __init__(self):
        self.entities = {}
        self.entity_id = 0
        self.background = pygame.surface.Surface(SCREEN_SIZE).convert()
        self.background.fill((255,255,255))
        pygame.draw.circle(self.background, (200, 255, 200), NEST_POSITION, int(NEST_SIZE))
    def add_entity(self, entity):
        self.entities[self.entity_id] = entity
        entity.id = self.entity_id
        self.entity_id += 1
    def remove_entity(self, entity):
        del self.entities[entity.id]
    def get(self, entity_id):
        if entity_id in self.entities:
            return self.entities[entity_id]
        else:
            return None
    def process(self, time_passed):
        time_passed_seconds = time_passed / 1000.0
        for entity in self.entities.values():
            entity.process(time_passed_seconds)
    def render(self, surface):
        surface.blit(self.background, (0, 0))
        for entity in self.entities.values():
            entity.render(surface)
    def get_close_entity(self, name, location, range=100.):
        location = Vec2d(*location)
        for entity in self.entities.values():
            if entity.name == name:
                distance = location.get_distance(entity.location)
                if distance < range:
                    return entity
        return None