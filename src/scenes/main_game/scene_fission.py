#Shash

from scenes.scene_base import Scene_Base
from scenes.scene_game_over import Scene_Game_Over
from scenes.main_game.scene_anitibodies import Scene_Anitibodies

class Scene_Fission(Scene_Base):
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
        self.play_song("audio/testmusic2.mp3")
        self.set_background("images/bloodstream.png")

        GAME_WIDTH = self.window.game_width
        GAME_HEIGHT = self.window.game_height
		#only blaze goes here
		#load up character animation
		#character is loaded up here
        self.set_value("player_animation", self.show_picture(self.get_value("player_frames"), GAME_WIDTH/2, 30, 20))
        self.add_dialog("Now, you're in the perfect environment. Nothing is really bothering you yet.")
        self.add_dialog("This is the perfect time for you to start replicating.")
        self.add_dialog("You're a cell, unlike those wannabe virues. You can replicate on your own using binary fission.")
        self.add_dialog("You can grow exponentially this way.")
        self.add_dialog("It's been a few hours, and look at the size of your population! Let's follow one of you.")

        self.set_background("images/crossroad.jpg")
        self.add_dialog("Ah, the proverbial crossroads. One path will take you forward, while the other...")
        self.add_dialog("Sometimes there's a reason the road is less traveled.")
        self.add_button(x = 600,
						y = 400, 
						w = 300,
						h = 40,
						name = "Go right",
						buttonColors = ["#7D7DB4","#64648C","252525"],
						font = ["Arial", 17, -1, False],
						action = self.right)
        self.add_button(x = 200,
						y = 400, 
						w = 300,
						h = 40,
						name = "Go left",
						buttonColors = ["#7D7DB4","#64648C","252525"],
						font = ["Arial", 17, -1, False],
						action = self.left)
        self.wait_for_button_press()

    def right(self):
        self.remove_all_buttons()
        self.add_dialog("The odds were in your favor. Good work!")
        self.goto_scene(Scene_Anitibodies)

    def left(self):
        self.remove_all_buttons()
        self.add_dialog("Well...we all make bad decisions. Unfortunately this bad decision was your last.")
        self.add_dialog("This is the end for you. But hey, maybe one of your other clones might find success.")
        self.goto_scene(Scene_Game_Over)