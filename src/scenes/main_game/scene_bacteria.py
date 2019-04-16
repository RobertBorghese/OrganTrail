#Shash
from scenes.scene_base import Scene_Base
from scenes.scene_game_over import Scene_Game_Over

class Scene_Bacteria(Scene_Base):
    def setup(self):
        self.play_song("audio/testmusic2.mp3")
        self.set_background("images/bloodstream.png")
        self.show_picture("images/bacteria.png", 200, 0)
        self.add_dialog("TBC")