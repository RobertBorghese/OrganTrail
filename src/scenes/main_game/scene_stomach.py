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
        GAME_WIDTH = self.window.game_width
        GAME_HEIGHT = self.window.game_height
        #only jelly belly goes here
		#set_Value provides global access to character animation
		#move character here
        self.set_value("player_animation", self.show_picture(self.get_value("player_frames"), GAME_WIDTH/2, 30, 20))
        self.play_song("audio/testmusic2.mp3")
        self.set_background("images/stomach_inside.jpg")

        self.add_dialog("You've reached the stomach! This was your destination, but your mission is far from over.")
        self.add_dialog("This is where food goes after its been chewed up.")
        self.add_dialog("Digestive enzymes and acids aid in digestion.")
        self.add_dialog("Don't worry, you're too small to be affected. Just keep moving.")
        #cell appears
        cell = self.show_picture(["images/cell_0.png", "images/cell_1.png", "images/cell_2.png"], GAME_WIDTH/64 , -10, 20)
        if self.get_value("entry") == 0:
            self.add_dialog("Ah, another vulnerable cell to infect.")
            self.add_dialog("This one is much bigger, so make more copies of yourself and start wreaking havoc. Go nuts.")
        else:
            self.add_dialog("Ah, a cell. Looks nice and peaceful.")
            self.add_dialog("Let's kill it.")
            self.add_dialog("Yep, viruses need to infect a host cell to make more copies of itself. That's how they multiply.")
            self.add_dialog("They inject their DNA into the host, and the DNA uses the host's own protein building mechanism to make more viruses.")
            self.add_dialog("Of course, this kills the host cell, but that's life.")
		
		#animation for multiplying
		#jelly belly shakes first and then multiplies
        self.move_picture(self.get_value("player_animation"), GAME_WIDTH/2 + 10 , 40, 20)
        self.move_picture(self.get_value("player_animation"), GAME_WIDTH/2 , 30, 20)
        self.move_picture(self.get_value("player_animation"), GAME_WIDTH/2 + 10, 40, 20)
        self.move_picture(self.get_value("player_animation"), GAME_WIDTH/2 , 30, 20)
        copy_1 = self.show_picture(["images/jellyBelly_0.png", "images/jellyBelly_1.png"], GAME_WIDTH/2 , 30, 20)
        copy_2 = self.show_picture(["images/jellyBelly_0.png", "images/jellyBelly_1.png"], GAME_WIDTH/2, 30, 20)
        #copy_3 = self.show_picture(["images/jellyBelly_0.png", "images/jellyBelly_1.png"], GAME_WIDTH/2, 30, 20)
        #copy_4 = self.show_picture(["images/jellyBelly_0.png", "images/jellyBelly_1.png"], GAME_WIDTH/2, 30, 20)
        self.move_picture(copy_1, GAME_WIDTH/2 - 100, -200, 30)
        self.move_picture(copy_2, GAME_WIDTH/2 - 100, 300, 30)
        #self.move_picture(copy_3, GAME_WIDTH/2 + 150, -200, 30)
        #self.move_picture(copy_4, GAME_WIDTH/2 + 150, 300, 30)
		
		#cell shaking
        self.move_picture(cell, GAME_WIDTH/64 + 30 , -10, 20)
        self.move_picture(cell, GAME_WIDTH/64 , -30, 20)
        self.move_picture(cell, GAME_WIDTH/64 + 30, -10, 20)
        self.move_picture(cell, GAME_WIDTH/64, -30, 20)
		
        #cell disappears
        self.add_dialog("Wow, there are a lot of you now. Enough for the victim to notice, I'd say.")
		
		#cell gets attacked and shakes each time
        self.move_picture(copy_1, GAME_WIDTH/32, 30, 20)
        self.move_picture(copy_1, GAME_WIDTH/2 - 100, -200, 20)
        self.move_picture(cell, GAME_WIDTH/64 + 50 , -10, 10)
        self.move_picture(cell, GAME_WIDTH/64 , -50, 10)
        self.move_picture(cell, GAME_WIDTH/64 + 50 , -10, 10)
        self.move_picture(cell, GAME_WIDTH/64, -50, 10)
		
        self.move_picture(copy_2, GAME_WIDTH/32, 30, 20)
        self.move_picture(copy_2, GAME_WIDTH/2 - 100, 300, 30)
        self.move_picture(cell, GAME_WIDTH/64 + 50 , -10, 10)
        self.move_picture(cell, GAME_WIDTH/64 , -50, 10)
        self.move_picture(cell, GAME_WIDTH/64 + 50 , -10, 10)
        self.move_picture(cell, GAME_WIDTH/64, -50, 10)

        self.move_picture(self.get_value("player_animation"), GAME_WIDTH/32 , 30, 20)
        self.move_picture(self.get_value("player_animation"), GAME_WIDTH/2 , 30, 20)
        self.move_picture(cell, GAME_WIDTH/64 + 50 , -10, 10)
        self.move_picture(cell, GAME_WIDTH/64 , -50, 10)
        self.move_picture(cell, GAME_WIDTH/64 + 50 , -10, 10)
        self.move_picture(cell, GAME_WIDTH/64, -50, 10)

        self.move_picture(cell, GAME_WIDTH/64 + 10 , 1000, 20)
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


    
