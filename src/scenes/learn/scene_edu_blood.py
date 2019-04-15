#Shash
import random

from scenes.scene_base import Scene_Base
import scenes.scene_other_test
from scenes.scene_game_over import Scene_Game_Over
from scenes.common.scene_platelet import Scene_Platelet

FONT = ["Arial", 18, -1, False]

class Scene_Edu_Blood(Scene_Base):
    def setup(self):
        #self.set_background("images/Background1.png") #replace with correct background
        self.play_song("audio/testmusic2.mp3")

        self.add_dialog("The victim got a cut on their knee from a...football injury. Yes.")
        self.add_dialog("Not because they slipped while they were running to turn off the oven with Bagel Bites inside.")
        self.add_dialog("You took the chance and ran into the new opening. Now look around.")
        self.set_background("images/bloodstream.png")

        self.add_dialog("Ah, the bloodstream. So nice and tranquil, with cells all over the place.") 
        self.add_dialog("Red blood cells, carrying oxygen, and white blood cells, looking for pathogens to kill.")
        self.add_dialog("They have no idea what they're in for.")
        self.add_dialog("But wait -- they've noticed the damage to the skin!") 
        self.add_dialog("Neutrophils, or first-responder white blood cells, are coming to catch the invaders!")
        self.set_background("images/boxing.png")

        self.play_song("audio/danger_jingle.mp3") #note: keeps repeating, not sure how to stop
		#Todo: add image of WBC like a pokemon just appeared

        self.add_dialog("A White Blood Cell arrived!")
        #chance of vaccination
        print(self.get_value("vaxx"))
        if self.get_value("vaxx"):
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
		#bug: fades away to next scene too quickly, we can't see all the text
        if self.get_value("vaxx"):
            if self.generate_random_chance(20):
                self.add_dialog("Hit! Show 'em who's boss!")
                self.add_dialog("Hit! Show 'em who's boss!")
                self.add_dialog("Better get going before more show up...")
				#animation of WBC death
                self.goto_scene(Scene_Platelet)
            else:
                self.add_dialog("Your will was strong, but the blood cell was stronger...")
                self.add_dialog("Your will was strong, but the blood cell was stronger...")
                self.goto_scene(Scene_Game_Over)
        else:
            if self.generate_random_chance(100): #change to 80 eventually
                self.add_dialog("Hit! Show 'em who's boss!")
                self.add_dialog("Hit! Show 'em who's boss!")
                self.add_dialog("Better get going before more show up...")
				#animation of WBC death
                self.goto_scene(Scene_Platelet)

            else:
                self.add_dialog("Your will was strong, but the blood cell was stronger...")
                self.add_dialog("Your will was strong, but the blood cell was stronger...")
                self.goto_scene(Scene_Game_Over)
