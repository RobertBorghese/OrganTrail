from PyQt5.QtWidgets import QGraphicsScene, QGraphicsTextItem, QGraphicsPixmapItem, QGraphicsRectItem
from PyQt5.QtGui import QPixmap, QFont, QColor

from audio.audio_player import AudioPlayer
from objects.button import Button

import random

class Scene_Base(QGraphicsScene):
	def __init__(self, window):
		super().__init__()
		self.setSceneRect(0, 0, window.game_width, window.game_height)
		self.window = window
		self.init_fields()
		self.create_fade()
		self.dialog_box = None
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
		self.buttons = []
		self.current_id = 1
		self.texts = {}
		self.images = {}
		self.moving_images = []
		self.updatable_images = []
		self.vaxx = None
		self.entry = None

	def create_fade(self, opc=1):
		self.fading_box = QGraphicsRectItem(0, 0, self.width(), self.height())
		self.fading_box.setBrush(QColor(0, 0, 0))
		self.fading_box.setOpacity(opc)
		self.fading_box.setZValue(100)
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
		self.update_moving_images()
		self.update_animated_images()

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
					if self.actions[0][0] == 0:
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

	def update_moving_images(self):
		if len(self.moving_images) > 0:
			index = 0
			new_data = []
			for image in self.moving_images:
				pic_id = image[0]
				item = self.images[pic_id]
				item.setX(item.x() + image[1])
				item.setY(item.y() + image[2])
				image[3] -= 1
				if image[3] > 0:
					new_data.append(image)
				elif image[4] is not None:
					image[4]()
				index += 1

			self.moving_images = new_data

	def update_animated_images(self):
		if len(self.updatable_images) > 0:
			index = 0
			for image in self.updatable_images:
				image[2] += 1
				if image[2] > image[4]:
					image[2] = 0
					image[3] += 1
					if image[3] >= len(image[1]):
						image[3] = 0
					image[0].setPixmap(QPixmap(image[1][image[3]]))


	# ==============================================
	# * Mouse Events
	#
	# Handle mouse input.
	# ==============================================

	def mouseMoveEvent(self, mouseEvent):
		pass

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
		else:
			super(Scene_Base, self).mousePressEvent(mouseEvent)

	# ==============================================
	# * Action Management
	# ==============================================

	def finish_action(self):
		if len(self.actions) > 0:
			self.actions.pop(0)
		else:
			self.wait_for_button_press()

	def check_if_first(self):
		if len(self.actions) == 1:
			self.perform_next_action()

	def perform_next_action(self):
		if len(self.actions) > 0:
			action = self.actions[0]
			self.current_action = action_type = action[0]

			if action_type is -1:
				self.actually_hide_dialog_box()
			elif action_type is 0:
				self.actually_show_dialog(action)
			elif action_type is 1:
				self.actually_show_button(action)
			elif action_type is 2:
				self.actually_set_background(action)
			elif action_type is 3:
				self.actually_goto_scene(action)
			elif action_type is 4:
				self.actually_close_game()
			elif action_type is 5:
				self.actually_play_song(action)
			elif action_type is 6:
				self.actually_wait_for_button_press()
			elif action_type is 7:
				self.actually_remove_all_buttons()
			elif action_type is 8:
				self.actually_show_text(action)
			elif action_type is 9:
				self.actually_hide_text(action)
			elif action_type is 10:
				self.actually_show_image(action)
			elif action_type is 11:
				self.actually_hide_image(action)
			elif action_type is 12:
				self.actually_move_image(action)

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

	def actually_hide_dialog_box(self):
		print("hide dialog box")
		if self.dialog_box is not None:
			self.removeItem(self.dialog_box)
			self.dialog_box = None

	def actually_show_button(self, data):
		button = Button(self, data[3], data[4], data[5], data[6], data[7], data[8], data[9])
		button.setX(data[1])
		button.setY(data[2])
		self.buttons.append(button)
		self.addItem(button)
		self.call_next_action()

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

	def actually_wait_for_button_press(self):
		self.current_action = -1

	def actually_remove_all_buttons(self):
		for b in self.buttons:
			self.removeItem(b)
		self.buttons = []
		self.call_next_action()

	def actually_show_text(self, data):
		text_item = QGraphicsTextItem()
		text_item.setZValue(5)
		if len(data) >= 8 and data[7] != None:
			text_item.setDefaultTextColor(QColor(data[7]))
		else:
			text_item.setDefaultTextColor(QColor("#FFFFFF"))

		text_item.setX(data[2])
		text_item.setY(data[3])
		text_item.setTextWidth(data[4])
		text_item.setPlainText(data[5])

		temp_font = text_item.font()
		temp_font.setPointSize(data[6])
		text_item.setFont(temp_font)

		self.addItem(text_item)
		self.texts[data[1]] = text_item
		self.call_next_action()

	def actually_hide_text(self, data):
		self.removeItem(self.texts[data[1]])
		self.texts[data[1]] = None
		self.call_next_action()

	def actually_show_image(self, data):
		image = None
		if isinstance(data[2], list):
			image = QGraphicsPixmapItem(QPixmap(data[2][0]))
			self.updatable_images.append([image, data[2], 0, 0, data[5]])
		else:
			image = QGraphicsPixmapItem(QPixmap(data[2]))
		image.setX(data[3])
		image.setY(data[4])
		self.addItem(image)
		self.images[data[1]] = image
		self.call_next_action()

	def actually_hide_image(self, data):
		self.removeItem(self.texts[data[1]])
		self.texts[data[1]] = None
		self.call_next_action()

	def actually_move_image(self, data):
		image_id = data[1]
		image = self.images[image_id]
		duration = data[4]
		x_speed = (data[2] - image.x()) / duration
		y_speed = (data[3] - image.y()) / duration
		callback = self.call_next_action if data[5] else None
		image_data = [image_id, x_speed, y_speed, duration, callback]
		self.moving_images.append(image_data)
		if not data[5]:
			self.call_next_action()

	# ==============================================
	# * Setup Calls
	# ==============================================

	def add_call(self, data):
		self.actions.append(data)
		self.check_if_first()

	# ==============================================
	# * Extended Calls
	# ==============================================

	# ==============================================
	# Adds a dialog to the game.
	#
	# Ex:
	#     self.add_dialog("Hello World!")
	# ==============================================
	def add_dialog(self, msg, fontSize=20):
		self.add_call([0, msg, fontSize])

	# ==============================================
	# Hides the dialog box
	#
	# Ex:
	#     self.hide_dialog_box()
	# ==============================================
	def hide_dialog_box(self):
		self.add_call([-1])

	# ==============================================
	# Adds a button to the game.
	# After adding all buttons, be sure to call "self.wait_for_button_press".
	# Check scenes/scene_titlescreen.py for example of "font" and "buttonColors"
	#
	# Ex:
	#     self.add_button(30, 30, 200, 200, "My Button!", self.another_function)
	# ==============================================
	def add_button(self, x, y, w, h, name, action, font=None, buttonColors=None, textColors=None):
		self.add_call([1, x, y, w, h, name, font, buttonColors, textColors, action])

	# ==============================================
	# Sets the current background.
	#
	# Ex:
	#     self.set_background("images/Background1.png")
	# ==============================================
	def set_background(self, path):
		self.add_call([2, path])

	# ==============================================
	# Changes the game to the provided scene.
	#
	# Ex:
	#     self.goto_scene(scenes.my_other_scene.My_Other_Scene)
	# ==============================================
	def goto_scene(self, scene):
		self.add_call([3, scene])

	# ==============================================
	# Closes the game.
	#
	# Ex:
	#     self.close_game()
	# ==============================================
	def close_game(self):
		self.add_call([4])

	# ==============================================
	# Plays a song.
	#
	# Ex:
	#     self.play_song("audio/testmusic2.mp3")
	# ==============================================
	def play_song(self, path):
		self.add_call([5, path])

	# ==============================================
	# Once all buttons are created, this will wait for the player to press one.
	#
	# Ex:
	#     self.wait_for_button_press()
	# ==============================================
	def wait_for_button_press(self):
		self.add_call([6])

	# ==============================================
	# Removes all buttons from the screen.
	#
	# Ex:
	#     self.remove_all_buttons()
	# ==============================================
	def remove_all_buttons(self):
		self.add_call([7])

	# ==============================================
	# Based on the value provided, there is a chance it will return True.
	#
	# Ex:
	#     if self.generate_random_chance(30):
	#		  # there is a 30% chance of this happening
	# 	  else:
	#		  # there is a 70% chance of this happening
	# ==============================================
	def generate_random_chance(self, val):
		return random.randint(0, 100) <= val

	# ==============================================
	# Shows text on the screen (not in dialog).
	# This function returns an ID that can be used in self.hide_text.
	#
	# Ex:
	#     text_id = self.show_text(10, 10, 200, "Hello Screen!", 40, "#FF44CC")
	# ==============================================
	def show_text(self, x, y, w, text, size=30, color=None):
		new_id = self.current_id
		self.current_id += 1
		self.add_call([8, new_id, x, y, w, text, size, color])
		return new_id

	# ==============================================
	# Hides the text connected to the ID.
	#
	# Ex:
	#     self.hide_text(text_id)
	# ==============================================
	def hide_text(self, text_id):
		self.add_call([9, text_id])

	# ==============================================
	# Shows a picture on the screen.
	# This function returns an ID that can be used in other functions.
	#
	# Ex:
	#     pic_id = self.show_picture("images/TestImage1.png", 30, 30)
	#
	# ----------------------------------------------
	#
	# Using an array of strings will create an animation.
	# In that case, the last argument is the frame-change frequency of the animation.
	#
	# Ex:
	#     pic_id = self.show_picture(["images/p1_frame_0.png", "images/p1_frame_1.png"], 100, 100, 30)
	# ==============================================
	def show_picture(self, path, x, y, animation_speed=20):
		new_id = self.current_id
		self.current_id += 1
		self.add_call([10, new_id, path, x, y, animation_speed])
		return new_id

	# ==============================================
	# Removes the picture connected to the provided ID.
	#
	# Ex:
	#     self.hide_picture(pic_id)
	# ==============================================
	def hide_picture(self, image_id):
		self.add_call([11, image_id])

	# ==============================================
	# Moves the picture to new coordinates over a duration of time.
	#
	# Ex:
	#     self.move_picture(pic_id, 90, 30, 120)
	# ==============================================
	def move_picture(self, image_id, x, y, duration, wait_until_finished=True):
		self.add_call([12, image_id, x, y, duration, wait_until_finished])

	#===============================================
	# Sets the vaccination status
	# True/False, 50% chance
	#===============================================
	def set_vaxx(self):
		if self.generate_random_chance(50):
			self.vaxx = True
		else:
			self.vaxx = False

	#===============================================
	# Sets the entry point
	# 0 is for blood (cut)
	# 1 is for stomach (mouth)
	#===============================================	
	def set_entry(self):
		if self.generate_random_chance(50):
			self.entry = 0
		else:
			self.entry = 1

	# ==============================================
	# Gets and sets global values
	#
	# Ex:
	#     self.set_value("Health", 100)
	#
	#     self.add_value("Health", -1)
	#
	#     if self.get_value("Health") <= 30:
	#         self.add_dialog("Player is less than 30 health!")
	# ==============================================
			
	def set_value(self, name, value):
		Scene_Base.GLOBAL_VARS[name] = value

	def add_value(self, name, value):
		Scene_Base.GLOBAL_VARS[name] += value

	def get_value(self, name):
		return Scene_Base.GLOBAL_VARS[name]



Scene_Base.GLOBAL_VARS = {}

