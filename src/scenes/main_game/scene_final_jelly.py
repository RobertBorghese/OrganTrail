#Shash
from scenes.scene_base import Scene_Base
from scenes.scene_game_over import Scene_Game_Over
from scenes.scene_victory import Scene_Victory

class Scene_Final_Jelly(Scene_Base):
    def setup(self):
        '''
        #Note: This block is for testing only. Use if you are skipping straight to this scene
        self.set_value("vaxx", False)
        self.set_value("entry", 0)
        self.set_value("pathogen", 1) #change as needed
        self.set_value("player_frames", ["images/jelyBelly_0", "images/jellyBelly_1"]) #change as needed
		#temp value for player animation, will set later in enter scene
        self.set_value("player_animation", 0)
        '''
        GAME_WIDTH = self.window.game_width
        GAME_HEIGHT = self.window.game_height
        #only jelly belly goes here
		#move character here
        self.set_value("player_animation", self.show_picture(self.get_value("player_frames"), GAME_WIDTH/2, 30, 20))
        self.play_song("audio/testmusic2.mp3")
        self.set_background("images/intestines.jpg")

        self.add_dialog("It's been a few hours, and you've been going to town in the intestines.")
        self.add_dialog("The victim has definitely noticed by now.")
        self.add_dialog("So many immune cells are fighting you and your copies.")
        self.add_dialog("As a result, the victim is feeling lots of pain. Great work!")
        #cell appears
        self.add_dialog("Oh, but that means the victim will eat some medicine. That's not good.")
        self.add_dialog("You can keep running along the intestines, doing as much damage as possible. But that medicine will eventually catch up.")
        #cell disappears
        self.add_dialog("You could also go back to the stomach, maybe recruit some of your copies there...")
        self.add_button(x = 600,
						y = 400, 
						w = 300,
						h = 40,
						name = "Keep moving",
						buttonColors = ["#7D7DB4","#64648C","252525"],
						font = ["Arial", 17, -1, False],
						action = self.keep_moving)
        self.add_button(x = 200,
						y = 400, 
						w = 300,
						h = 40,
						name = "Back to the stomach",
						buttonColors = ["#7D7DB4","#64648C","252525"],
						font = ["Arial", 17, -1, False],
						action = self.back_to_stomach)
        self.wait_for_button_press()

    def keep_moving(self):
        self.remove_all_buttons()
        self.add_dialog("You decide to keep moving forward.")
        self.add_dialog("You did a lot more damage, but that medicine came.")
        self.add_dialog("And it came down hard.")
        self.add_dialog("This is the end for you. But hey, props for causing such an inconvenience for the victim!")
        self.goto_scene(Scene_Game_Over)


    def back_to_stomach(self):
        self.remove_all_buttons()
        GAME_WIDTH = self.window.game_width
        GAME_HEIGHT = self.window.game_height
        self.set_background("images/stomach_inside.jpg")
        copy_1 = self.show_picture(self.get_value("player_frames"), GAME_WIDTH/2 - 100, -200, 30)
        copy_2 = self.show_picture(self.get_value("player_frames"), GAME_WIDTH/2 - 200, 300, 30)
        copy_3 = self.show_picture(self.get_value("player_frames"), 100, -100, 30)
        copy_4 = self.show_picture(self.get_value("player_frames"), 50, 200, 30)
        copy_5 = self.show_picture(self.get_value("player_frames"), GAME_WIDTH/2 - 300, 30, 30)
        copy_6 = self.show_picture(self.get_value("player_frames"), -200, 30, 30)
        self.add_dialog("Back to the stomach! Wow, there are a lot of you here.")
        self.add_dialog("You keep bumping into your copies. Careful, some of your DNA might get mixed up!")
        self.add_dialog("Wait, what's this? You're...mutating!")
        self.add_dialog("You've mutated! Look at that! Now you can resist the medicine that's coming down!")
        self.add_dialog("And now...make more copies of your mutated self! This is perfect!")
        self.add_dialog("Soon, the victim will start feeling even more pain.")
        self.add_dialog("And they will probably die of...dare I say...")
        self.add_dialog("DYSENTERY!!")
        self.goto_scene(Scene_Victory)


    
