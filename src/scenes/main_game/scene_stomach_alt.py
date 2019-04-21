#Shash
from scenes.scene_base import Scene_Base
from scenes.scene_game_over import Scene_Game_Over
from scenes.main_game.scene_neuron import Scene_Neuron
from scenes.main_game.scene_antibodies import Scene_Antibodies
from scenes.main_game.scene_neuron import Scene_Neuron

class Scene_Stomach_Alt(Scene_Base):
    def setup(self):
        '''
        #Note: This block is for testing only. Use if you are skipping straight to this scene
        self.set_value("vaxx", False)
        self.set_value("entry", 0)
        self.set_value("pathogen", 1) #change as needed
        self.set_value("player_frames", ["images/rashCrash_0", "images/rashCrash_1"]) #change as needed
		#temp value for player animation, will set later in enter scene
        self.set_value("player_animation", 0)
        '''
        GAME_WIDTH = self.window.game_width
        GAME_HEIGHT = self.window.game_height
        self.play_song("audio/testmusic2.mp3")
		
        self.set_value("player_animation", self.show_picture(self.get_value("player_frames"), GAME_WIDTH/2, 30, 20))
        self.set_background("images/stomach_inside.jpg")

        self.add_dialog("You've reached the stomach! But your mission is far from over.")
        self.add_dialog("This is where food goes after its been chewed up.")
        self.add_dialog("Digestive enzymes and acids aid in digestion.")
        self.add_dialog("Don't worry, you're too small to be affected. Just keep moving.")
        self.add_dialog("Get to the bloodstream ASAP. You can move to the intestines and get absorbed into the stream.")
        self.set_background("images/intestines.jpg")
        self.add_dialog("Okay, you made it. You can try and get reabsorbed here, but there's a crowded mix of cells on the other side. Things that were just reabsorbed before you.")
        self.add_dialog("Might be harder to fight past everything.")
        self.add_dialog("On the other hand, if you keep going down the intestines and go too far, you might end up leaving the body altogether.")
        self.add_dialog("I'll leave that to your imagination.")
        self.add_button(x = 600,
						y = 400, 
						w = 300,
						h = 40,
						name = "Enter bloodstream here",
						buttonColors = ["#7D7DB4","#64648C","252525"],
						font = ["Arial", 17, -1, False],
						action = self.blood)
        self.add_button(x = 200,
						y = 400, 
						w = 300,
						h = 40,
						name = "Keep moving",
						buttonColors = ["#7D7DB4","#64648C","252525"],
						font = ["Arial", 17, -1, False],
						action = self.forward)
        self.wait_for_button_press()

    def blood(self):
        self.remove_all_buttons()
        self.add_dialog("You decide to enter the bloodstream here.")
        self.add_dialog("As soon as you enter, you come across a group of phagocytes, eating up everything they can.")
        self.add_dialog("And you also become their food.")
        self.add_dialog("This is the end for you.")
        self.goto_scene(Scene_Game_Over)


    def forward(self):
        self.remove_all_buttons()
        self.add_dialog("You decide to keep moving. You find a nice open slot and enter the bloodstream.")
        self.add_dialog("There are fewer defense cells here.")
        if self.get_value("pathogen") == 2:
            self.goto_scene(Scene_Neuron)
        else:
            self.goto_scene(Scene_Antibodies)


    