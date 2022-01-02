from mycroft import MycroftSkill, intent_file_handler


class MusicPlaylist(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('playlist.music.intent')
    def handle_playlist_music(self, message):
        self.speak_dialog('playlist.music')


def create_skill():
    return MusicPlaylist()

