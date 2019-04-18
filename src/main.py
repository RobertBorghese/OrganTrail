import sys

from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtWidgets import QApplication, QWidget, QGraphicsView, QGraphicsScene, QGraphicsRectItem, QVBoxLayout

from scenes.scene_titlescreen import Scene_TitleScreen
from scenes.scene_game_over import Scene_Game_Over
from scenes.main_game.scene_bacteria import Scene_Bacteria
from scenes.main_game.scene_stomach import Scene_Stomach
from audio.audio_player import AudioPlayer

# Set this to the first scene of the game
#FIRST_SCENE = Scene_TitleScreen
FIRST_SCENE = Scene_Stomach

# Set this to the screen width and height
RESOLUTION_WIDTH = 1108
RESOLUTION_HEIGHT = 624

BUTTON_PRESS_SOUND_EFFECT = "audio/se_button_click.wav"

class MyWindow(QWidget):
	def __init__(self):
		super().__init__(None, self.get_flags())
		self.game_width = RESOLUTION_WIDTH
		self.game_height = RESOLUTION_HEIGHT
		self.setup_window()
		self.setup_game_view()
		self.setup_game_scene()
		AudioPlayer.preload_sound_effect("audio/danger_jingle.mp3")

	def get_flags(self):
		return (Qt.Dialog 
				| Qt.CustomizeWindowHint 
				| Qt.MSWindowsFixedSizeDialogHint
				| Qt.WindowSystemMenuHint 
				| Qt.WindowCloseButtonHint 
				| Qt.WindowTitleHint
				| Qt.WindowMinimizeButtonHint)

	def setup_window(self):
		self.setWindowTitle('Organ Trail')
		self.resize(self.game_width, self.game_height)
		self.setMinimumSize(self.width() / 2, self.height() / 2)

	def setup_game_view(self):
		layout = QVBoxLayout(self)
		self.view = QGraphicsView(self)
		self.view.setStyleSheet("QGraphicsView { border: none; }")
		self.view.setMouseTracking(True)
		layout.addWidget(self.view)
		layout.setContentsMargins(0, 0, 0, 0)

	def setup_game_scene(self):
		self.goto_scene(FIRST_SCENE)
		self.startTimer(10)

	def goto_scene(self, scene):
		self.view.setScene(scene(self))

	def close_game(self):
		self.close()

	def resizeEvent(self, event):
		pass

	def timerEvent(self, event):
		if self.view is not None and self.view.scene() is not None:
			self.view.scene().update()

def main():
	app = QApplication(sys.argv)
	w = MyWindow()
	w.show()
	sys.exit(app.exec_())

if __name__ == '__main__':
	main()
	