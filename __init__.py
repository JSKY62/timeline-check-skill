from mycroft import MycroftSkill, intent_file_handler


class TimelineCheck(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('check.timeline.intent')
    def handle_check_timeline(self, message):
        self.speak_dialog('check.timeline')


def create_skill():
    return TimelineCheck()

