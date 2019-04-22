from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaPlaylist, QSoundEffect

class AudioPlayer:
	@classmethod
	def play_song(cls, path):
		if hasattr(cls, "current_song") and cls.current_song == path:
			return
		else:
			cls.current_song = path
		cls.music_list = QMediaPlaylist()
		cls.music_list.addMedia(QMediaContent(QUrl.fromLocalFile(path)))
		cls.music_list.setPlaybackMode(QMediaPlaylist.Loop)

		cls.music_player = QMediaPlayer()
		cls.music_player.setPlaylist(cls.music_list)
		cls.set_music_volume(100)
		cls.music_player.play()

	@classmethod
	def set_music_volume(cls, amount):
		cls.music_player.setVolume(amount)

	@classmethod
	def get_music_volume(cls):
		return cls.music_player.volume()

	@classmethod
	def set_se_volume(cls, amount):
		cls.se_volume = amount
		if hasattr(cls, "sound_effects"):
			for path, se in cls.sound_effects.items():
				se.setVolume(amount / 100)

	@classmethod
	def get_se_volume(cls):
		if not hasattr(cls, "se_volume"):
			return 100
		return cls.se_volume

	@classmethod
	def stop_song(cls):
		if hasattr(cls, "music_player"):
			cls.music_player.stop()

	@classmethod
	def preload_sound_effect(cls, path):
		if not hasattr(cls, "sound_effects"):
			cls.sound_effects = {}
			cls.se_volume = 100
		if path not in cls.sound_effects:
			se = QSoundEffect()
			se.setVolume(cls.se_volume / 100)
			se.setSource(QUrl.fromLocalFile(path))
			cls.sound_effects[path] = (se)

	@classmethod
	def play_sound_effect(cls, path):
		if hasattr(cls, "sound_effects"):
			if path in cls.sound_effects:
				cls.sound_effects[path].play()