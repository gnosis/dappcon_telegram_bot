from datetime import datetime


class Event():
    def __init__(self, title, speakers, start_time, end_time, location, event_type):

        self.title = title
        self.location = location.title()
        self.type = event_type.title()

        if type(speakers) == list:
            self.speakers = speakers
        else:
            self.speakers = list(speakers.split(','))

        assert isinstance(start_time, datetime) and isinstance(end_time, datetime)

        self.start = start_time
        self.end = end_time

    def __str__(self):
        st = '{}:{}'.format(self.start.hour, self.start.minute or '00')
        en = '{}:{}'.format(self.end.hour, self.end.minute or '00')

        return '\n'.join([
            '{}-{}; {} at {}'.format(st, en, self.type.title(), self.location),
            self.title,
            '    - ' + '\n    - '.join(self.speakers),
        ])

    def __repr__(self):
        return str(self)

    def is_now(self):
        return self.start <= datetime.now() < self.end