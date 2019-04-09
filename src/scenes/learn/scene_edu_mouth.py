#Shash
import random

from scenes.scene_base import Scene_Base
import scenes.scene_other_test
from scenes.common.scene_fight import Scene_Fight

FONT = ["Arial", 18, -1, False]

class Scene_Edu_Mouth(Scene_Base):
    def setup(self):
        self.set_background("images/Background1.png") #replace with correct background
        self.play_song("audio/testmusic2.mp3")

        self.add_dialog("The victim was enjoying a nice restaurant with some friends.")
        self.add_dialog("Unfortunately the restaurant had some health code violations that day...")
        self.add_dialog("They ate the seafood, and you went along for the ride. Open wide...")
        self.add_dialog("Look at that, you've got direct access to the stomach! Down the esophagus you go!") 
        self.add_dialog("Todo: finish stomach paths")

        self.goto_scene(Scene_Fight)