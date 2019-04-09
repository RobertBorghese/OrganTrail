#Shash
import random

from scenes.scene_base import Scene_Base
import scenes.scene_other_test
from scenes.common.scene_fight import Scene_Fight

FONT = ["Arial", 18, -1, False]

class Scene_Edu_Blood(Scene_Base):
    def setup(self):
        self.set_background("images/Background1.png") #replace with correct background
        self.play_song("audio/testmusic2.mp3")

        self.add_dialog("The victim got a cut on their knee from a...football injury. Yes.")
        self.add_dialog("Not because they slipped while they were running to turn off the oven with Bagel Bites inside.")
        self.add_dialog("You took the chance and ran into the new opening. Now look around.")
        self.add_dialog("Ah, the bloodstream. So nice and tranquil, with cells all over the place.") 
        self.add_dialog("Red blood cells, carrying oxygen, and white blood cells, looking for pathogens to kill.")
        self.add_dialog("They have no idea what they're in for.")
        self.add_dialog("But wait -- they've noticed the damage to the skin!") 
        self.add_dialog("Neutrophils, or first-responder white blood cells, are coming to catch the invaders!")
        self.goto_scene(Scene_Fight)