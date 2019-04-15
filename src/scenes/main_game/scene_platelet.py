#Shash

from scenes.scene_base import Scene_Base
from scenes.scene_game_over import Scene_Game_Over
from scenes.main_game.scene_bacteria import Scene_Bacteria

class Scene_Platelet(Scene_Base):
    def setup(self):
        self.play_song("audio/testmusic2.mp3")
        self.set_background("images/bloodstream.png")

        self.add_dialog("Look at that, it's the platelets!")
        self.add_dialog("They always gather at a damaged blood vessel to fix it.")
        self.add_dialog("They produce a substance called fibrin, which patches up the leak.")
        self.add_dialog("Blood cells get caught in the fibrin and eventually plug the hole completely.")
        self.add_dialog("Yep, the body uses its own blood cells to repair damage.")
        self.add_dialog("Pretty oppressive, if you ask me.")
        self.add_dialog("But what do I know, I'm just a text box.")
        self.add_dialog("Anyway, it might be fun to take a closer look...")
        self.add_button(x = 600,
						y = 400, 
						w = 300,
						h = 40,
						name = "Take a closer look",
						buttonColors = ["#7D7DB4","#64648C","252525"],
						font = ["Arial", 17, -1, False],
						action = self.look)
        self.add_button(x = 200,
						y = 400, 
						w = 300,
						h = 40,
						name = "Keep going upstream",
						buttonColors = ["#7D7DB4","#64648C","252525"],
						font = ["Arial", 17, -1, False],
						action = self.move)
    def look(self):
        self.add_dialog("Uh oh! You got caught in the fibrin, and got crushed in the chaos!")
        self.add_dialog("Uh oh! You got caught in the fibrin, and got crushed in the chaos!")
        self.add_dialog("Too bad, that's the end for you.")
        self.goto_scene(Scene_Game_Over)

    def move(self):
        self.add_dialog("You keep moving upstream, ignoring the chaos at the platelets.")
        self.add_dialog("You keep moving upstream, ignoring the chaos at the platelets.")
        self.add_dialog("Good choice, you would've gotten caught in the fibrin otherwise, and that would've been the end.")
        if self.get_value("pathogen") == 1 or self.get_value("pathogen") == 2:
            self.goto_scene(Scene_Bacteria)
        else:
            self.add_dialog("Todo: bacteria character path")
