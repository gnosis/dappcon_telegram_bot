import json
from collections import namedtuple
from datetime import datetime
from event import Event


def dict_to_namedtuple(my_dict, name=None):
    return json.loads(
        json.dumps(my_dict),
        object_hook=lambda d: namedtuple(name or 'X', d.keys())(*d.values())
    )

def make_event(json_str):
    elt = dict_to_namedtuple(json_str)
    return Event(
        title=elt.title,
        speakers=elt.speakers,
        start_time=datetime.strptime(elt.start, '%Y-%m-%d %H:%M'),
        end_time=datetime.strptime(elt.end, '%Y-%m-%d %H:%M'),
        location=elt.location,
        event_type=elt.event_type
    )

def load_schedule():
    raw_events = []
    for file_name in ['main_stage', 'side_stage', 'workshop']:
        with open('data/{}.json'.format(file_name), 'r') as file:
            stage_list = json.loads(file.read())
            raw_events += stage_list

    return [make_event(r) for r in raw_events]