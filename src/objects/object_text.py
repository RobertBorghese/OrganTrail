import pyglet

from objects.object_base import Object_Base

# ---------------------------------------------------------------
# * Object_Text
#
# A class used to create objects that show text.
# ---------------------------------------------------------------
class Object_Text(Object_Base):
	def __init__(self, text, font, size, x, y):
		super().__init__()
		self.obj = pyglet.text.Label(text, font_name=font, font_size=size, x=x, y=y, anchor_x='center', anchor_y='center')

# ---------------------------------------------------------------