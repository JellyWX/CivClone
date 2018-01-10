class Title():
  def __init__(self, gui, im, *args, **kwargs):
    ## rendering components ##
    self.gui = gui
    self.images = im

    ## metadata ##
    self.cursor_x = 0
    self.cursor_y = 0
    self.post_init(*args, **kwargs)

  def post_init(self):
    pass

  def setCursorPos(self, x, y):
    self.cursor_x = x
    self.cursor_y = y

  def key_hit(self, key_hit):
    pass

  def click(self, action):
    pass

  def render(self):
    pass
