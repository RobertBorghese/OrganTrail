from scenes.scene_base import Scene_Base
from scenes.scene_test import Scene_Test

class Scene_TitleScreen(Scene_Base):
	def setup(self):
		self.set_background("images/Background1.png")
		self.play_song("audio/testmusic2.mp3")

		GAME_WIDTH = self.window.game_width
		GAME_HEIGHT = self.window.game_height

		# Shows a piece of text on-screen to act as "Title"
		# Perhaps place title text on background image instead?
		self.show_text(GAME_WIDTH / 4, GAME_HEIGHT / 3, GAME_WIDTH, "Organ Trail: The Game!", 50)

		self.show_picture("images/TestImage1.png", 30, 30)

		# The format for the buttons' font
		# ["Font Name", #Font Size#, #Font Weight#, ?Is Italic?]
		FONT = ["Arial", 18, -1, False]

		# The format for the buttons' colors
		# ["Top Color", "Bottom Color", "Outline Color"]
		COLORS = ["#7D7DB4","#64648C","252525"]

		BUTTON_WIDTH = 200
		BUTTON_HEIGHT = 40

		self.add_button(x = (GAME_WIDTH * (1 / 4)) - (BUTTON_WIDTH / 2),
						y = GAME_HEIGHT * (3 / 4), 
						w = BUTTON_WIDTH,
						h = BUTTON_HEIGHT,
						name = "Play New Game",
						font = FONT,
						buttonColors = COLORS,
						action = self.new_game)

		self.add_button(x = (GAME_WIDTH * (2 / 4)) - (BUTTON_WIDTH / 2),
						y = GAME_HEIGHT * (3 / 4), 
						w = BUTTON_WIDTH,
						h = BUTTON_HEIGHT,
						name = "Change Options",
						font = FONT,
						buttonColors = COLORS,
						action = self.options)

		self.add_button(x = (GAME_WIDTH * (3 / 4)) - (BUTTON_WIDTH / 2),
						y = GAME_HEIGHT * (3 / 4), 
						w = BUTTON_WIDTH,
						h = BUTTON_HEIGHT,
						name = "Quit Game",
						font = FONT,
						buttonColors = COLORS,
						action = self.quit)

		self.wait_for_button_press()

	def new_game(self):
		self.goto_scene(Scene_Test)

	def options(self):
		self.add_dialog("TODO: Actually make options scene.")

	def quit(self):
		self.close_game()