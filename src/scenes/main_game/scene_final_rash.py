#Shash
from scenes.scene_base import Scene_Base
from scenes.scene_game_over import Scene_Game_Over
from scenes.scene_victory import Scene_Victory

class Scene_Final_Rash(Scene_Base):
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

        self.set_background("images/neurons.jpg")
        self.add_dialog("You've been doing some work.")
        self.add_dialog("Traveling up and down the axons of these neurons.")
        self.add_dialog("You've multiplied a whole bunch, too.")
        self.add_dialog("I'd say this is the perfect time to activate and strike!")
        self.add_dialog("Now, how should you go about this? You can gather all your copies in one spot and launch a large scale attack.")
        self.add_dialog("That will cause a giant rash to grow and will no doubt cause more infections.")
        self.add_dialog("Or, you can spread out a bit more and cause smaller rashes and sores across the body. Just as harmful, I'd say.")
        self.add_button(x = 600,
						y = 400, 
						w = 300,
						h = 40,
						name = "United we stand!",
						buttonColors = ["#7D7DB4","#64648C","252525"],
						font = ["Arial", 17, -1, False],
						action = self.unite)
        self.add_button(x = 200,
						y = 400, 
						w = 300,
						h = 40,
						name = "Divide and conquer!",
						buttonColors = ["#7D7DB4","#64648C","252525"],
						font = ["Arial", 17, -1, False],
						action = self.divide)
        self.wait_for_button_press()

    def divide(self):
        self.remove_all_buttons()
        self.add_dialog("Divide and conquer! You let your fellow viruses spread out along the body.")
        self.add_dialog("And now...you strike! Rashes and sores are breaking out everywhere!")
        self.add_dialog("So much so that no matter how much skin treatment the victim tries, there are always more of you to attack.")
        self.add_dialog("You've successfully infected the victim!")
        self.goto_scene(Scene_Victory)
		


    def unite(self):
        self.remove_all_buttons()
        self.add_dialog("United we stand! You gather all the forces here and unite them.")
        self.add_dialog("And now...you strike! Everyone concentrates on this one area, and a huge rash forms.")
        self.add_dialog("This rash is easy to infect, so other viruses and bacteria can enter through here.")
        self.add_dialog("In the 1800's, this would have meant certain death for the victim.")
        self.add_dialog("Unfortunately, the victim has some great skin ointment, and made sure to cover the rash.")
        self.add_dialog("Since you were all in one place, you all were killed by the ointment. This is the end for you.")
        self.goto_scene(Scene_Game_Over)