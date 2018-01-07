class Map():
  def __init__(self):
    pass

class Tile():
  def __init__(self, gui, base, content=[], pathways=[None, None, None, None]): ## Pathways are done as [up, down, left, right]. Placeholder of None can be used
    self.base = base
    self.content = content
    self.pathways = pathways

  def render(self, x, y):
    gui.Image(base, x, y, 50, 50)
    for i in self.content:
      i.render(x, y)
