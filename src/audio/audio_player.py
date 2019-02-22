from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent, QMediaPlaylist

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