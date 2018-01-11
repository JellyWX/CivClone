from title import Title
import random
import pygame
import time

class Map(Title):
  def post_init(self, width=5, height=5):
    self.map = []
    for i in range(height):
      temp = []
      for j in range(width):
        temp.append(Tile(self.gui, self.images['sea_anim'], vary=False))
      self.map.append(temp)

    self.scale = 1

  def scroll(self, direction):
    if direction == 'up' and self.scale > 0.06:
      self.scale -= 0.04
    elif direction == 'down':
      self.scale += 0.04

  def render(self):
    current_tile = 0
    current_row = 0
    invert = 0

    tw = 120 * self.scale
    th = 80 * self.scale

    outline = 2 * self.scale

    if outline < 1:
      outline = 1

    for row in self.map:
      for tile in row:
        tile.render(current_tile, current_row, tw, th, outline, invert)

        current_tile += 1

      invert += 1
      current_row += 1
      current_tile = 0

class Tile():
  def __init__(self, gui, base, content=[], vary=False): ## Pathways are done as [up, down, left, right]. Placeholder of None can be used
    self.gui = gui
    self.base = base
    self.content = content
    self.animated = False
    if vary:
      self.rotation = random.choice([45, -45, 135, -135])
    else:
      self.rotation = 45

    if self.base.get_height() > self.base.get_width() and (self.base.get_height() / self.base.get_width()) % 1 == 0.0:
      if 'loading animated tile' not in self.gui.debug.content:
        self.gui.debug.put('loading animated tile')
      self.frame = 0
      self.animated = True
      self.last_interval = time.time()
      self.max_frame = int(self.base.get_height() / self.base.get_width())

      self.frames = []
      for i in range(self.max_frame):
        self.frames.append(self.base.subsurface(pygame.Rect((0, self.base.get_width() * i), (self.base.get_width(), self.base.get_width()))))

  def render(self, x, y, tw, th, outline, invert):
    if self.animated and time.time() - self.last_interval > 0.5:
      self.frame += 1
      if self.frame >= self.max_frame:
        self.frame = 0

      self.last_interval = time.time()

    if self.animated:
      self.gui.Image(
        pygame.transform.rotate(
          self.frames[self.frame],
          self.rotation
        ),
        x * tw + (tw/2 * (invert % 2)),
        y * th/2,
        tw,
        th
        )

    else:
      self.gui.Image(
        pygame.transform.rotate(
          self.base,
          self.rotation
        ),
        x * tw + (tw/2 * (invert % 2)),
        y * th/2,
        tw,
        th
        )

    self.gui.Color(pygame.transform.average_color(self.base))
    self.gui.Line(
      [x * tw + (tw/2 * (invert % 2)) + tw/2, y * th/2],
      [(x + 1) * tw + (tw/2 * (invert % 2)), (y + 1) * th/2],
      width=outline
    )
    self.gui.Line(
      [(x + 1) * tw + (tw/2 * (invert % 2)), (y + 1) * th/2],
      [x * tw + (tw/2 * (invert % 2)) + tw/2, (y + 2) * th/2],
      width=outline
    )
    self.gui.Line(
      [x * tw + (tw/2 * (invert % 2)) + tw/2, (y + 2) * th/2],
      [x * tw + (tw/2 * (invert % 2)), (y + 1) * th/2],
      width=outline
    )
    self.gui.Line(
      [x * tw + (tw/2 * (invert % 2)), (y + 1) * th/2],
      [x * tw + (tw/2 * (invert % 2)) + tw/2, y * th/2],
      width=outline
    )

    for i in self.content:
      i.render(x, y)
