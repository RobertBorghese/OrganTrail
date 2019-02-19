class Easer():
	def linear(t):
		return t
	def easeInQuad(t):
		return t*t
	def easeOutQuad(t):
		return t*(2-t)
	def easeInOutQuad(t):
		return 2*t*t if t<.5 else -1+(4-2*t)*t
	def easeInCubic(t):
		return t*t*t
	def easeOutCubic(t):
		q = t - 1
		return (q)*t*t+1
	def easeInOutCubic(t):
		return 4*t*t*t if t<.5 else (t-1)*(2*t-2)*(2*t-2)+1
	def easeInQuart(t):
		return t*t*t*t
	def easeOutQuart(t):
		q = t - 1
		return 1-(q)*t*t*t
	def easeInOutQuart(t):
		q = t - 1
		return 8*t*t*t*t if t<.5 else 1-8*(q)*t*t*t
	def easeInQuint():
		return t*t*t*t*t
	def easeOutQuint(t):
		q = t - 1
		return 1+(q)*t*t*t*t
	def easeInOutQuint(t):
		q = t - 1
		return 16*t*t*t*t*t if t<.5 else 1+16*(q)*t*t*t*t