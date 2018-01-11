import sys
from title import Title
import pygame
import random
from map import Map

class TitleScreen(Title):

  def click(self, action):
    if action == ('mouse0', 'down'):
      if 40 < self.cursor_x < 140 and 65 < self.cursor_y < 90: # START button
        self.gui.render_sequence = [Reset(self.gui, self.images), Map(self.gui, self.images)]

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


class DebugOut(Title):

  def post_init(self):
    self.content = ['debug mode enabled']

  def put(self, msg):
    self.content.insert(0, str(msg))
    print(msg)

  def render(self):

    for c in range(len(self.content)):
      if c > 15:
        self.content.pop(c)
        continue


      self.gui.Color('000000')
      self.gui.Rect(0, self.gui.height - (12 * (c + 1)), self.gui.width, 12)

      self.gui.Color('FFFFFF')
      self.gui.Text(self.content[c], 12)
      self.gui.showText(0, self.gui.height - (12 * (c + 1)))


class Reset(Title):

  def render(self):
    self.gui.Color('000000')
    self.gui.Rect(0, 0, self.gui.width, self.gui.height)
