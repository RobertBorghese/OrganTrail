from scenes.scene_base import Scene_Base

class Scene_Game_Over(Scene_Base):
	def setup(self):
		GAME_WIDTH = self.window.game_width
		GAME_HEIGHT = self.window.game_height
		self.set_background("images/Background1.png")
		self.show_text(GAME_WIDTH / 4, GAME_HEIGHT / 3, GAME_WIDTH / 2, "Game Over!", 50)
		self.add_dialog("Thanks for playing!")
		self.close_game()