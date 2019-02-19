from other.easing import Easer

# ---------------------------------------------------------------
# * Object_Base
#
# The parent class of all "objects"
# Each object can use the properties defined here.
# ---------------------------------------------------------------
class Object_Base():
	def __init__(self):
		self.x = 0
		self.y = 0
		self.width = 0
		self.height = 0
		self.motions = []
		self.obj = None
		self.create()

	def create(self):
		pass

	# This is called when the object starts.
	def start(self):
		pass

	# This is called to render the object to the screen. "window" is the window to render to.
	def draw(self):
		if self.obj != None:
			self.obj.draw()

	# This is called every frame to update the game logic.
	def update(self):
		if self.obj != None and len(self.motions) > 0:
			i = 0
			remove_ids = []
			while i < len(self.motions):
				m = self.motions[i]
				curr_time = m[3]
				curr_time += 1
				end_time = m[4]
				if curr_time == end_time:
					remove_ids.append(i)
				else:
					ratio = m[5](curr_time / end_time)
					setattr(self.obj, m[0], m[1] + ((m[2] - m[1]) * ratio))
					m[3] = curr_time
				i += 1
			for i in remove_ids:
				self.motions.pop(i)

	def add_motion(self, name, start, finish, duration, curve_type="easeOutQuad"):
		if isinstance(curve_type, str) and hasattr(Easer, curve_type):
			setattr(self.obj, name, start)
			self.motions.append([name, start, finish, 0, duration, getattr(Easer,curve_type)])

	# Called when the mouse enters the object.
	def on_mouse_entered(self):
		pass

	# Called when the mouse leaves the object.
	def on_mouse_leave(self):
		pass

	# Called when the mouse clicks on the object.
	def on_mouse_clicked(self, button):
		pass

# ---------------------------------------------------------------
