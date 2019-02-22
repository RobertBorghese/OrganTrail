import random

from scenes.scene_base import Scene_Base
import scenes.scene_other_test

class Scene_Test(Scene_Base):
	def setup(self):
		self.set_background("images/Background.png")
		self.play_song("audio/testmusic2.mp3")

		self.add_dialog("This is the first message!")
		self.add_dialog("This is a second message!")
		self.add_dialog("There is a 50% chance we will go to the next scene; otherwise, we will loop this one.")

		if random.randint(1, 100) >= 50:
			self.goto_scene(scenes.scene_other_test.Scene_Other_Test)
		else:
			self.goto_scene(Scene_Test)