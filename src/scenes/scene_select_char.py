#Shash

import random
from scenes.scene_base import Scene_Base
from scenes.scene_enter import Scene_Enter

class Scene_SelectChar(Scene_Base):
    def setup(self):
        #todo: add title (Character selection + descriptions)
        self.add_button(x = 200,
					y = 200, 
					w = 200,
					h = 40,
					name = "Jelly Belly",
					buttonColors = ["#7D7DB4","#64648C","252525"],
					font = ["Arial", 18, -1, False],
					action = self.jelly)
        self.add_button(x = 600,
					y = 200, 
					w = 200,
					h = 40,
					name = "Rash Crash",
					buttonColors = ["#7D7DB4","#64648C","252525"],
					font = ["Arial", 18, -1, False],
					action = self.rash)
        self.add_button(x = 200,
					y = 400, 
					w = 200,
					h = 40,
					name = "Hack Pack",
					buttonColors = ["#7D7DB4","#64648C","252525"],
					font = ["Arial", 18, -1, False],
					action = self.hack)
        self.add_button(x = 600,
					y = 400, 
					w = 200,
					h = 40,
					name = "Blaze Daze",
					buttonColors = ["#7D7DB4","#64648C","252525"],
					font = ["Arial", 18, -1, False],
					action = self.blaze)

    def jelly(self):
        self.set_value("pathogen", 1)
        self.goto_scene(Scene_Enter)
    
    def rash(self):
        self.set_value("pathogen", 2)
        self.goto_scene(Scene_Enter)

    def hack(self):
        self.set_value("pathogen", 3)
        self.goto_scene(Scene_Enter)

    def blaze(self):
        self.set_value("pathogen", 4)
        self.goto_scene(Scene_Enter)