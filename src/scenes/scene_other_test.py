from scenes.scene_base import Scene_Base
import scenes.scene_test
import scenes.scene_game_over

class Scene_Other_Test(Scene_Base):
	def setup(self):
		self.set_background("images/Background2.jpg")
		self.play_song("audio/testmusic2.mp3")

		self.add_dialog("You're now on your epic adventure!")
		
		# Show the enemy virus
		GAME_WIDTH = self.window.game_width
		pic_id = self.show_picture(["images/p2_frame_0.png", "images/p2_frame_1.png"], -500, 30)
		self.move_picture(pic_id, (GAME_WIDTH / 2) - 250, 30, 60)

		self.add_dialog("\"Oh god, an enemy has appeared! What will happen?\" - You say.")

		if self.generate_random_chance(80):
			self.add_dialog("Before you could think, the enemy attacked!")
			self.add_dialog("You were damaged by 3.")
			self.add_dialog("It's time to run back to the beginning!")
			self.add_value("Health", -3)
			self.goto_scene(scenes.scene_test.Scene_Test)
		else:
			self.add_dialog("You courageously strike the enemy!")
			self.move_picture(pic_id, (GAME_WIDTH / 2) - 250, 1000, 60)
			self.add_dialog("You beat the evil enemy! :D")
			self.goto_scene(scenes.scene_game_over.Scene_Game_Over)