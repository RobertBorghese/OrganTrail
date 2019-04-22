#Shash
from scenes.scene_base import Scene_Base
from scenes.scene_game_over import Scene_Game_Over
from scenes.main_game.scene_final_jelly import Scene_Final_Jelly

class Scene_Intestine(Scene_Base):
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
        #only jelly belly goes here
        self.show_picture("images/jellyBelly_0.png", 700, 30, 30)
        self.play_song("audio/testmusic2.mp3")
        self.set_background("images/intestines.jpg")

        self.add_dialog("Welcome to the intestines. This is where you'll deliver the final blow!")
        self.add_dialog("Once food has been broken down enough, it comes here, where it is filtered.")
        self.add_dialog("Useful parts get absorbed into the bloodstream, and the rest just goes.")
        self.add_dialog("I'll leave that to your imagination. Just don't join the waste.")
        self.add_dialog("Now is your chance to multiply even more and disrupt the digestive system!")
        self.add_dialog("Oh come on! What's a white blood cell doing here?!")

        #fight
        self.set_background("images/boxing.png")
        self.play_sound("audio/danger_jingle.wav")
        self.set_value("tempPic", self.show_picture("images/wbc.png", -100, 0))
        self.move_picture(self.get_value("tempPic"), 200, 0, 30)
        self.add_dialog("A White Blood Cell arrived!")
        
        self.play_song("audio/combatmusic.mp3")
        
        #chance of vaccination
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

        self.wait_for_button_press()

    def fight(self):

        if self.get_value("vaxx"):
            if self.generate_random_chance(20):
                self.move_picture(self.get_value("tempPic"), 200, -20, 20)
                self.move_picture(self.get_value("tempPic"), 200, 600, 30)
                self.remove_all_buttons()
                self.add_dialog("Hit! Show 'em who's boss!")
                self.add_dialog("Better get going before more show up...")
                self.goto_scene(Scene_Final_Jelly)
            else:
                self.remove_all_buttons()
                self.add_dialog("Your will was strong, but the blood cell was stronger...")
                
                self.goto_scene(Scene_Game_Over)
        else:
            if self.generate_random_chance(80): 
                self.remove_all_buttons()
                self.add_dialog("Hit! Show 'em who's boss!")
                self.move_picture(self.get_value("tempPic"), 200, -20, 20)
                self.move_picture(self.get_value("tempPic"), 200, 600, 30)
                self.add_dialog("Better get going before more show up...")
                self.goto_scene(Scene_Final_Jelly)
            else:
                self.remove_all_buttons()
                self.add_dialog("Your will was strong, but the blood cell was stronger...")
                self.goto_scene(Scene_Game_Over)


    