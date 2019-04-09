#Shash
import random

from scenes.scene_base import Scene_Base
from scenes.scene_game_over import Scene_Game_Over

FONT = ["Arial", 18, -1, False]

class Scene_Fight(Scene_Base):
	def setup(self):
		
		self.set_background("images/Background1.png")
		self.play_song("audio/danger_jingle.mp3") #note: keeps repeating, not sure how to stop

		#Todo: add image of WBC like a pokemon just appeared

		self.add_dialog("A White Blood Cell arrived!")
        #chance of vaccination
		print(self.vaxx)
		if self.vaxx:
			self.add_dialog("The victim is vaccinated, so you only have a 20% chance of beating the cell.")
			self.add_button(x = 400,
						y = 400, 
						w = 300,
						h = 40,
						name = "Attack!",
						buttonColors = ["#7D7DB4","#64648C","252525"],
						font = ["Arial", 18, -1, False],
						action = self.fight)
		else:
			self.add_dialog("This victim is unvaccinated, so you have an 80% chance of beating the cell!")
			self.add_button(x = 400,
						y = 400, 
						w = 300,
						h = 40,
						name = "Attack!",
						buttonColors = ["#7D7DB4","#64648C","252525"],
						font = ["Arial", 18, -1, False],
						action = self.fight)

	def fight(self):
		self.add_dialog("You fight.")
		if self.vaxx:
			if self.generate_random_chance(20):
				self.add_dialog("Hit! Show 'em who's boss!")
				#animation of WBC death
				#goto: next scene
			else:
				self.add_dialog("Your will was strong, but the blood cell was stronger...")
				self.goto_scene(Scene_Game_Over)
		else:
			if self.generate_random_chance(80):
				self.add_dialog("Hit! Show 'em who's boss!")
				#animation of WBC death
				#goto: next scene

			else:
				self.add_dialog("Your will was strong, but the blood cell was stronger...")
				self.goto_scene(Scene_Game_Over)


			
		
