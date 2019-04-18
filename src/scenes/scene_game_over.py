from scenes.scene_base import Scene_Base
import scenes.scene_titlescreen 

class Scene_Game_Over(Scene_Base):
	def setup(self):
		GAME_WIDTH = self.window.game_width
		GAME_HEIGHT = self.window.game_height

		#self.set_value("pathogen", 2)

		self.set_background("images/Background2.jpg")
		self.play_song("audio/gameover.mp3")
		#self.show_text(GAME_WIDTH / 4, GAME_HEIGHT / 20, GAME_WIDTH / 2, "Game Over!", 50)

		if self.get_value("pathogen") == 1:
			self.show_picture(["images/jellyBelly_0.png", "images/jellyBelly_1.png"], GAME_WIDTH / 4, 30, 30)
		elif self.get_value("pathogen") == 2:
			self.show_picture(["images/rashCrash_0.png", "images/rashCrash_1.png"], GAME_WIDTH / 4, 30, 30)
		else:
			self.show_picture(["images/blazeDaze_0.png", "images/blazeDaze_1.png"], GAME_WIDTH / 4, 30, 30)

		game_over_images = [
			"images/gameOverV2_0",
			"images/gameOverV2_1",
			"images/gameOverV2_2",
			"images/gameOverV2_3"
		]
		title_id = self.show_picture(game_over_images, GAME_WIDTH / 4, 5, 20)

		self.add_dialog("Not all pathogens can succeed. Oh well, better luck next time.")
		self.add_dialog("Thanks for playing!")
		
		self.add_button(x = 200,
						y = 400, 
						w = 300,
						h = 40,
						name = "Quit",
						buttonColors = ["#7D7DB4","#64648C","252525"],
						font = ["Arial", 18, -1, False],
						action = self.close)
		
		self.add_button(x = 600,
						y = 400, 
						w = 300,
						h = 40,
						name = "Back to Main",
						buttonColors = ["#7D7DB4","#64648C","252525"],
						font = ["Arial", 18, -1, False],
						action = self.title)
		
	def close(self):
		self.close_game()

	def title(self):
		self.goto_scene(scenes.scene_titlescreen.Scene_TitleScreen)
