import pyglet

# ---------------------------------------------------------------
# * Scene_Base
#
# The parent class of all "scenes"
# These manipulate behavior of various objects and should be reused.
# ---------------------------------------------------------------
class Scene_Base():
	def __init__(self, game):
		self.game = game
		self.window = game.window
		self.objects = []
		self.create()

	# This is called when the scene starts. Used to add objects.
	def create(self):
		pass

	# This is called to draw the scene to the screen.
	def draw(self):
		for obj in self.objects:
			obj.draw()

	# This is called every frame to update the game logic.
	def update(self):
		for obj in self.objects:
			if hasattr(obj, "update"):
				obj.update()

	# Whenever key is pressed, this function is called
	def on_key_press(self, key, modifiers):
		pass

	# Whenver key is released, this function is called
	def on_key_release(self, key, modifiers):
		pass

	# Whenever the mouse is moved, this function is called.
	def on_mouse_move(self, x, y, dx, dy):
		pass

	# Whenever a mouse button is pressed, this function is called.
	def on_mouse_press(self, x, y, button, modifiers):
		pass

	# Whenever a mouse button is released, this function is called
	def on_mouse_release(self, x, y, button, modifiers):
		pass

	# Adds an object to the scene
	def add_object(self, obj):
		self.objects.append(obj)

	# Goes to a different scene
	def goto_scene(self, scene, transition=60):
		self.game.goto_scene(scene, transition)

	# Adds a dialog to the story
	def add_dialog(self, text):
		pass

# ---------------------------------------------------------------
