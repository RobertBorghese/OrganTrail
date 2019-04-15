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

		self.add_dialog("Hello, pathogen!")
		#display user's avatar, if-case based on self.pathogen

		self.add_dialog("It's a cruel world out there, and you look like you need some place warm, with lots of nourishment.")
		self.add_dialog("Hey, it's a human person. That's your victim!")
        #chance of vaccination
		#self.set_vaxx()
		if self.generate_random_chance(0): #change t0 50 eventually
			self.set_value("vaxx", True)
		else:
			self.set_value("vaxx", False)
		
		print(self.get_value("vaxx"))

		if self.generate_random_chance(100): #change to 50 eventually
			self.set_value("entry", 0)
		else:
			self.set_value("entry", 1)
		
		print(self.get_value("entry"))

		if self.get_value("vaxx"):
			self.add_dialog("The victim was smart and got vaccinated this season. Be careful! (lower chances of survival)")
		else:
			self.add_dialog("The victim is from Oregon! No vaccines in here! (higher chances of survival)")
		
		#Entry point
		if self.get_value("entry") == 0:
			self.goto_scene(Scene_Edu_Blood)
		else:
			self.goto_scene(Scene_Edu_Mouth) #TBC
