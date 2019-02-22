from PyQt5.QtWidgets import QGraphicsScene, QGraphicsTextItem, QGraphicsPixmapItem, QGraphicsRectItem
from PyQt5.QtGui import QPixmap, QFont, QColor

from audio.audio_player import AudioPlayer

class Scene_Base(QGraphicsScene):
	def __init__(self, window):
		super().__init__()
		self.setSceneRect(0, 0, window.game_width, window.game_height)
		self.window = window
		self.init_fields()
		self.create_fade()
		self.setup()

	def init_fields(self):
		self.actions = []
		self.current_action = -1
		self.dialog_box = None
		self.target_text = None
		self.current_dialog_text = None
		self.current_dialog_text_offset = 0
		self.background = None
		self.fading_box = None
		self.fade_dir = 0
		self.next_scene = None

	def create_fade(self, opc=1):
		self.fading_box = QGraphicsRectItem(0, 0, self.width(), self.height())
		self.fading_box.setBrush(QColor(0, 0, 0))
		self.fading_box.setOpacity(opc)
		self.addItem(self.fading_box)

	# ==============================================
	# * Setup
	#
	# Overwrite with child classes to add actions.
	# ==============================================

	def setup(self):
		pass

	# ==============================================
	# * Update
	#
	# Updates the scene. Handles input, waiting, etc.
	# ==============================================

	def update(self):
		self.update_fade()
		self.update_dialog()
		self.update_dialog_text()

	def update_fade(self):
		if self.fading_box is not None:
			if self.fade_dir == 0 and self.fading_box.opacity() > 0:
				self.fading_box.setOpacity(self.fading_box.opacity() - 0.02)
				if self.fading_box.opacity() <= 0:
					self.removeItem(self.fading_box)
					self.fading_box = None
			elif self.fade_dir == 1 and self.fading_box.opacity() < 1:
				self.fading_box.setOpacity(self.fading_box.opacity() + 0.02)
				if self.fading_box.opacity() >= 1:
					if self.next_scene is not None:
						self.window.goto_scene(self.next_scene)
					else:
						self.actually_close_game()

	def update_dialog(self):
		if self.dialog_box is not None:
			if self.dialog_box.opacity() < 0.5:
				self.dialog_box.setOpacity(self.dialog_box.opacity() + 0.04)
				if self.dialog_box.opacity() >= 0.5:
					self.dialog_box.setOpacity(0.5)
					self.actually_show_dialog(self.actions[0])

	def update_dialog_text(self):
		if self.current_dialog_text is not None:
			curr_text = self.current_dialog_text.toPlainText()
			if curr_text != self.target_text:
				if self.current_dialog_text_offset < 3:
					self.current_dialog_text_offset += 1
				else:
					self.current_dialog_text_offset = 0
					self.current_dialog_text.setPlainText(self.target_text[:len(curr_text) + 1])

	# ==============================================
	# * Mouse Events
	#
	# Handle mouse input.
	# ==============================================

	def mouseMoveEvent(self, mouseEvent):
		pass
		#print(mouseEvent.pos())

	def mousePressEvent(self, mouseEvent):
		self.when_mouse_pressed(mouseEvent)

	def mouseDoubleClickEvent(self, mouseEvent):
		self.when_mouse_pressed(mouseEvent)

	def when_mouse_pressed(self, mouseEvent):
		if self.current_action == 0 and mouseEvent.button() == 1:
			if self.current_dialog_text is not None:
				if self.current_dialog_text.toPlainText() != self.target_text:
					self.current_dialog_text.setPlainText(self.target_text)
				else:
					self.removeItem(self.current_dialog_text)
					self.call_next_action()

	# ==============================================
	# * Action Management
	# ==============================================

	def finish_action(self):
		self.actions.pop(0)

	def check_if_first(self):
		if len(self.actions) == 1:
			self.perform_next_action()

	def perform_next_action(self):
		if len(self.actions) > 0:
			action = self.actions[0]
			self.current_action = action_type = action[0]

			if action_type is 0:
				self.actually_show_dialog(action)
			elif action_type is 2:
				self.actually_set_background(action)
			elif action_type is 3:
				self.actually_goto_scene(action)
			elif action_type is 4:
				self.actually_close_game()
			elif action_type is 5:
				self.actually_play_song(action)

	def call_next_action(self):
		self.finish_action()
		self.perform_next_action()

	# ==============================================
	# * Actual Implementations
	# ==============================================

	def actually_show_dialog(self, data):
		if self.dialog_box is None:
			self.create_dialog_box()
		else:
			self.current_dialog_text = QGraphicsTextItem()
			self.current_dialog_text.setZValue(1)
			self.current_dialog_text.setDefaultTextColor(QColor(255, 255, 255))

			temp_font = self.current_dialog_text.font()
			temp_font.setPointSize(data[2])
			self.current_dialog_text.setFont(temp_font)

			self.addItem(self.current_dialog_text)
			self.current_dialog_text.setX(self.dialog_box.x() + 10)
			self.current_dialog_text.setY(self.dialog_box.y() + 10)
			self.current_dialog_text.setTextWidth(self.dialog_box.boundingRect().width() - 20)

			self.target_text = data[1]
			self.current_dialog_text_offset = 0

	def create_dialog_box(self):
		self.dialog_box = QGraphicsRectItem(0, 0, self.width() - 20, self.height() / 4)
		self.dialog_box.setBrush(QColor(0, 0, 0))
		self.dialog_box.setX(10)
		self.dialog_box.setY(self.height() - self.dialog_box.boundingRect().height() - 10)
		self.dialog_box.setOpacity(0)
		self.addItem(self.dialog_box)

	def actually_set_background(self, data):
		if self.background is not None:
			self.removeItem(self.background)
			self.background = None

		self.background = QGraphicsPixmapItem(QPixmap(data[1]).scaled(self.window.game_width, self.window.game_height))
		self.background.setZValue(-1)
		self.addItem(self.background)
		self.call_next_action()

	def actually_goto_scene(self, data):
		self.next_scene = data[1]
		self.fade_dir = 1
		self.create_fade(0)

	def actually_close_game(self):
		self.window.close_game()

	def actually_play_song(self, data):
		AudioPlayer.play_song(data[1])
		self.call_next_action()

	# ==============================================
	# * Setup Calls
	# ==============================================

	def add_call(self, data):
		self.actions.append(data)
		self.check_if_first()

	def add_dialog(self, msg, fontSize=20):
		self.add_call([0, msg, fontSize])

	def add_button(self, name, action):
		self.add_call([1, name, action])

	def set_background(self, path):
		self.add_call([2, path])

	def goto_scene(self, scene):
		self.add_call([3, scene])

	def close_game(self):
		self.add_call([4])

	def play_song(self, path):
		self.add_call([5, path])