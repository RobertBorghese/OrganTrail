#Shash
import random

from scenes.scene_base import Scene_Base
from scenes.main_game.scene_edu_blood import Scene_Edu_Blood
from scenes.main_game.scene_edu_mouth import Scene_Edu_Mouth

FONT = ["Arial", 18, -1, False]

class Scene_Enter(Scene_Base):
	def setup(self):

		self.play_song("audio/testmusic2.mp3")

		#Image and description of user's character
		if self.get_value("pathogen") == 1:
			self.add_dialog("Hello, Jelly Belly!")
			pic_id = self.show_picture("images/jellyBelly_0.png", 500, 30, 30)
			self.move_picture(pic_id, -100, 30, 50)
			self.add_dialog("You are a virus that targets the stomach and digestive system, causing stomach aches.")

		elif self.get_value("pathogen") == 2:
			self.add_dialog("Hello, Rash Crash!")
			pic_id = self.show_picture("images/rashCrash_0.png", 500, 30, 30)
			self.move_picture(pic_id, -100, 30, 50)
			self.add_dialog("You are a virus that targets the outer skin layer, causing rashes.")

		elif self.get_value("pathogen") == 3:
			self.add_dialog("Hello, Blaze Daze!")
			pic_id = self.show_picture("images/blazeDaze_0.png", 500, 30, 30)
			self.move_picture(pic_id, -100, 30, 50)
			self.add_dialog("You are a bacteria that causes high fevers.")

		self.add_dialog("It's a cruel world out there, and you look like you need some place warm, with lots of nourishment.")
		pic_id = self.show_picture("images/human.png", 800, 100, 30)
		self.move_picture(pic_id, 300, 100, 50)
		self.add_dialog("Hey, it's a human person. That's your victim!")

        #chance of vaccination
		if self.generate_random_chance(0): #change to 50 eventually
			self.set_value("vaxx", True)
		else:
			self.set_value("vaxx", False)
		
		#print(self.get_value("vaxx"))

        #entry point (cut or mouth)
		if self.generate_random_chance(100): #change to 50 eventually
			self.set_value("entry", 0) #cut
		else:
			self.set_value("entry", 1) #mouth
		
		#print(self.get_value("entry"))

		if self.get_value("vaxx"):
			self.add_dialog("The victim was smart and got vaccinated this season. Be careful! (lower chances of survival)")
		else:
			self.add_dialog("The victim is from Oregon! No vaccines in here! (higher chances of survival)")
		
		#Entry point
		if self.get_value("entry") == 0:
			self.goto_scene(Scene_Edu_Blood)
		else:
			self.goto_scene(Scene_Edu_Mouth) #TBC
