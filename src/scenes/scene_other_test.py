from scenes.scene_base import Scene_Base
import scenes.scene_test

class Scene_Other_Test(Scene_Base):
	def setup(self):
		self.set_background("images/Background2.jpg")

		self.add_dialog("We are now in the second scene called Scene_Other_Test!")
		self.add_dialog("We're now gonna return to the original scene!")

		self.goto_scene(scenes.scene_test.Scene_Test)