#Shash
from scenes.scene_base import Scene_Base
from scenes.scene_game_over import Scene_Game_Over
from scenes.main_game.scene_final_blaze import Scene_Final_Blaze

class Scene_Fever(Scene_Base):
    def setup(self):
        
        #Note: This block is for testing only. Use if you are skipping straight to this scene
        self.set_value("vaxx", False)
        self.set_value("entry", 0)
        self.set_value("pathogen", 3) #change as needed
        self.set_value("player_frames", ["images/blazeDaze_0", "images/blazeDaze_1"]) #change as needed
		#temp value for player animation, will set later in enter scene
        self.set_value("player_animation", 0)
        
        GAME_WIDTH = self.window.game_width
        GAME_HEIGHT = self.window.game_height
		#load up character animation
		#character is loaded up here
        self.set_value("player_animation", self.show_picture(self.get_value("player_frames"), GAME_WIDTH/2, 30, 20))
        self.play_song("audio/testmusic2.mp3")
        self.set_background("images/bloodstream.png")

        self.add_dialog("You've established a large presence in the bloodstream now. ")
        self.add_dialog("So many white blood cells are trying to fight you, but you outnumber them.")
        self.add_dialog("They are a lot stronger, though. The fight is brutal.")
        self.add_dialog("With this much activity going on, the blood temperature is rising.")
        self.add_dialog("The rise in temperature is starting to kill a lot of you, and the morale of the blood cells is going up.")
        self.add_dialog("Uh oh, here comes one now...")

        self.set_background("images/boxing.png")

        self.set_value("wbc", self.show_picture(["images/wbc_0", "images/wbc_1", "images/wbc_2", "images/wbc_3"], -100, 0))
        self.move_picture(self.get_value("wbc"), GAME_WIDTH/32, 0, 20)
        self.play_sound("audio/danger_jingle.wav")
        self.play_song("audio/combatmusic.mp3")
		
		#player character bounce animation
        self.move_picture(self.get_value("player_animation") ,  GAME_WIDTH/2, -20, 15)
        self.move_picture(self.get_value("player_animation") ,  GAME_WIDTH/2, 30, 15)
		
        self.add_dialog("A White Blood Cell arrived!")
        
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
	
        GAME_WIDTH = self.window.game_width
        GAME_HEIGHT = self.window.game_height
		#bug: fades away to next scene too quickly, we can't see all the text
        if self.get_value("vaxx"):
            if self.generate_random_chance(20):
				#animation to attack
                self.move_picture(self.get_value("player_animation") ,  GAME_WIDTH/32, 30, 15)
                self.move_picture(self.get_value("player_animation") ,  GAME_WIDTH/2, 30, 15)
				
				#animation of WBC death
                self.move_picture(self.get_value("wbc"), GAME_WIDTH/32, -20, 20)
                self.move_picture(self.get_value("wbc"), GAME_WIDTH/32, 600, 30)
                self.remove_all_buttons()
                self.add_dialog("Hit! Show 'em who's boss!")
                self.add_dialog("Better get going before more show up...")
				
                self.goto_scene(Scene_Final_Blaze)
            else:
                self.remove_all_buttons()
				
				#wbc animation to attack
                self.move_picture(self.get_value("wbc"), GAME_WIDTH/2, 30, 20)
				
				#wbc chowing down motion
                self.move_picture(self.get_value("wbc"), GAME_WIDTH/2, 35, 10)
                self.move_picture(self.get_value("wbc"), GAME_WIDTH/2, 25, 10)
				
                self.add_dialog("Your will was strong, but the blood cell was stronger...")
                
                self.goto_scene(Scene_Game_Over)
        else:
            if self.generate_random_chance(80): #change to 80 eventually
                self.remove_all_buttons()
                
				#animation to attack
                self.move_picture(self.get_value("player_animation") ,  GAME_WIDTH/32, 30, 15)
                self.move_picture(self.get_value("player_animation") ,  GAME_WIDTH/2, 30, 15)
                self.add_dialog("Hit! Show 'em who's boss!")
				
				#animation of WBC death
                self.move_picture(self.get_value("wbc"), GAME_WIDTH/32, -20, 20)
                self.move_picture(self.get_value("wbc"), GAME_WIDTH/32, 600, 30)
                self.add_dialog("Better get going before more show up...")
				
                self.goto_scene(Scene_Final_Blaze)

            else:
                self.remove_all_buttons()
				
				#wbc animation to attack
                self.move_picture(self.get_value("wbc"), GAME_WIDTH/2, 30, 20)
				
				#wbc chowing down  motion
                self.move_picture(self.get_value("wbc"), GAME_WIDTH/2, 40, 30)
                self.move_picture(self.get_value("wbc"), GAME_WIDTH/2, 20, 30)
                self.move_picture(self.get_value("wbc"), GAME_WIDTH/2, 40, 30)
                self.move_picture(self.get_value("wbc"), GAME_WIDTH/2, 20, 30)
				
                self.add_dialog("Your will was strong, but the blood cell was stronger...")
                self.goto_scene(Scene_Game_Over)