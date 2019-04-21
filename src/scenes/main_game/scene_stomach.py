#Shash
from scenes.scene_base import Scene_Base
from scenes.scene_game_over import Scene_Game_Over
from scenes.main_game.scene_intestine import Scene_Intestine

class Scene_Stomach(Scene_Base):
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
        self.set_background("images/stomach_inside.jpg")

        self.add_dialog("You've reached the stomach! This was your destination, but your mission is far from over.")
        self.add_dialog("This is where food goes after its been chewed up.")
        self.add_dialog("Digestive enzymes and acids aid in digestion.")
        self.add_dialog("Don't worry, you're too small to be affected. Just keep moving.")
        #cell appears
        self.add_dialog("Ah, another vulnerable cell to infect.")
        self.add_dialog("This one is much bigger, so make more copies of yourself and start wreaking havoc. Go nuts.")
        #cell disappears
        self.add_dialog("Wow, there are a lot of you now. Enough for the victim to notice, I'd say.")
        self.add_dialog("You can stick around if you want. Try and do some more damage here. Or, you can keep going towards the intestines, where you'll really shine.")
        self.add_button(x = 600,
						y = 400, 
						w = 300,
						h = 40,
						name = "Stay in the stomach",
						buttonColors = ["#7D7DB4","#64648C","252525"],
						font = ["Arial", 17, -1, False],
						action = self.stomach)
        self.add_button(x = 200,
						y = 400, 
						w = 300,
						h = 40,
						name = "Go to the intestines",
						buttonColors = ["#7D7DB4","#64648C","252525"],
						font = ["Arial", 17, -1, False],
						action = self.intestine)
        self.wait_for_button_press()

    def stomach(self):
        self.remove_all_buttons()
        self.add_dialog("You decide to stay here. It's not a bad place, really.")
        self.add_dialog("Unfortunately, the victim happened to be near a drug store.")
        self.add_dialog("They ate a pill, and it came down with a vengeance.")
        self.add_dialog("This is the end for you. But hey, maybe one of your other clones might have success?")
        self.goto_scene(Scene_Game_Over)


    def intestine(self):
        self.remove_all_buttons()
        self.add_dialog("You decide to keep moving. On to the intestines!")
        self.add_dialog("You did less damage to the stomach by moving, so you were undetected.")
        self.goto_scene(Scene_Intestine)


    