from scenes.scene_base import Scene_Base
from scenes.scene_test import Scene_Test
from scenes.scene_enter import Scene_Enter
from scenes.scene_select_char import Scene_SelectChar

from objects.settings_dialog import Settings_Dialog

class Scene_TitleScreen(Scene_Base):
	def setup(self):
		self.set_background("images/Background1.png")
		self.play_song("audio/testmusic.wav")

		self.showMenu()

	def new_game(self):
		self.goto_scene(Scene_SelectChar)
		#self.goto_scene(Scene_Test)

	def showMenu(self):
		GAME_WIDTH = self.window.game_width
		GAME_HEIGHT = self.window.game_height
		# Show animated picture offscreen...
		title_character = self.show_picture(["images/hackPack_0.png", "images/hackPack_1.png"], -500, 30)
		# ... and move it to center of screen
		self.move_picture(title_character, GAME_WIDTH, 20, 300, False)

		# Shows a piece of text on-screen to act as "Title"
		# Perhaps place title text on background image instead?
		#self.show_text(GAME_WIDTH / 4, GAME_HEIGHT / 3, GAME_WIDTH, "Organ Trail: The Game!", 50)
		title_screen_images = [
			"images/titleScreen_0",
			"images/titleScreen_1",
			"images/titleScreen_2",
			"images/titleScreen_3"
		]
		title = self.show_picture(title_screen_images, GAME_WIDTH / 4, 30, 10)

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
						name = "Play New Game",
						font = FONT,
						buttonColors = COLORS,
						action = self.new_game)

		self.add_button(x = (GAME_WIDTH * (2 / 4)) - (BUTTON_WIDTH / 2),
						y = BUTTON_Y, 
						w = BUTTON_WIDTH,
						h = BUTTON_HEIGHT,
						name = "Change Options",
						font = FONT,
						buttonColors = COLORS,
						action = self.showSettings)

		self.add_button(x = (GAME_WIDTH * (3 / 4)) - (BUTTON_WIDTH / 2),
						y = BUTTON_Y, 
						w = BUTTON_WIDTH,
						h = BUTTON_HEIGHT,
						name = "Quit Game",
						font = FONT,
						buttonColors = COLORS,
						action = self.quit)

		self.set_value("Health", 10)

		self.wait_for_button_press()
		#hide title graphics when button is clicked
		#self.hide_picture(title)


	def showSettings(self):
		dialog = Settings_Dialog(self.window)
		dialog.exec()
		self.wait_for_button_press()
		"""
		#removes buttons from menu
		self.remove_all_buttons()
		GAME_WIDTH = self.window.game_width
		GAME_HEIGHT = self.window.game_height
		
		#show settings title
		settings_images = [
			"images/settings_0",
			"images/settings_1",
			"images/settings_2"
		]
		settings = self.show_picture(settings_images, GAME_WIDTH / 5, 30, 15)
		
		# The format for the buttons' font
		# ["Font Name", #Font Size#, #Font Weight#, ?Is Italic?]
		FONT = ["Arial", 15, -1, False]

		# The format for the buttons' colors
		# ["Top Color", "Bottom Color", "Outline Color"]
		COLORS = ["#7D7DB4","#64648C","252525"]

		BUTTON_WIDTH = 200
		BUTTON_HEIGHT = 40
		BUTTON_Y = GAME_HEIGHT * (3 / 4) + 20
		
		self.add_button(x = (GAME_WIDTH * (1 / 3)) - (BUTTON_WIDTH / 2),
						y = BUTTON_Y, 
						w = BUTTON_WIDTH,
						h = BUTTON_HEIGHT,
						name = "Adjust Volume",
						font = FONT,
						buttonColors = COLORS,
						action = self.adjustVol)

		self.add_button(x = (GAME_WIDTH * (2 / 3)) - (BUTTON_WIDTH / 2),
						y = BUTTON_Y, 
						w = BUTTON_WIDTH,
						h = BUTTON_HEIGHT,
						name = "Back to Main",
						font = FONT,
						buttonColors = COLORS,
						action = self.showMenu)

		self.wait_for_button_press()
		#removes settings title and buttons before going back to menu
		self.hide_picture(settings)
		self.remove_all_buttons()
		"""

	def adjustVol(self):
		self.showMenu()

	def quit(self):
		self.close_game()