import pyglet

from objects.object_base import Object_Base

# ---------------------------------------------------------------
# * Object_Test
#
# Tests objects.
# ---------------------------------------------------------------
class Object_Test(Object_Base):
	def create(self):
		ball_image = pyglet.image.load('images/test.jpg')
		self.obj = pyglet.sprite.Sprite(ball_image, x=50, y=50)
		self.add_motion("x", -600, 200, 100)

	def draw(self):
		self.obj.draw()

# ---------------------------------------------------------------
