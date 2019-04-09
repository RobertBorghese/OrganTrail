#Shash
import random

from scenes.scene_base import Scene_Base
from scenes.learn.scene_edu_blood import Scene_Edu_Blood
from scenes.learn.scene_edu_mouth import Scene_Edu_Mouth

FONT = ["Arial", 18, -1, False]

class Scene_Enter(Scene_Base):
	def setup(self):
		self.set_background("images/Background1.png") #replace with correct background
		self.play_song("audio/testmusic2.mp3")

		self.add_dialog("Welcome to the body!")
        #chance of vaccination
		self.set_vaxx()
		print(self.vaxx)
		self.set_entry()
		if self.vaxx:
			self.add_dialog("This victim was smart and got vaccinated this season. Be careful!")
		else:
			self.add_dialog("The victim is from Oregon! No vaccines in here!")
		
		#Entry point
		if self.entry == 0:
			self.goto_scene(Scene_Edu_Blood)
		else:
			self.goto_scene(Scene_Edu_Mouth)