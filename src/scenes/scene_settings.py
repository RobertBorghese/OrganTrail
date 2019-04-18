from scenes.scene_base import Scene_Base
from scenes.scene_enter import Scene_Enter

class Scene_Settings(Scene_Base):
	def setup(self):
		self.set_background("images/Background1.png")
		self.play_song("audio/testmusic.wav")

		GAME_WIDTH = self.window.game_width
		GAME_HEIGHT = self.window.game_height

		# The format for the buttons' font
		# ["Font Name", #Font Size#, #Font Weight#, ?Is Italic?]
		FONT = ["Arial", 15, -1, False]

		# The format for the buttons' colors
		# ["Top Color", "Bottom Color", "Outline Color"]
		COLORS = ["#7D7DB4","#64648C","252525"]

		BUTTON_WIDTH = 200
		BUTTON_HEIGHT = 40
		BUTTON_Y = GAME_HEIGHT * (3 / 4) + 20

		self.add_button(x = (GAME_WIDTH * (1 / 4)) - (BUTTON_WIDTH / 2),
						y = BUTTON_Y, 
						w = BUTTON_WIDTH,
						h = BUTTON_HEIGHT,
						name = "Adjust Volume",
						font = FONT,
						buttonColors = COLORS,
						action = self.adjustVol)

		self.add_button(x = (GAME_WIDTH * (2 / 4)) - (BUTTON_WIDTH / 2),
						y = BUTTON_Y, 
						w = BUTTON_WIDTH,
						h = BUTTON_HEIGHT,
						name = "Back to Main",
						font = FONT,
						buttonColors = COLORS,
						action = self.title)

		self.wait_for_button_press()

	def adjustVol(self):
		self.goto_scene(scenes.scene_titlescreen.Scene_TitleScreen)
	def title(self):
		self.goto_scene(scenes.scene_titlescreen.Scene_TitleScreen)