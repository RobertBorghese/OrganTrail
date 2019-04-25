from PyQt5.QtCore import Qt, QUrl, QSize
from PyQt5.QtWidgets import QApplication, QDialog, QGraphicsView, QGraphicsScene, QGraphicsRectItem, QVBoxLayout, QSlider, QLabel, QGroupBox, QCheckBox, QFrame, QSpacerItem, QWidget
from PyQt5.QtGui import QResizeEvent

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
		layout.setSpacing(12);
		self.group.setLayout(layout)

		self.fullscreen = QCheckBox("Use Fullscreen", self)
		self.fullscreen.setChecked(self.parentWidget().windowState() == (Qt.WindowFullScreen))
		layout.addWidget(self.fullscreen)

		line = QFrame(self);
		line.setFrameShape(QFrame.HLine);
		line.setFrameShadow(QFrame.Sunken);
		layout.addWidget(line)

		temp = QWidget(self.group)
		layout.addWidget(temp)
		slider_layout1 = QVBoxLayout(temp)
		self.label = QLabel("Music Volume", self)
		slider_layout1.addWidget(self.label)

		self.slider = QSlider(self)
		self.slider.setMouseTracking(True)
		self.slider.valueChanged.connect(self.on_value_music_changed)
		self.slider.setOrientation(Qt.Horizontal)
		self.slider.setValue(AudioPlayer.get_music_volume())
		slider_layout1.addWidget(self.slider)

		line2 = QFrame(self);
		line2.setFrameShape(QFrame.HLine);
		line2.setFrameShadow(QFrame.Sunken);
		layout.addWidget(line2)

		temp2 = QWidget(self.group)
		layout.addWidget(temp2)
		slider_layout2 = QVBoxLayout(temp2)
		self.se_label = QLabel("Sound Effect Volume", self)
		slider_layout2.addWidget(self.se_label)

		self.se_slider = QSlider(self)
		self.se_slider.setMouseTracking(True)
		self.se_slider.valueChanged.connect(self.on_se_value_changed)
		self.se_slider.setOrientation(Qt.Horizontal)
		self.se_slider.setValue(AudioPlayer.get_se_volume())
		slider_layout2.addWidget(self.se_slider)

	def on_value_music_changed(self, val):
		AudioPlayer.set_music_volume(val)

	def on_se_value_changed(self, val):
		AudioPlayer.set_se_volume(val)

	def closeEvent(self, event):
		if self.fullscreen.isChecked():
			self.parentWidget().setWindowState(Qt.WindowFullScreen)
		else:
			self.parentWidget().setWindowState(Qt.WindowNoState)
		self.parentWidget().resizeEvent(QResizeEvent(self.parentWidget().size(), QSize(0, 0)))
		event.accept()
