from mycroft import MycroftSkill, intent_file_handler


class Http(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('http.intent')
    def handle_http(self, message):
        self.speak_dialog('http')


def create_skill():
    return Http()

