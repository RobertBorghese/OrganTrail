#Shash

#Needs fixing (format)
import random
from scenes.scene_base import Scene_Base
from scenes.scene_enter import Scene_Enter

class Scene_SelectChar(Scene_Base):
    def setup(self):
        GAME_WIDTH = self.window.game_width
        GAME_HEIGHT = self.window.game_height
        self.show_text(GAME_WIDTH / 4, GAME_HEIGHT / 20, GAME_WIDTH / 2, "Select your character.", 30, "#000000")
        self.show_picture(["images/jellyBelly_0.png", "images/jellyBelly_1.png"], -80, 50, 30)
        self.add_button(x = 80,
					y = 475, 
					w = 200,
					h = 40,
					name = "Jelly Belly",
					buttonColors = ["#7D7DB4","#64648C","252525"],
					font = ["Arial", 18, -1, False],
					action = self.jelly)

        self.show_picture(["images/rashCrash_0.png", "images/rashCrash_1.png"], 700, 50, 30)
        self.add_button(x = 850,
					y = 475, 
					w = 200,
					h = 40,
					name = "Rash Crash",
					buttonColors = ["#7D7DB4","#64648C","252525"],
					font = ["Arial", 18, -1, False],
					action = self.rash)

        self.show_picture(["images/blazeDaze_0.png", "images/blazeDaze_1.png"], 300, 50, 30)
        self.add_button(x = 450,
					y = 475, 
					w = 200,
					h = 40,
					name = "Blaze Daze",
					buttonColors = ["#7D7DB4","#64648C","252525"],
					font = ["Arial", 18, -1, False],
					action = self.blaze)

    #set_Value provides global access to character animation
    def jelly(self):
        self.set_value("pathogen", 1)
        self.set_value("player_frames", ["images/jellyBelly_0", "images/jellyBelly_1"])
		#temp value for player animation, will set later in enter scene
        self.set_value("player_animation", 0)
        self.goto_scene(Scene_Enter)
    
    def rash(self):
        self.set_value("pathogen", 2)
        self.set_value("player_frames", ["images/rashCrash_0", "images/rashCrash_1"])
		#temp value for player animation, will set later in enter scene
        self.set_value("player_animation", 0)
        self.goto_scene(Scene_Enter)

    def blaze(self):
        self.set_value("pathogen", 3)
        self.set_value("player_frames", ["images/blazeDaze_0", "images/blazeDaze_1"])
		#temp value for player animation, will set later in enter scene
        self.set_value("player_animation", 0)
        self.goto_scene(Scene_Enter)
