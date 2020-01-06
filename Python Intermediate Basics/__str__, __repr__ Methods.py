import datetime

# datetime.datetime.now()
#
# print(datetime.datetime.now())
#
# print(repr(datetime.datetime.now()))
#
# print(str(datetime.datetime.now()))


#Example
import pygame
import random
from blob import Blob
import numpy as np
import logging


class Blob:

    def __init__(self, color, x_boundary, y_boundary, size_range=(4, 8), movement_range=(-1, 2)):
        self.size = random.randrange(size_range[0], size_range[1])
        self.color = color
        self.x_boundary = x_boundary
        self.y_boundary = y_boundary
        self.x = random.randrange(0, self.x_boundary)
        self.y = random.randrange(0, self.y_boundary)
        self.movement_range = movement_range

    def __repr__(self):
        return 'Blob({}, {}, ({}, {}))'.format(self.color,
                                               self.size,
                                               self.x,
                                               self.y)

    def __str__(self):
        return 'Blob of color: {}, size: {}, location: ({}, {}))'.format(self.color,
                                                                         self.size,
                                                                         self.x,
                                                                         self.y)


    def move(self):
        self.move_x = random.randrange(self.movement_range[0], self.movement_range[1])
        self.move_y = random.randrange(self.movement_range[0], self.movement_range[1])
        self.x += self.move_x
        self.y += self.move_y

    def check_bounds(self):
        if self.x < 0:
            self.x = 0
        elif self.x > self.x_boundary:
            self.x = self.x_boundary

        if self.y < 0:
            self.y = 0
        elif self.y > self.y_boundary:
            self.y = self.y_boundary





'''
DEBUG   Detailed information, typically of interest only when diagnosing problems.
INFO    Confirmation that things are working as expected.
WARNING An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.
ERROR   Due to a more serious problem, the software has not been able to perform some function.
CRITICAL    A serious error, indicating that the program itself may be unable to continue running.
'''

logging.basicConfig(filename='logfile.log', level=logging.INFO)

STARTING_BLUE_BLOBS = 15
STARTING_RED_BLOBS = 15
STARTING_GREEN_BLOBS = 15

WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

game_display = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blob World")
clock = pygame.time.Clock()


class BlueBlob(Blob):

    def __init__(self, x_boundary, y_boundary):
        Blob.__init__(self, (0, 0, 255), x_boundary, y_boundary)

    def __add__(self, other_blob):
        logging.info('Blob add op {} + {}'.format(str(self.color), str(other_blob.color)))
        if other_blob.color == (255, 0, 0):
            self.size -= other_blob.size
            other_blob.size -= self.size
        elif other_blob.color == (0, 255, 0):
            self.size += other_blob.size
            other_blob.size = 0
        elif other_blob.color == (0, 0, 255):
            pass
        else:
            raise Exception('Tried to combine one or multiple blobs of unsupported colors.')


class RedBlob(Blob):

    def __init__(self, x_boundary, y_boundary):
        Blob.__init__(self, (255, 0, 0), x_boundary, y_boundary)


class GreenBlob(Blob):

    def __init__(self, x_boundary, y_boundary):
        Blob.__init__(self, (0, 255, 0), x_boundary, y_boundary)


def is_touching(b1, b2):
    return np.linalg.norm(np.array([b1.x, b1.y]) - np.array([b2.x, b2.y])) < (b1.size + b2.size)


def handle_collisions(blob_list):
    blues, reds, greens = blob_list
    for blue_id, blue_blob, in blues.copy().items():
        for other_blobs in blues, reds, greens:
            for other_blob_id, other_blob in other_blobs.copy().items():
                logging.debug(
                    'Checking if blobs are touching {} + {}'.format(str(blue_blob.color), str(other_blob.color)))
                if blue_blob == other_blob:
                    pass
                else:
                    if is_touching(blue_blob, other_blob):
                        blue_blob + other_blob
                        if other_blob.size <= 0:
                            del other_blobs[other_blob_id]
                        if blue_blob.size <= 0:
                            del blues[blue_id]

    return blues, reds, greens


def draw_environment(blob_list):
    blues, reds, greens = handle_collisions(blob_list)
    game_display.fill(WHITE)
    for blob_dict in blob_list:
        for blob_id in blob_dict:
            blob = blob_dict[blob_id]
            pygame.draw.circle(game_display, blob.color, [blob.x, blob.y], blob.size)
            blob.move()
            blob.check_bounds()

    pygame.display.update()
    return blues, reds, greens


def main():
    blue_blobs = dict(enumerate([BlueBlob(WIDTH, HEIGHT) for i in range(STARTING_BLUE_BLOBS)]))
    red_blobs = dict(enumerate([RedBlob(WIDTH, HEIGHT) for i in range(STARTING_RED_BLOBS)]))
    green_blobs = dict(enumerate([GreenBlob(WIDTH, HEIGHT) for i in range(STARTING_GREEN_BLOBS)]))

    while True:
        try:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

            blue_blobs, red_blobs, green_blobs = draw_environment([blue_blobs, red_blobs, green_blobs])
            clock.tick(60)
        except Exception as e:
            logging.critical(str(e))
            pygame.quit()
            quit()
            break


if __name__ == '__main__':
    blue_blobs = dict(enumerate([BlueBlob(WIDTH, HEIGHT) for i in range(STARTING_BLUE_BLOBS)]))
    red_blobs = dict(enumerate([RedBlob(WIDTH, HEIGHT) for i in range(STARTING_RED_BLOBS)]))
    green_blobs = dict(enumerate([GreenBlob(WIDTH, HEIGHT) for i in range(STARTING_GREEN_BLOBS)]))
#    main()