#Shash
from scenes.scene_base import Scene_Base
from scenes.scene_game_over import Scene_Game_Over
from scenes.main_game.scene_anitibodies import Scene_Anitibodies

class Scene_Bacteria(Scene_Base):
    def setup(self):
        '''
        self.set_value("vaxx", False)
        self.set_value("entry", 0)
        self.set_value("pathogen", 1)
        '''
        #only viruses go here
        if self.get_value("pathogen") == 1:
            self.show_picture("images/jellyBelly_0.png", 700, 30, 30)
        elif self.get_value("pathogen") == 2:
            self.show_picture("images/rashCrash_0.png", 700, 30, 30)
        
        self.play_song("audio/testmusic2.mp3")
        self.set_background("images/bloodstream.png")
        #todo: find a better pic of bacteria with a face
        #self.show_picture("images/bacteria.png", 200, 0)
        self.add_dialog("Hey, it's a bacteria cell.")
        self.add_dialog("Despite their reputation, not all of them are out to infect and kill people.")
        self.add_dialog("This one seems like it's pretty harmless. It might even be helpful to the host.")
        self.add_dialog("Let's kill it.")
        self.add_dialog("Yep, viruses need to infect a host cell to make more copies of itself. That's how they multiply.")
        self.add_dialog("They inject their DNA into the host, and the DNA uses the host's own protein building mechanism to make more viruses.")
        self.add_dialog("Of course, this kills the host cell, but that's life.")
        self.add_dialog("Although, if you infect a bigger cell, you can make even more copies of yourself. Decisions...")
        self.add_button(x = 600,
						y = 400, 
						w = 300,
						h = 40,
						name = "Infect the bacteria cell",
						buttonColors = ["#7D7DB4","#64648C","252525"],
						font = ["Arial", 17, -1, False],
						action = self.infect)
        self.add_button(x = 200,
						y = 400, 
						w = 300,
						h = 40,
						name = "Wait for a larger cell",
						buttonColors = ["#7D7DB4","#64648C","252525"],
						font = ["Arial", 17, -1, False],
						action = self.greedy)
        self.wait_for_button_press()

    def infect(self):
        self.remove_all_buttons()
        self.add_dialog("You infected the bacteria cell. Good choice.")
        self.add_dialog("Don't let chances like this pass you by in the hopes that something better might come along.")
        self.add_dialog("Just some life advice from your friend, the text box.")
        self.add_dialog("Now there are over 100 of you! They're going in every direction. We'll follow one of you the rest of the way")
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


    def greedy(self):
        self.remove_all_buttons()
        self.add_dialog("You waited for a bigger cell.")
        self.add_dialog("Unfortunately, a group of white blood cells took that opportunity and ganged up.")
        self.add_dialog("You never stood a chance. That's the end for you.")
        self.goto_scene(Scene_Game_Over)

    def left(self):
        self.remove_all_buttons()
        self.add_dialog("The odds were in your favor. Good work!")
        if self.get_value("pathogen") == 1:
            self.goto_scene(Scene_Anitibodies)
        else:
            self.add_dialog("Goto next Rash Crash scene")

    def right(self):
        self.remove_all_buttons()
        self.add_dialog("Well...we all make bad decisions. Unfortunately this bad decision was your last.")
        self.add_dialog("This is the end for you. But hey, maybe one of your other clones might have success?")
        self.goto_scene(Scene_Game_Over)