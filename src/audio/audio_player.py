from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaPlaylist, QSoundEffect

class AudioPlayer:
	@classmethod
	def play_song(cls, path):
		cls.music_list = QMediaPlaylist()
		cls.music_list.addMedia(QMediaContent(QUrl.fromLocalFile(path)))
		cls.music_list.setPlaybackMode(QMediaPlaylist.Loop)

		cls.music_player = QMediaPlayer()
		cls.music_player.setPlaylist(cls.music_list)
		cls.music_player.setVolume(100)
		cls.music_player.play()

	@classmethod
	def stop_song(cls):
		if hasattr(cls, "music_player"):
			cls.music_player.stop()

	@classmethod
	def preload_sound_effect(cls, path):
		if not hasattr(cls, "sound_effects"):
			cls.sound_effects = {}
		if path not in cls.sound_effects:
			se = QSoundEffect()
			se.setSource(QUrl.fromLocalFile(path))
			cls.sound_effects[path] = (se)

	@classmethod
	def play_sound_effect(cls, path):
		if hasattr(cls, "sound_effects"):
			if path in cls.sound_effects:
				cls.sound_effects[path].play()