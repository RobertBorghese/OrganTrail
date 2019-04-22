#Shash
import random

from scenes.scene_base import Scene_Base
from scenes.scene_game_over import Scene_Game_Over
from scenes.main_game.scene_stomach import Scene_Stomach
from scenes.main_game.scene_stomach_alt import Scene_Stomach_Alt

FONT = ["Arial", 18, -1, False]

class Scene_Edu_Mouth(Scene_Base):
    def setup(self):
        GAME_WIDTH = self.window.game_width
        GAME_HEIGHT = self.window.game_height
        self.play_song("audio/testmusic2.mp3")
        self.play_song("audio/testmusic2.mp3")
		
        self.set_value("player_animation", self.show_picture(self.get_value("player_frames"), GAME_WIDTH/2, 30, 20))

        self.add_dialog("The victim was enjoying a nice restaurant with some friends.")
        self.add_dialog("Unfortunately the restaurant had some health code violations that day...")
        self.add_dialog("They ate the seafood, and you went along for the ride. Open wide...")
        self.set_background("images/esophagus.jpg")
        self.add_dialog("Look at that, you've got direct access to the stomach! Down the esophagus you go!") 
        self.add_dialog("But you're a tiny pathogen. It might be dangerous to go alone.")
        self.add_dialog("You can just cling to something here and stay. After you've replicated a bit, then you can go down to the main areas.")
        self.add_button(x = 600,
						y = 400, 
						w = 300,
						h = 40,
						name = "Stay back",
						buttonColors = ["#7D7DB4","#64648C","252525"],
						font = ["Arial", 17, -1, False],
						action = self.stay)
        self.add_button(x = 200,
						y = 400, 
						w = 300,
						h = 40,
						name = "Down we go!",
						buttonColors = ["#7D7DB4","#64648C","252525"],
						font = ["Arial", 17, -1, False],
						action = self.down)
        self.wait_for_button_press()

    def stay(self):
        GAME_WIDTH = self.window.game_width
        GAME_HEIGHT = self.window.game_height
        self.remove_all_buttons()
        self.add_dialog("You decide to stay back.")
        self.add_dialog("Wait -- what's that rumbling? It feels like the air pressure just dropped...")
        self.move_picture(self.get_value("player_animation"), GAME_WIDTH/2 + 10, 30, 20)
        self.move_picture(self.get_value("player_animation"), GAME_WIDTH/2, 30, 20)
        self.move_picture(self.get_value("player_animation"), GAME_WIDTH/2 + 10, 30, 20)
        self.move_picture(self.get_value("player_animation"), GAME_WIDTH/2, 30, 20)
        self.move_picture(self.get_value("player_animation"), -500, -500, 40)
        self.add_dialog("*Ah-CHOOO!* The victim sneezed! And you went flying.")
        self.add_dialog("Well, that invasion ended as soon as it began. The victim walks away, unharmed.")
        self.add_dialog("For now, this is the end for you. But maybe you'll land on another victim to kill...")
        self.goto_scene(Scene_Game_Over)

    def down(self):
        self.remove_all_buttons()
        self.add_dialog("Down the hatch!")
        self.add_dialog("You're on your way to the stomach. Hopefully, you won't be detected for a while.")
        if self.get_value("pathogen") == 1:
            self.goto_scene(Scene_Stomach)
        else:
            self.goto_scene(Scene_Stomach_Alt)

