from title import Title
import pygame

class Map(Title):
  def post_init(self, width=5, height=5):
    self.map = [[Tile(self.gui, self.images['grass'])] * width] * height
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
  def __init__(self, gui, base, content=[], pathways=[None, None, None, None]): ## Pathways are done as [up, down, left, right]. Placeholder of None can be used
    self.gui = gui
    self.base = base
    self.content = content
    self.pathways = pathways

  def render(self, x, y, tw, th, outline, invert):

    self.gui.Image(
      pygame.transform.rotate(
        self.base,
        45
      ),
      x * tw + (tw/2 * (invert % 2)),
      y * th/2,
      tw,
      th)

    self.gui.Color('11AAFF')
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
