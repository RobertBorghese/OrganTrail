from scenes.scene_base import Scene_Base
#from scenes.scene_titlescreen import Scene_TitleScreen

class Scene_Game_Over(Scene_Base):
	def setup(self):
		GAME_WIDTH = self.window.game_width
		GAME_HEIGHT = self.window.game_height
		self.set_background("images/Background1.png")
		self.play_song("audio/gameover.mp3")
		self.show_text(GAME_WIDTH / 4, GAME_HEIGHT / 3, GAME_WIDTH / 2, "Game Over!", 50)
		self.add_dialog("Not all pathogens can succeed. Oh well, better luck next time.")
		self.add_dialog("Thanks for playing!")
		
		self.add_button(x = 400,
						y = 400, 
						w = 300,
						h = 40,
						name = "Quit",
						buttonColors = ["#7D7DB4","#64648C","252525"],
						font = ["Arial", 18, -1, False],
						action = self.close)
	def close(self):
		self.close_game()
