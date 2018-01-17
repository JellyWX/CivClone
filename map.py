from title import Title
import random
import pygame
import time

class Map(Title):
  def post_init(self, width=20, height=50):
    self.width = width
    self.height = height

    self.dragging = False
    self.delta = [0, 0]
    self.drag_pos = (0, 0)

    self.map = [[]]
    for i in range(height):
      temp = [Tile(self.gui, self.images['sea_anim'])]
      for j in range(width):
        temp.append(Tile(self.gui, self.images['grass'], vary=True))
      self.map.append(temp)

    self.scale = 1

  def scroll(self, direction):
    if direction == 'up' and self.scale > 0.2:
      self.scale -= 0.04
    elif direction == 'down':
      self.scale += 0.04

  def click(self, action):
    if action == ('mouse0', 'down'):
      self.dragging = True
      self.drag_pos = self.cursor_x, self.cursor_y
    elif action == ('mouse0', 'up'):
      self.dragging = False

  def render(self):
    if self.dragging:
      self.delta[0] += self.drag_pos[0] - self.cursor_x
      self.delta[1] += self.drag_pos[1] - self.cursor_y

      self.drag_pos = self.cursor_x, self.cursor_y

    tw = 120 * self.scale
    th = 80 * self.scale

    outline = 2 * self.scale

    if outline < 1:
      outline = 1

    top = self.delta[1]
    bottom = top + self.gui.height
    left = self.delta[0]
    right = left + self.gui.width

    high_row = (top // (th/2)) - 1
    low_row = (bottom // (th/2)) + 1

    left_col = left // (tw/2) - 1
    right_col = right // (tw/2) + 1

    high_row, low_row, left_col, right_col = map(int, (high_row, low_row, left_col, right_col))

    if high_row < 0:
      high_row = 0
    if low_row >= self.height:
      low_row = self.height - 1

    if right_col >= self.width:
      right_col %= self.width

    print(left_col, right_col)

    current_tile = left_col
    current_row = high_row
    invert = high_row % 2

    for row in self.map[high_row:low_row]:
      for tile in row[left_col:right_col]:
        if (tw * current_tile) - self.delta[0] < self.gui.width and 0 < tw * (current_tile + 2) - self.delta[0]:
          tile.render(current_tile * tw - self.delta[0], current_row * th/2 - self.delta[1], tw, th, outline, invert)

        current_tile += 1

      invert += 1
      current_row += 1
      current_tile = 0


class Tile():
  last_interval = time.time()
  frame = 0

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
      self.animated = True
      self.max_frame = int(self.base.get_height() / self.base.get_width())

      self.frames = []
      for i in range(self.max_frame):
        self.frames.append(self.base.subsurface(pygame.Rect((0, self.base.get_width() * i), (self.base.get_width(), self.base.get_width()))))

  def render(self, x, y, tw, th, outline, invert):
    if self.animated:
      if time.time() - Tile.last_interval > 0.8:
        Tile.frame += 1
        Tile.last_interval = time.time()

      self.gui.Image(
        pygame.transform.rotate(
          self.frames[Tile.frame % self.max_frame],
          self.rotation
        ),
        x + (tw/2 * (invert % 2)),
        y,
        tw,
        th
        )

    else:
      self.gui.Image(
        pygame.transform.rotate(
          self.base,
          self.rotation
        ),
        x + (tw/2 * (invert % 2)),
        y,
        tw,
        th
        )

    self.gui.Color(pygame.transform.average_color(self.base))
    self.gui.Line(
      [x + (tw/2 * (invert % 2)) + tw/2, y],
      [(x + tw) + (tw/2 * (invert % 2)), y + th/2],
      width=outline
    )
    self.gui.Line(
      [(x + tw) + (tw/2 * (invert % 2)), y + th/2],
      [x + (tw/2 * (invert % 2)) + tw/2, y + th],
      width=outline
    )
    self.gui.Line(
      [x + (tw/2 * (invert % 2)) + tw/2, y + th],
      [x + (tw/2 * (invert % 2)), y + th/2],
      width=outline
    )
    self.gui.Line(
      [x + (tw/2 * (invert % 2)), y + th/2],
      [x + (tw/2 * (invert % 2)) + tw/2, y],
      width=outline
    )

    for i in self.content:
      i.render(x, y)
