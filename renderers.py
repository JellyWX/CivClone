import sys
from title import Title
import pygame
import random

class TitleScreen(Title):

  def click(self, action):
    if action == ('mouse0', 'down'):
      if 40 < self.cursor_x < 140 and 65 < self.cursor_y < 90: # START button
        self.gui.render_sequence = [Reset(self.gui, self.images), GameOverlay(self.gui, self.images, 'grass')]

      if 40 < self.cursor_x < 140 and 100 < self.cursor_y < 125: # EXIT button
        sys.exit()

  def render(self):
    # process rendering here

    self.gui.Color('FFFFFF')
    self.gui.Text('Civ Clone', 48)
    self.gui.showText(0, 0)

    # START button #
    if 40 < self.cursor_x < 140 and 65 < self.cursor_y < 90:
      self.gui.Color('CCCCCC')

    self.gui.Rect(40, 65, 100, 25)

    self.gui.Color('000000')
    self.gui.Text('START', 22)
    self.gui.showText(55, 65)
    # END #

    # EXIT button #
    self.gui.Color('FFFFFF')

    if 40 < self.cursor_x < 140 and 100 < self.cursor_y < 125:
      self.gui.Color('CCCCCC')

    self.gui.Rect(40, 100, 100, 25)

    self.gui.Color('000000')
    self.gui.Text('EXIT', 22)
    self.gui.showText(62, 100)
    # END #


class GameOverlay(Title):

  def post_init(self, img):
    self.img = img

  def click(self, action):
    pass

  def render(self):
    # process rendering here

    self.gui.Color('FFFFFF')
    self.gui.showText(0, 0)

    current_tile = 0
    current_row = 0
    invert = -1

    tw = 120
    th = 80

    for i in range(5):
      for j in range(5):
        self.gui.Image(
          pygame.transform.rotate(
            self.images[self.img],
            45
          ),
          20 + current_tile * tw + (tw / 4 * invert),
          20 + current_row * th/2,
          tw,
          th)

        current_tile += 1

      invert *= -1
      current_row += 1
      current_tile = 0


class Reset(Title):

  def render(self):
    self.gui.Color('000000')
    self.gui.Rect(0, 0, self.gui.width, self.gui.height)
