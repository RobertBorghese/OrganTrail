from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtWidgets import QApplication, QDialog, QGraphicsView, QGraphicsScene, QGraphicsRectItem, QVBoxLayout, QSlider, QLabel, QGroupBox

from audio.audio_player import AudioPlayer

class Settings_Dialog(QDialog):
	def __init__(self, parent):
		super().__init__(parent, self.get_flags())
		self.setup_window()
		self.setup_settings()

	def get_flags(self):
		return (Qt.Dialog 
				| Qt.CustomizeWindowHint 
				| Qt.MSWindowsFixedSizeDialogHint
				| Qt.WindowSystemMenuHint 
				| Qt.WindowCloseButtonHint 
				| Qt.WindowTitleHint)

	def setup_window(self):
		self.setWindowTitle('Game Settings')
		self.resize(200, 60)

	def setup_settings(self):
		main_layout = QVBoxLayout(self)
		main_layout.setContentsMargins(12, 12, 12, 12)

		self.group = QGroupBox(self)
		self.group.setTitle('Settings')
		main_layout.addWidget(self.group)

		layout = QVBoxLayout(self.group)
		layout.setContentsMargins(12, 12, 12, 12)
		self.group.setLayout(layout)

		self.label = QLabel("Music Volume", self)
		layout.addWidget(self.label)

		self.slider = QSlider(self)
		self.slider.setMouseTracking(True)
		self.slider.valueChanged.connect(self.on_value_music_changed)
		self.slider.setOrientation(Qt.Horizontal)
		self.slider.setValue(AudioPlayer.get_music_volume())
		layout.addWidget(self.slider)

		self.se_label = QLabel("Sound Effect Volume", self)
		layout.addWidget(self.se_label)

		self.se_slider = QSlider(self)
		self.se_slider.setMouseTracking(True)
		self.se_slider.valueChanged.connect(self.on_se_value_changed)
		self.se_slider.setOrientation(Qt.Horizontal)
		self.se_slider.setValue(AudioPlayer.get_se_volume())
		layout.addWidget(self.se_slider)

	def on_value_music_changed(self, val):
		AudioPlayer.set_music_volume(val)

	def on_se_value_changed(self, val):
		AudioPlayer.set_se_volume(val)
