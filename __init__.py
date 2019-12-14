from mycroft import MycroftSkill, intent_file_handler
import requests


class Http(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('http.intent')
    def handle_http(self, message):
        self.speak_dialog('http')
        requests.put('http://192.168.0.101/api/AmE3DbmI-V6GpnsBHqdG-g5NG7Xiz1AvUh8iMVt7/lights/12/state', data="{\"on\":false}")


def create_skill():
    return Http()

