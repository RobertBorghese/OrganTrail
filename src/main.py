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

"""
window = pyglet.window.Window()
label = pyglet.text.Label('Hello, world', font_name='Times New Roman', font_size=36, x=window.width//2, y=window.height//2, anchor_x='center', anchor_y='center')

@window.event
def on_draw():
	window.clear()
	label.draw()

def update(dt):
	label.x = label.x + 1

def main():
	print("TEsts")
	print(label.x)
	pyglet.clock.schedule_interval(update, 1/120.0)
	pyglet.app.run()

main()
"""
"""
# ---------------------------------------------------------------
# * Game
#
# This is the main class that runs the game.
# ---------------------------------------------------------------
class Game():
	def __init__(self):
		self.current_scene = None
		self.window = None
		self.should_run = True

	# Called once the game starts
	def start_game(self):
		pygame.init()
		pygame.font.init()

		# Creates window
		self.window = pygame.display.set_mode((800, 600));

		# Sets window title
		pygame.display.set_caption("The Virus Game Thingy")

		# Sets "scene" to starting scene
		self.current_scene = self.create_starting_scene()

	# Runs the game
	def run_game(self):
		while self.should_run:
			self.handle_events()
			self.update_game()

	# Handles events like QUIT, MOUSEMOTION, and MOUSEBUTTONDOWN
	def handle_events(self):
		for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.should_run = False
				elif event.type == pygame.MOUSEMOTION:
					if self.current_scene != None:
						pos = event.pos
						self.current_scene.on_mouse_move(pos[0], pos[1])
				elif event.type == pygame.MOUSEBUTTONDOWN:
					if self.current_scene != None:
						pos = event.pos
						self.current_scene.on_mouse_pressed(pos[0], pos[1], event.button)

	# Updates and renders the current scene
	def update_game(self):
		if self.current_scene != None:
			self.current_scene.update()
			if self.window != None:
				self.window.fill((255, 255, 255))
			self.current_scene.render(self.window)
			pygame.display.update()

	# Called once game ends
	def finish_game(self):
		pygame.quit()
		pygame.font.quit()

	# Returns an instance of the starting scene
	# TODO: Change to title scene
	def create_starting_scene(self):
		return Scene_Test()

# ---------------------------------------------------------------

# Creates a "Game" object than runs it
def main():
	game = Game()
	game.start_game()
	game.run_game()
	game.finish_game()
"""

# If this is the main file, it runs the "main" function
#if __name__ == "__main__":
#	main()
