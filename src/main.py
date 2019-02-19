import pyglet

# import Scene_Test from scenes/scene_test.py
from scenes.scene_test import Scene_Test

# Place the initial scene here!
STARTING_SCENE = Scene_Test

# ---------------------------------------------------------------
# * Game
#
# This is the main class that runs the game.
# ---------------------------------------------------------------
class Game():
	def __init__(self):
		self.create_window()
		self.create_first_scene()

	def create_first_scene(self):
		self.scene = STARTING_SCENE(self)

	def create_window(self):
		self.window = pyglet.window.Window()
		self.window.on_draw = self.draw
		self.window.on_key_press = self.on_key_press
		self.window.on_key_release = self.on_key_release
		self.window.on_mouse_motion = self.on_mouse_motion
		self.window.on_mouse_press = self.on_mouse_press
		self.window.on_mouse_release = self.on_mouse_release

	def start(self):
		pyglet.clock.schedule_interval(self.update, 1/120.0)
		pyglet.app.run()

	def draw(self):
		self.window.clear()
		self.scene.draw()

	def update(self, dt):
		self.scene.update()

	def goto_scene(self, scene, transition):
		self.scene = scene

	def on_key_press(self, key, modifiers):
		self.scene.on_key_press(key, modifiers)

	def on_key_release(self, key, modifiers):
		self.scene.on_key_release(key, modifiers)

	def on_mouse_motion(self, x, y, dx, dy):
		self.scene.on_mouse_move(x, y, dx, dy)

	def on_mouse_release(self, x, y, button, modifiers):
		self.scene.on_mouse_release(x, y, button, modifiers)

	def on_mouse_press(self, x, y, button, modifiers):
		self.scene.on_mouse_press(x, y, button, modifiers)

# ---------------------------------------------------------------

# Creates a "Game" object then runs it
def main():
	game = Game()
	print("-- Game has started --")
	game.start()
	print("-- Game has ended --")

# If this is the main file, it runs the "main" function
if __name__ == "__main__":
	main()
