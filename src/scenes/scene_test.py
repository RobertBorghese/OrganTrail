import pyglet

from scenes.scene_base import Scene_Base
from objects.object_test import Object_Test
from objects.object_text import Object_Text

# ---------------------------------------------------------------
# * Scene_Test
#
# This is a test scene for practicing features.
# It is a child class of Scene_Base in order to inhereit functions.
#
# Check out scenes/Scene_Base.py for information about the functions.
# ---------------------------------------------------------------
class Scene_Test(Scene_Base):
	def create(self):
		self.label = Object_Text("Hello World", "Comic Sans", 36, self.window.width // 2, self.window.height // 2)
		self.add_object(self.label)
		self.add_object(Object_Test())

	def update(self):
		super().update()
		#self.label.x += 1

	def on_mouse_move(self, x, y, dx, dy):
		print("Mouse moved: [" + str(x) + ", " + str(y) + "]")

	def on_mouse_press(self, x, y, button, modifiers):
		print("Mouse button #" + str(button) + " pressed at [" + str(x) + ", " + str(y) + "]")

# ---------------------------------------------------------------
