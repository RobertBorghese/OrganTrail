#Shash
from scenes.scene_base import Scene_Base
from scenes.scene_game_over import Scene_Game_Over
from scenes.main_game.scene_stomach import Scene_Stomach

class Scene_Anitibodies(Scene_Base):
    def setup(self):
        '''
        self.set_value("vaxx", False)
        self.set_value("entry", 0)
        self.set_value("pathogen", 1)
        '''
        #only jelly belly goes here
        self.show_picture("images/jellyBelly_0.png", 700, 30, 30)
        self.play_song("audio/testmusic2.mp3")
        self.set_background("images/bloodstream.png")

        self.add_dialog("Circulation, circulation. What a fun ride.")
        self.add_dialog("The circulatory system is how things get around.")
        self.add_dialog("Red blood cells in particular carry oxygen to different parts of the body.")
        self.add_dialog("They go from the heart to large arteries, and then to smaller capillaries near different organs.")
        self.add_dialog("Once they deliver the oxygen, they exit and travel back to the heart through veins.")
        self.add_dialog("You can probably make your way to the stomach area this way.")
        self.add_dialog("Just ride this out and you'll find yourself there in no time.")
        self.add_dialog("Wait...what's this??")

        antibodies = self.show_picture("images/antibodies.png", -200, 100, 30)
        self.move_picture(antibodies, 300, 100, 30)
        self.add_dialog("A white blood cell just shot you with antibodies! If they stick to you, that means your cover is blown.")
        self.add_dialog("Oh no, here it comes...")
        self.move_picture(antibodies, 1500, 100, 30)
        #hide_picture not working, not sure what the issue is
        #self.hide_picture(antibodies)

        #fight scene
        self.set_background("images/boxing.png")
        self.play_sound("audio/danger_jingle.wav") #note: not playing at all
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
		#bug: fades away to next scene too quickly, we can't see all the text
        if self.get_value("vaxx"):
            if self.generate_random_chance(20):
                self.move_picture(self.get_value("tempPic"), 200, -20, 20)
                self.move_picture(self.get_value("tempPic"), 200, 600, 30)
                self.remove_all_buttons()
                self.add_dialog("Hit! Show 'em who's boss!")
                self.add_dialog("Better get going before more show up...")
                self.goto_scene(Scene_Stomach)
            else:
                self.remove_all_buttons()
                self.add_dialog("Your will was strong, but the blood cell was stronger...")
                
                self.goto_scene(Scene_Game_Over)
        else:
            if self.generate_random_chance(100): #change to 80 eventually
                self.remove_all_buttons()
                self.add_dialog("Hit! Show 'em who's boss!")
                self.move_picture(self.get_value("tempPic"), 200, -20, 20)
                self.move_picture(self.get_value("tempPic"), 200, 600, 30)
                self.add_dialog("Better get going before more show up...")
                self.goto_scene(Scene_Stomach)

            else:
                self.remove_all_buttons()
                self.add_dialog("Your will was strong, but the blood cell was stronger...")
                self.goto_scene(Scene_Game_Over)

    