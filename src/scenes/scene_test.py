import random

from scenes.scene_base import Scene_Base
import scenes.scene_other_test
import scenes.scene_game_over

FONT = ["Arial", 18, -1, False]

class Scene_Test(Scene_Base):
	def setup(self):
		self.set_background("images/Background1.png")
		self.play_song("audio/testmusic2.mp3")

		self.add_dialog("Welcome to the game!")
		self.add_dialog("You currently have " + str(self.get_value("Health")) + " health!")
		self.add_dialog("Do you want to go on an adventure?")

		self.add_button(x = 600,
						y = 400, 
						w = 300,
						h = 40,
						name = "Go on Adventure",
						buttonColors = ["#7D7DB4","#64648C","252525"],
						font = ["Arial", 18, -1, False],
						action = self.go_on_adventure)

		self.add_button(x = 200,
						y = 400, 
						w = 300,
						h = 40,
						name = "Do not go",
						buttonColors = ["#b57d7d","#64648C","252525"],
						font = ["Arial", 18, -1, False],
						action = self.do_not_go)

		self.wait_for_button_press()

	def go_on_adventure(self):
		self.add_dialog("You decide to go on an adventure!")
		self.goto_scene(scenes.scene_other_test.Scene_Other_Test)

	def do_not_go(self):
		self.add_dialog("You decide to not go on an adventure")
		self.goto_scene(scenes.scene_game_over.Scene_Game_Over)