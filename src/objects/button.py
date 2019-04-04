from PyQt5.QtCore import QRectF
from PyQt5.QtWidgets import QGraphicsItem, QGraphicsDropShadowEffect
from PyQt5.QtGui import QPixmap, QFont, QColor, QLinearGradient, QPainter, QPen, QPainterPath

from audio.audio_player import AudioPlayer

# The sound effect that is played when a button is pressed
BUTTON_PRESS_SOUND_EFFECT = "audio/se_button_click.wav"

class Button(QGraphicsItem):
	def __init__(self, parentScene, width, height, text, font, buttonColors, textColors, callback):
		super().__init__()
		self.scene = parentScene
		self.width = width
		self.height = height
		self.isPressed = False
		self.text = text
		self.callback = callback

		if font != None:
			self.font = QFont(font[0], font[1], font[2], font[3])
		else:
			self.font = QFont()

		if buttonColors != None:
			self.buttonColors = [QColor(buttonColors[0]),QColor(buttonColors[1]),QColor(buttonColors[2])]
		else:
			self.buttonColors = [QColor(125,125,180),QColor(100,100,140),QColor(25,25,25)]

		if textColors != None:
			self.textColors = [QColor(textColors[0]), QColor(textColors[1])]
		else:
			self.textColors = [QColor(255,255,255), QColor(0,0,0)]

		self.add_shadow()

		AudioPlayer.preload_sound_effect(BUTTON_PRESS_SOUND_EFFECT)

	def add_shadow(self):
		self.shadow = QGraphicsDropShadowEffect()
		self.shadow.setOffset(3, 3)
		self.shadow.setColor(QColor(0, 0, 0))
		self.setGraphicsEffect(self.shadow)

	def boundingRect(self):
		return QRectF(0, 0, self.width, self.height)

	def mousePressEvent(self, event):
		self.isPressed = True
		self.shadow.setColor(QColor(0, 0, 0, 0))
		self.update()
		if len(BUTTON_PRESS_SOUND_EFFECT) > 0:
			AudioPlayer.play_sound_effect(BUTTON_PRESS_SOUND_EFFECT)

	def mouseReleaseEvent(self, event):
		self.isPressed = False
		self.shadow.setColor(QColor(0, 0, 0))
		if self.callback != None:
			self.callback()
			self.scene.call_next_action()
		self.update()

	def paint(self, painter, option, widget):
		if self.isPressed:
			painter.translate(3, 3)

		# Gradient
		gradient = QLinearGradient(0, 0, 0, self.height)
		gradient.setColorAt(0, self.buttonColors[0])
		gradient.setColorAt(1, self.buttonColors[1])

		# Button Background
		painter.setRenderHint(QPainter.Antialiasing)
		painter.setFont(self.font)
		painter.setPen(self.buttonColors[2])
		painter.setBrush(gradient)
		painter.drawRoundedRect(0, 0, self.width, self.height, 10, 10)

		# Button Text
		painter.setPen(QColor(0, 0, 0))
		painter.drawText(QRectF(2, 2, self.width, self.height), 0x84, self.text)
		painter.setPen(QColor(255, 255, 255))
		painter.drawText(QRectF(0, 0, self.width, self.height), 0x84, self.text)









