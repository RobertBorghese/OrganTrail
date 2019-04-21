#Shash
from scenes.scene_base import Scene_Base
from scenes.scene_game_over import Scene_Game_Over
from scenes.main_game.scene_final_rash import Scene_Final_Rash

class Scene_Neuron(Scene_Base):
    def setup(self):
        '''
        #Note: This block is for testing only. Use if you are skipping straight to this scene
        self.set_value("vaxx", False)
        self.set_value("entry", 0)
        self.set_value("pathogen", 1)
        self.set_value("player_frames", ["images/rashCrash_0", "images/rashCrash_1"])
		#temp value for player animation, will set later in enter scene
        self.set_value("player_animation", 0)
        '''
        GAME_WIDTH = self.window.game_width
        GAME_HEIGHT = self.window.game_height
		#only rash crash goes here
		#load up character animation
		#character is loaded up here
        self.set_value("player_animation", self.show_picture(self.get_value("player_frames"), GAME_WIDTH/2, 30, 20))
        
        self.play_song("audio/testmusic2.mp3")
        self.set_background("images/bloodstream.png")

        self.add_dialog("Alright, you've been traveling and multiplying a bit.")
        self.add_dialog("The body is starting to notice. Blood cells have been alerted.")
        self.add_dialog("You may wanna hide for a bit. Viruses tend to do that.")
        self.add_dialog("In fact, viruses can hide their DNA in other cells for years without doing anything.")
        self.add_dialog("Then, something will trigger them to activate and go nuts.")
        #Todo: show neuron cell here
        self.add_dialog("You can hide in this neuron up here. It's right under the epidermis, or the outer skin layer.")
        self.add_dialog("That's your goal, after all. Or, if you want, you can brute force it and keep trucking along the bloodstream.")
        self.add_button(x = 600,
						y = 400, 
						w = 300,
						h = 40,
						name = "Hide in neuron",
						buttonColors = ["#7D7DB4","#64648C","252525"],
						font = ["Arial", 17, -1, False],
						action = self.hide_neuron)
        self.add_button(x = 200,
						y = 400, 
						w = 300,
						h = 40,
						name = "Keep moving",
						buttonColors = ["#7D7DB4","#64648C","252525"],
						font = ["Arial", 17, -1, False],
						action = self.forward)
        self.wait_for_button_press()

    def hide_neuron(self):
        self.remove_all_buttons()
        self.add_dialog("You hide in the neuron. Perfect timing, too. A large group of white blood cells just went by.")
        self.add_dialog("Now you multiply and spread out among the neurons and the epidermis.")
        self.goto_scene(Scene_Final_Rash)
		


    def forward(self):
        self.remove_all_buttons()
        self.add_dialog("Onward! You keep moving forward.")
        self.add_dialog("Unfortunately, a group of white blood cells were patrolling this area.")
        self.add_dialog("They all gang up. This is the end for you.")
        self.goto_scene(Scene_Game_Over)