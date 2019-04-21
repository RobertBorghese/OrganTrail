#Shash
from scenes.scene_base import Scene_Base
from scenes.scene_game_over import Scene_Game_Over

class Scene_Final_Blaze(Scene_Base):
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

        self.add_dialog("You've been doing some work.")
        self.add_dialog("The temperature is going higher, but your army is persevering.")
        self.add_dialog("The victim is not feeling too great.")
        self.add_dialog("Headaches, chills, stuff like that.")
        self.add_dialog("It's time to finish this. The victim should be eating some medicine soon. Will you run away? Or will you face it head-on?")
        self.add_button(x = 600,
						y = 400, 
						w = 300,
						h = 40,
						name = "Run",
						buttonColors = ["#7D7DB4","#64648C","252525"],
						font = ["Arial", 17, -1, False],
						action = self.run)
        self.add_button(x = 200,
						y = 400, 
						w = 300,
						h = 40,
						name = "Face it",
						buttonColors = ["#7D7DB4","#64648C","252525"],
						font = ["Arial", 17, -1, False],
						action = self.face)
        self.wait_for_button_press()

    def face(self):
        self.remove_all_buttons()
        self.add_dialog("You face the medicine. What's the worst that can happen?")
        self.add_dialog("Ah...just like that, 99.9% of your army is gone. But what's this?")
        self.add_dialog("You somehow survived? But how?")
        self.add_dialog("Antibacterial resistance!!! You were one of only a few bacteria who had a mutation allowing you to resist the antibiotics.")
        self.add_dialog("Now you can replicate and pass on your mutation. And with the exponential growth that follows...")
        self.add_dialog("The medicine can't kill you! The fever spikes back up...101...102...104...")
        self.add_dialog("The fever is too high to control. You did it!")
        self.add_dialog("GOTO: Victory!")
		


    def run(self):
        self.remove_all_buttons()
        self.add_dialog("You run...right into a pack of white blood cells.")
        self.add_dialog("Why do they have to ruin everything?")
        self.add_dialog("As the medicine kills your whole population, you face your fate with the blood cells. This is the end for you.")
        self.goto_scene(Scene_Game_Over)