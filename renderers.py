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
    self.scale = 1

  def scroll(self, direction):
    if direction == 'up' and self.scale > 0.06:
      self.scale -= 0.04
    elif direction == 'down':
      self.scale += 0.04

  def render(self):
    # process rendering here

    self.gui.Color('FFFFFF')
    self.gui.showText(0, 0)

    current_tile = 0
    current_row = 0
    invert = 0

    tw = 120 * self.scale
    th = 80 * self.scale

    outline = 2 * self.scale

    if outline < 1:
      outline = 1

    for i in range(5):
      for j in range(5):
        self.gui.Image(
          pygame.transform.rotate(
            self.images[self.img],
            45
          ),
          current_tile * tw + (tw/2 * (invert % 2)),
          current_row * th/2,
          tw,
          th)

        self.gui.Color('11AAFF')
        self.gui.Line(
          [current_tile * tw + (tw/2 * (invert % 2)) + tw/2, current_row * th/2],
          [(current_tile + 1) * tw + (tw/2 * (invert % 2)), (current_row + 1) * th/2],
          width=outline
        )
        self.gui.Line(
          [(current_tile + 1) * tw + (tw/2 * (invert % 2)), (current_row + 1) * th/2],
          [current_tile * tw + (tw/2 * (invert % 2)) + tw/2, (current_row + 2) * th/2],
          width=outline
        )
        self.gui.Line(
          [current_tile * tw + (tw/2 * (invert % 2)) + tw/2, (current_row + 2) * th/2],
          [current_tile * tw + (tw/2 * (invert % 2)), (current_row + 1) * th/2],
          width=outline
        )
        self.gui.Line(
          [current_tile * tw + (tw/2 * (invert % 2)), (current_row + 1) * th/2],
          [current_tile * tw + (tw/2 * (invert % 2)) + tw/2, current_row * th/2],
          width=outline
        )

        current_tile += 1

      invert += 1
      current_row += 1
      current_tile = 0


class Reset(Title):

  def render(self):
    self.gui.Color('000000')
    self.gui.Rect(0, 0, self.gui.width, self.gui.height)
